""" Data retrieval from DTC server
Use dtc_download() function. It will yield generator with market data. Beware of possible gaps.
Beware that the first yielded object is general information!
"""
import logging
import selectors
import socket
import struct
import threading
import time as t
import collections
from pandas import to_datetime
from google.protobuf import json_format

from pydtc.DTC import DTCProtocol_pb2 as Dtc
from pydtc.common import InterruptibleThread, Progress, str_to_tstamp, now
from pydtc.datadefs import MktDataEntry

import typing
if typing.TYPE_CHECKING:
    from typing import Union

# Mapping message type to DTC message object and human readable name
DTC_MTYPE_MAP = {
    Dtc.ENCODING_REQUEST: (Dtc.EncodingRequest, "encoding request"),
    Dtc.ENCODING_RESPONSE: (Dtc.EncodingResponse, "encoding response"),
    Dtc.LOGON_REQUEST: (Dtc.LogonRequest, "logon request"),
    Dtc.LOGON_RESPONSE: (Dtc.LogonResponse, "logon response"),
    Dtc.HEARTBEAT: (Dtc.Heartbeat, "heartbeat"),
    Dtc.MARKET_DATA_SNAPSHOT: (Dtc.MarketDataSnapshot, "market data snapshot"),
    Dtc.HISTORICAL_PRICE_DATA_REQUEST: (Dtc.HistoricalPriceDataRequest, "historical data request"),
    Dtc.HISTORICAL_PRICE_DATA_REJECT: (Dtc.HistoricalPriceDataReject, "historical data reject"),
    Dtc.HISTORICAL_PRICE_DATA_RESPONSE_HEADER: (Dtc.HistoricalPriceDataResponseHeader,
                                                "historical data response header"),
    Dtc.HISTORICAL_PRICE_DATA_RECORD_RESPONSE: (Dtc.HistoricalPriceDataRecordResponse,
                                                "historical data record response"),
    Dtc.LOGOFF: (Dtc.Logoff, "logoff"),
    Dtc.GENERAL_LOG_MESSAGE: (Dtc.GeneralLogMessage, "general log message")
}

TYPE_TO_STRUCT_FORMAT = {
    1: "i",  # CPPTYPE_INT32
    2: "l",  # CPPTYPE_INT64
    3: "I",  # CPPTYPE_UINT32
    4: "L",  # CPPTYPE_UINT64
    5: "d",  # CPPTYPE_DOUBLE
    6: "f",  # CPPTYPE_FLOAT
    7: "?",  # CPPTYPE_BOOL
    8: "ENUM",  # CPPTYPE_ENUM; Special handling required
    9: "s",  # CPPTYPE_STRING
    10: "s"  # CPPTYPE_MESSAGE; TODO: this is an assumption, needs review
}


def dtc_bin_encoder(message):
    """ Encode DTC Message object to little-endian binary string
    Args:
        message (DtcProtocol): DTC Protocol message object (e.g. Dtc.EncodingRequest())
    Returns:
        bytes: binary message representation
    """
    bin_msg = b""  # (bytes): binary message
    # We use message.DESCRIPTOR to fetch its format and values
    for f in message.DESCRIPTOR.fields:
        struct_fmt = TYPE_TO_STRUCT_FORMAT[f.cpp_type]  # (str): struct format character
        f_value = getattr(message, f.name)  # field value
        if struct_fmt == 'ENUM':
            # Detect enum type and set normal struct format symbol
            # WARNING! HARDCODED VALUES AHEAD
            # TODO: check for sendable only
            # uint16_t enums
            if f.enum_type.name == ("AtBidOrAskEnum" or "HistoricalPriceDataRejectReasonCodeEnum"):
                struct_fmt = "H"
            # uint8_t enums
            elif f.enum_type.name == ("MarketDepthUpdateTypeEnum" or "PartialFillHandlingEnum" or "PutCallEnum"):
                struct_fmt = "B"
            else:
                struct_fmt = "i"
        if struct_fmt == 's':
            # Serialize string field before packing
            f_value = f_value.encode()
            str_len = str(len(f_value))
            bin_msg += struct.pack('<' + str_len + struct_fmt, f_value) + b'\x00'  # little-endian
        else:
            # For other types - just pack
            bin_msg += struct.pack('<' + struct_fmt, f_value)  # little-endian
    return bin_msg


def dtc_bin_decoder(dtc_message, bin_message):
    """ Decode little-endian binary string to DTC Message object
    Args:
        dtc_message (DtcProtocol): DTC Protocol message object (e.g. Dtc.EncodingRequest())
        bin_message (bytes): binary message body (without header)
    Returns:
        DtcProtocol: DTC Protocol message object with the set fields
    """
    bytes_unpacked = 0  # (int): number of bytes that we've already read from the msg_body
    string_field_count = 0  # (int): how many string fields have been extracted so far
    # We use dtc_message.DESCRIPTOR to fetch its format and extract fields one by one
    fields = dtc_message.DESCRIPTOR.fields
    for f in fields:
        struct_fmt = TYPE_TO_STRUCT_FORMAT[f.cpp_type]  # (str): struct format character
        # print("Fname: {}; bytes_unpacked: {}".format(f.name, bytes_unpacked))
        if struct_fmt == 'ENUM':
            # Detect enum type and set normal struct format symbol
            # WARNING! HARDCODED VALUES AHEAD
            # TODO: check for receivable only
            # uint16_t enums
            if f.enum_type.name == ("AtBidOrAskEnum" or "HistoricalPriceDataRejectReasonCodeEnum"):
                struct_fmt = "H"
            # uint8_t enums
            elif f.enum_type.name == ("MarketDepthUpdateTypeEnum" or "PartialFillHandlingEnum"
                                      or "PutCallEnum"):
                struct_fmt = "B"
            else:
                struct_fmt = "i"
        if struct_fmt == 's':
            # Strings are always delimited by null terminator. Extract it, determine length and unpack
            bin_value = bin_message[bytes_unpacked:].split(b'\x00')[string_field_count]
            field_bin_length = len(bin_value)
            value = struct.unpack('<' + str(field_bin_length) + struct_fmt, bin_value)[0]  # (str): encoded
            # Write to DTC Message object the unpacked bytes
            setattr(dtc_message, f.name, value.decode())
            bytes_unpacked += field_bin_length
        else:
            field_bin_length = struct.calcsize(struct_fmt)
            # Slice out interesting bytes
            bin_value = bin_message[bytes_unpacked:bytes_unpacked + field_bin_length]
            # Write to DTC Message object the unpacked bytes
            setattr(dtc_message, f.name,
                    struct.unpack('<' + struct_fmt, bin_value)[0])  # little-endian
            bytes_unpacked += field_bin_length

    return dtc_message


def send_message(m, m_type, sock):
    """ Prepend header to the message and send it to the specified socket
    Args:
        m (bytes): binary message to send
        m_type (int): Dtc message ID
        sock (socket.socket): socket connection
    """
    total_len = 4 + len(m)  # 2 bytes Size + 2 bytes Type
    header = struct.pack('<HH', total_len, m_type)  # Prepare 4-byte little-endian header
    sock.send(header + m)  # Send message
    if logging.root.level <= logging.DEBUG:
        logging.debug("Sent {0}".format(DTC_MTYPE_MAP[m_type][1]))


class DTCProtobufHeartbeat(InterruptibleThread):
    """ Separate thread for sending DTC heartbeat to a socket in the google.protobuf format
    Attributes:
        sock (socket.socket): socket where heartbeats are sent
        period (int): interval between heartbeats
        message (bytes): serialized DTC heartbeat message
    """

    def __init__(self, sock, period):
        """
        Args:
            sock (socket.socket): where to send heartbeats
            period (int): heartbeat period in seconds
        """
        super().__init__()
        self.name = "Heartbeat"
        self.daemon = True
        self.sock = sock
        self.period = period
        self.message = Dtc.Heartbeat().SerializeToString()

    def run(self):
        """ Send heartbeats while self.running flag is True """
        while self.running:
            send_message(self.message, Dtc.HEARTBEAT, self.sock)
            self.event.wait(self.period)


class DTCMessageReceiver(InterruptibleThread):
    """ Infinitely receive new messages in separate thread
    Attributes:
        sock (socket.socket): source socket
        messages (list[tuple[int, DtcProtocol]]): list of tuples, where [0] is message type and [1] is
            deserialized DTC Protocol message object
        selector (selectors.DefaultSelector): select() syscall exposure to listen for IO events, i.e. incoming packets
        data_arrival_event (threading.Event): event is triggered upon first historical data message arrival
            Listened by upstream DtcConnection to get first timestamp
    """

    def __init__(self, sock, condition):
        """
        Args:
            sock (socket.socket): from where to receive messages
            condition (threading.Condition): lock for notification of new messages available
        """
        super().__init__()
        self.daemon = True
        self.name = "MessageReceiver"
        self.sock = sock
        self.condition = condition
        self.messages = collections.deque()
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.sock, selectors.EVENT_READ)
        self.data_arrival_event = threading.Event()
        if logging.root.level <= logging.DEBUG:
            logging.debug("Receiver initialized")

    def run(self):
        """ Receive a message and then wait for signal to receive other messages """
        while self.running:
            # Listen for input event on the socket
            self.selector.select()
            self._get_message()

    def _get_message(self):
        """ Receive a message from the socket """
        msg_header = self.sock.recv(4)  # Receive header
        if msg_header:
            # First 2 bytes must be message size. Subtract 4 to get only body size
            msg_size = struct.unpack_from('<H', msg_header)[0]
            # 2 bytes with offset of 2 must be message type code
            msg_type = struct.unpack_from('<H', msg_header, 2)[0]
            # Now receive message body of known length
            try:
                msg_body = self.sock.recv(msg_size - 4)
            except OSError:
                # Socket must've been closed while we were picking at the header. This happens when there's,
                # for example, heartbeat arriving after the final message, but we don't care anymore
                pass
            else:
                # Once received, construct DTC message object and deserialize the received bytes
                try:
                    dtc_message = DTC_MTYPE_MAP[msg_type][0]()
                except KeyError:
                    if logging.root.level <= logging.WARN:
                        logging.warning("Received unknown message type: {0}".format(msg_type))
                else:
                    if logging.root.level <= logging.DEBUG:
                        logging.debug("Received {0}".format(DTC_MTYPE_MAP[msg_type][1]))
                    if msg_type == Dtc.ENCODING_RESPONSE:
                        # Encoding Response is always binary
                        dtc_message = dtc_bin_decoder(dtc_message, msg_body)
                    elif not self.data_arrival_event.is_set() and msg_type == Dtc.HISTORICAL_PRICE_DATA_RECORD_RESPONSE:
                        # We've got first historical data record. Signal other threads and forget about it
                        self.data_arrival_event.set()
                        dtc_message.ParseFromString(msg_body)
                    else:
                        dtc_message.ParseFromString(msg_body)
                    # Lock message list, add the message there, notify others about it and release the lock
                    with self.condition:
                        # Do not store heartbeat messages
                        if msg_type != Dtc.HEARTBEAT:
                            self.messages.append((msg_type, dtc_message))
                            self.condition.notify()
                    if logging.root.level <= logging.DEBUG:
                        logging.debug(json_format.MessageToJson(dtc_message))


class DtcConnection(object):
    """ DTC connection and data retrieval
    Attributes:
        sock (socket.socket): TCP/IP connection
        heartbeat (DTCProtobufHeartbeat): heartbeat thread (only for intraday connection)
        receiver (DTCMessageReceiver): message receiving thread
        historical (bool): True if this is historical data connection
        hist_rec_interval (int): Record interval of historical data
        hist_start_tstamp (int): First timestamp in the received data
        successful (bool): Data download is successful
        reception_complete (bool): All messages received
    """

    def __init__(self, dtc_server, heartbeat_interval=10, encoding=Dtc.PROTOCOL_BUFFERS, historical=True):
        """ Open a connection and login
        Args:
            dtc_server (tuple[str, int]): IP and port of the DTC server
            heartbeat_interval (int): interval between heartbeats in seconds
            encoding (int): DTC Protocol Encoding (binary by default), as historical connections supports only binary
            historical (bool): True if this is historical data connection
        """
        self.historical = historical
        self.hist_rec_interval = 0  # Just init, rewritten in self.historical_data_request
        self.hist_start_tstamp = 0
        self.successful = True
        self.reception_complete = False
        # Connect
        self.sock = socket.create_connection(dtc_server)

        self.condition = threading.Condition()  # Provider/consumer lock with receiver
        # Start message listener thread
        self.receiver = DTCMessageReceiver(self.sock, self.condition)
        self.receiver.start()

        enc_req = Dtc.EncodingRequest()
        enc_req.ProtocolVersion = Dtc.CURRENT_VERSION
        enc_req.Encoding = encoding
        enc_req.ProtocolType = "DTC"
        message = dtc_bin_encoder(enc_req)
        send_message(message, Dtc.ENCODING_REQUEST, self.sock)
        with self.condition:
            # Wait for response
            self.condition.wait()
            enc_resp = self.receiver.messages.popleft()
        assert (enc_resp[1].Encoding == encoding)  # We expect server to support requested encoding

        # Construct and send Logon Request
        logon_req = Dtc.LogonRequest()
        logon_req.ProtocolVersion = Dtc.CURRENT_VERSION
        logon_req.Username = "wat"
        logon_req.Password = "wat"
        if self.historical:
            # Don't send heartbeats for historical connections
            logon_req.HeartbeatIntervalInSeconds = -1
        else:
            logon_req.HeartbeatIntervalInSeconds = heartbeat_interval
        logon_req.ClientName = "wat"

        message = logon_req.SerializeToString()
        send_message(message, Dtc.LOGON_REQUEST, self.sock)
        with self.condition:
            # Wait for response
            self.condition.wait()
            logon_resp = self.receiver.messages.popleft()
        if logon_resp[1].Result != Dtc.LOGON_SUCCESS:
            logging.error(logon_resp[1].ResultText)
            self.disconnect()
        if logging.root.level <= logging.DEBUG:
            logging.debug("Receiver buffer: {0} message(s)".format(len(self.receiver.messages)))

        if not self.historical:
            # Begin sending heartbeats
            self.heartbeat = DTCProtobufHeartbeat(self.sock, heartbeat_interval)
            self.heartbeat.start()
        else:
            # Monitor download progress in a separate thread
            self.watcher = DtcDownloadWatcher(self)

    def disconnect(self):
        """ Gracefully logoff and close the connection """
        logging.debug("Disconnecting from DTC server")
        # Stop threads
        self.receiver.stop()
        if not self.historical:
            self.heartbeat.stop()
            # Send LOGOFF message
            logoff = Dtc.Logoff()
            logoff.Reason = "Client terminating"
            message = logoff.SerializeToString()
            send_message(message, Dtc.LOGOFF, self.sock)
        # Gracefully close the socket
        self.sock.close()

    def intraday_data_request(self, request_action, symbol, exchange):
        # TODO: this is prototype function and needs to be finalized
        """ Request data from the server
        Args:
            request_action (int): DTC Protocol RequestAction code (e.g. Dtc.SNAPSHOT)
            symbol (str): obviously, symbol :)
            exchange (str): exchange (e.g. "Bitcoin")
        """
        data_req = Dtc.MarketDataRequest()
        data_req.RequestAction = request_action
        data_req.SymbolID = 1  # TODO: Make sure this is unique when requesting multiple symbols
        data_req.Symbol = symbol
        data_req.Exchange = exchange
        message = data_req.SerializeToString()
        send_message(message, Dtc.MARKET_DATA_REQUEST, self.sock)

    def historical_data_request(self, symbol, exchange, rec_interval=Dtc.INTERVAL_1_MINUTE,
                                start=0, end=0):
        """ Request historical data from the server
        Args:
            symbol (str): symbol, oh yes
            exchange (str): exchange (e.g. "Bitcoin")
            rec_interval (int): one of Dtc.INTERVAL_* values. Basically, data resolution
            start (int): data begin timestamp. Earliest available by default
            end (int): data end timestamp. Latest available by default
        """
        self.hist_rec_interval = rec_interval
        self.hist_start_tstamp = start
        data_req = Dtc.HistoricalPriceDataRequest()
        data_req.RequestID = 1  # TODO: make sure it's incrementing with new requests if we reuse the connection
        data_req.Symbol = symbol
        data_req.Exchange = exchange
        data_req.RecordInterval = rec_interval
        data_req.StartDateTime = start
        data_req.EndDateTime = end
        data_req.MaxDaysToReturn = 0
        message = data_req.SerializeToString()
        send_message(message, Dtc.HISTORICAL_PRICE_DATA_REQUEST, self.sock)
        with self.condition:
            # Wait for response
            self.condition.wait()
            hist_resp = self.receiver.messages.popleft()
        if hist_resp[0] == Dtc.HISTORICAL_PRICE_DATA_REJECT:
            # If we got reject - display reject text and disconnect
            logging.error(hist_resp[1].RejectText)
            self.successful = False
            self.disconnect()
        elif hist_resp[0] == Dtc.GENERAL_LOG_MESSAGE:
            logging.warning("Got general message from server: '{}'".format(hist_resp[1].MessageText))
        elif bool(hist_resp[1].NoRecordsToReturn):
            # If no records available - give warning and disconnect
            logging.warning("No historical data records available. Check symbol name.")
            self.successful = False
            self.disconnect()
        # Now wait for the first data packet signalled by the MessageReceiver thread
        self.receiver.data_arrival_event.wait()
        # Once we have first data message - get the timestamp from it and start download watcher
        self.hist_start_tstamp = self.receiver.messages[0][1].StartDateTime
        self.watcher.start()

    def estimated_records(self, ts=now()):
        """ Estimate number of records between data start and given timestamp. Used for progress calculation
        Args:
            ts (int): timestamp for which to evaluate record number. Default: current time
        Returns:
            int: estimated number of records
        """
        # Warning: `end` parameter of `self.historical_data_request` is not used
        return round((ts - self.hist_start_tstamp) / self.hist_rec_interval)


class DtcDownloadWatcher(threading.Thread):
    """ Download progress watcher and metering thread
    Attributes:
        last_message (bool): If the last data historical message has been received
        last_record_count (int): Latest information on number of historical record messages in the deque
        last_deque_length (int): Latest information on overall deque length
        hc (DtcConnection): DTC Historical connection
        finished_event (threading.Event): condition lock to notify others that reception is over
    """

    def __init__(self, historical_connection):
        """
        Args:
            historical_connection (DtcConnection): DTC Historical connection instance
        """
        super().__init__()
        self.name = "DownloadWatcher"
        self.last_message = False
        self.last_record_count = 0
        self.last_deque_length = 0
        self.hc = historical_connection
        self.finished_event = threading.Event()

    def run(self):
        """ Check received messages, draw progress and disconnect when last message found """
        # Wait for MessageReceiver to report first data message arrival
        self.hc.receiver.data_arrival_event.wait()
        download_pbar = Progress(desc="Downloading data", unit="records", total=self.hc.estimated_records())
        # Real number of messages could be lower if there are gaps in data
        with download_pbar:
            while not self.last_message and not self.hc.reception_complete:
                with self.hc.condition:
                    try:
                        msg = self.hc.receiver.messages[-1]  # tuple[int, Dtc.Message]: msg_type and msg_object
                    except IndexError:
                        # Deque is empty. Okay... Let's wait
                        self.hc.condition.wait()
                    else:
                        if msg[0] == Dtc.HISTORICAL_PRICE_DATA_RECORD_RESPONSE or \
                                        msg[0] == Dtc.HISTORICAL_PRICE_DATA_RECORD_RESPONSE_INT:
                            # If this is historical data message - calculate progress
                            self.last_message = bool(msg[1].IsFinalRecord)
                            current_record_count = self.hc.estimated_records(msg[1].StartDateTime)
                            download_pbar.update(max(0, current_record_count - self.last_record_count))
                            self.last_record_count = current_record_count
                            # And wait for the next message if we haven't received the last one yet.
                            if not self.last_message:
                                # We cannot put this wait() in the beginning of the loop, as it may happen that the
                                # last message has already been received while we've been initializing the progress bar
                                self.hc.condition.wait()
        t.sleep(0.1)  # Let MessageReceiver finish its job
        logging.debug("{}: reception complete".format(self.name))
        self.hc.disconnect()
        self.hc.reception_complete = True
        self.finished_event.set()  # Notify other threads that reception is complete


def dtc_download(symbol, exchange="Bitcoin", start_date="01.01.1970", server=("127.0.0.1", 11101), debug=False):
    """ Download historical data over DTC protocol
    Args:
        symbol (str): symbol, oh yes
        exchange (str): exchange (e.g. "Bitcoin")
        start_date (Union[str, int]): date in any format
        server (tuple[str, int]): IP and port of the DTC server
        debug (bool): toggle very verbose logging (all messages will be shown)
    Yields:
        dict[str, Union(int, str)]: First yielded object is a dictionary with general info
        MktDataEntry: Market data
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    start_tstamp = str_to_tstamp(start_date)
    # Connect and request data
    hist_conn = DtcConnection(server)
    hist_conn.historical_data_request(symbol, exchange, start=start_tstamp)

    if not hist_conn.successful:
        return

    msgs = hist_conn.receiver.messages
    # Wait while messages appear in the deque if it's empty
    if len(msgs) == 0:
        logging.debug("Main thread is waiting for messages")
        with hist_conn.condition:
            hist_conn.condition.wait()

    # Although it was initially designed that message consumption is done in parallel to the reception,
    # practice has shown that it is much faster to do this sequentially. Message reception is significantly
    # slowed down by the consumption for some reason. Thus, we wait here for the watcher to report that
    # reception is over and only then proceed to consumption (unless everything has already been received).
    # Parallel reception code parts are not removed in hopes to implement parallelism through multiprocessing.
    if not hist_conn.reception_complete:
        logging.debug("Main thread is waiting for reception to complete")
        hist_conn.watcher.finished_event.wait()

    # First yielded object would be general info
    yield {"exchange": exchange, "symbol": symbol, "rec_interval": hist_conn.hist_rec_interval}
    # Now measure progress of deque consumption
    preproc_pbar = Progress(desc="Preprocessing data", unit="records", total=hist_conn.estimated_records())
    with preproc_pbar:
        while len(msgs) > 0 or not hist_conn.reception_complete:
            if len(msgs) > 0:
                # Messages available for consumption. Scan until we find the necessary type
                msg_type = -1
                while msg_type != Dtc.HISTORICAL_PRICE_DATA_RECORD_RESPONSE:
                    msg_type, msg = msgs.popleft()
                if bool(msg.IsFinalRecord):
                    # We found last message. Set the complete flag on the connection.
                    hist_conn.reception_complete = True
                preproc_pbar.update()
                yield MktDataEntry(
                    time=to_datetime(msg.StartDateTime, unit="s", utc=True),
                    o=msg.OpenPrice,
                    h=msg.HighPrice,
                    l=msg.LowPrice,
                    c=msg.LastPrice,
                    vol=msg.Volume,
                    tcount=msg.NumTrades,
                    bidv=msg.BidVolume,
                    askv=msg.AskVolume
                )
            else:
                t.sleep(0.1)
