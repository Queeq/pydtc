from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DTCVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DTC_VERSION_UNSET: _ClassVar[DTCVersion]
    CURRENT_VERSION: _ClassVar[DTCVersion]

class DTCMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_TYPE_UNSET: _ClassVar[DTCMessageType]
    LOGON_REQUEST: _ClassVar[DTCMessageType]
    LOGON_RESPONSE: _ClassVar[DTCMessageType]
    HEARTBEAT: _ClassVar[DTCMessageType]
    LOGOFF: _ClassVar[DTCMessageType]
    ENCODING_REQUEST: _ClassVar[DTCMessageType]
    ENCODING_RESPONSE: _ClassVar[DTCMessageType]
    MARKET_DATA_REQUEST: _ClassVar[DTCMessageType]
    MARKET_DATA_REJECT: _ClassVar[DTCMessageType]
    MARKET_DATA_SNAPSHOT: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_TRADE: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_TRADE_COMPACT: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_LAST_TRADE_SNAPSHOT: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR_2: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_BID_ASK: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_BID_ASK_COMPACT: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_BID_ASK_NO_TIMESTAMP: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_BID_ASK_FLOAT_WITH_MICROSECONDS: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_SESSION_OPEN: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_SESSION_HIGH: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_SESSION_LOW: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_SESSION_VOLUME: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_OPEN_INTEREST: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_SESSION_SETTLEMENT: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_SESSION_NUM_TRADES: _ClassVar[DTCMessageType]
    MARKET_DATA_UPDATE_TRADING_SESSION_DATE: _ClassVar[DTCMessageType]
    MARKET_DEPTH_REQUEST: _ClassVar[DTCMessageType]
    MARKET_DEPTH_REJECT: _ClassVar[DTCMessageType]
    MARKET_DEPTH_SNAPSHOT_LEVEL: _ClassVar[DTCMessageType]
    MARKET_DEPTH_SNAPSHOT_LEVEL_FLOAT: _ClassVar[DTCMessageType]
    MARKET_DEPTH_UPDATE_LEVEL: _ClassVar[DTCMessageType]
    MARKET_DEPTH_UPDATE_LEVEL_FLOAT_WITH_MILLISECONDS: _ClassVar[DTCMessageType]
    MARKET_DEPTH_UPDATE_LEVEL_NO_TIMESTAMP: _ClassVar[DTCMessageType]
    MARKET_DATA_FEED_STATUS: _ClassVar[DTCMessageType]
    MARKET_DATA_FEED_SYMBOL_STATUS: _ClassVar[DTCMessageType]
    TRADING_SYMBOL_STATUS: _ClassVar[DTCMessageType]
    MARKET_ORDERS_REQUEST: _ClassVar[DTCMessageType]
    MARKET_ORDERS_REJECT: _ClassVar[DTCMessageType]
    MARKET_ORDERS_ADD: _ClassVar[DTCMessageType]
    MARKET_ORDERS_MODIFY: _ClassVar[DTCMessageType]
    MARKET_ORDERS_REMOVE: _ClassVar[DTCMessageType]
    MARKET_ORDERS_SNAPSHOT_MESSAGE_BOUNDARY: _ClassVar[DTCMessageType]
    SUBMIT_NEW_SINGLE_ORDER: _ClassVar[DTCMessageType]
    SUBMIT_NEW_OCO_ORDER: _ClassVar[DTCMessageType]
    SUBMIT_FLATTEN_POSITION_ORDER: _ClassVar[DTCMessageType]
    FLATTEN_POSITIONS_FOR_TRADE_ACCOUNT: _ClassVar[DTCMessageType]
    CANCEL_ORDER: _ClassVar[DTCMessageType]
    CANCEL_REPLACE_ORDER: _ClassVar[DTCMessageType]
    OPEN_ORDERS_REQUEST: _ClassVar[DTCMessageType]
    OPEN_ORDERS_REJECT: _ClassVar[DTCMessageType]
    ORDER_UPDATE: _ClassVar[DTCMessageType]
    HISTORICAL_ORDER_FILLS_REQUEST: _ClassVar[DTCMessageType]
    HISTORICAL_ORDER_FILL_RESPONSE: _ClassVar[DTCMessageType]
    HISTORICAL_ORDER_FILLS_REJECT: _ClassVar[DTCMessageType]
    CURRENT_POSITIONS_REQUEST: _ClassVar[DTCMessageType]
    CURRENT_POSITIONS_REJECT: _ClassVar[DTCMessageType]
    POSITION_UPDATE: _ClassVar[DTCMessageType]
    ADD_CORRECTING_ORDER_FILL: _ClassVar[DTCMessageType]
    CORRECTING_ORDER_FILL_RESPONSE: _ClassVar[DTCMessageType]
    TRADE_ACCOUNTS_REQUEST: _ClassVar[DTCMessageType]
    TRADE_ACCOUNT_RESPONSE: _ClassVar[DTCMessageType]
    EXCHANGE_LIST_REQUEST: _ClassVar[DTCMessageType]
    EXCHANGE_LIST_RESPONSE: _ClassVar[DTCMessageType]
    SYMBOLS_FOR_EXCHANGE_REQUEST: _ClassVar[DTCMessageType]
    UNDERLYING_SYMBOLS_FOR_EXCHANGE_REQUEST: _ClassVar[DTCMessageType]
    SYMBOLS_FOR_UNDERLYING_REQUEST: _ClassVar[DTCMessageType]
    SECURITY_DEFINITION_FOR_SYMBOL_REQUEST: _ClassVar[DTCMessageType]
    SECURITY_DEFINITION_RESPONSE: _ClassVar[DTCMessageType]
    SYMBOL_SEARCH_REQUEST: _ClassVar[DTCMessageType]
    SECURITY_DEFINITION_REJECT: _ClassVar[DTCMessageType]
    ACCOUNT_BALANCE_REQUEST: _ClassVar[DTCMessageType]
    ACCOUNT_BALANCE_REJECT: _ClassVar[DTCMessageType]
    ACCOUNT_BALANCE_UPDATE: _ClassVar[DTCMessageType]
    ACCOUNT_BALANCE_ADJUSTMENT: _ClassVar[DTCMessageType]
    ACCOUNT_BALANCE_ADJUSTMENT_REJECT: _ClassVar[DTCMessageType]
    ACCOUNT_BALANCE_ADJUSTMENT_COMPLETE: _ClassVar[DTCMessageType]
    HISTORICAL_ACCOUNT_BALANCES_REQUEST: _ClassVar[DTCMessageType]
    HISTORICAL_ACCOUNT_BALANCES_REJECT: _ClassVar[DTCMessageType]
    HISTORICAL_ACCOUNT_BALANCE_RESPONSE: _ClassVar[DTCMessageType]
    USER_MESSAGE: _ClassVar[DTCMessageType]
    GENERAL_LOG_MESSAGE: _ClassVar[DTCMessageType]
    ALERT_MESSAGE: _ClassVar[DTCMessageType]
    JOURNAL_ENTRY_ADD: _ClassVar[DTCMessageType]
    JOURNAL_ENTRIES_REQUEST: _ClassVar[DTCMessageType]
    JOURNAL_ENTRIES_REJECT: _ClassVar[DTCMessageType]
    JOURNAL_ENTRY_RESPONSE: _ClassVar[DTCMessageType]
    HISTORICAL_PRICE_DATA_REQUEST: _ClassVar[DTCMessageType]
    HISTORICAL_PRICE_DATA_RESPONSE_HEADER: _ClassVar[DTCMessageType]
    HISTORICAL_PRICE_DATA_REJECT: _ClassVar[DTCMessageType]
    HISTORICAL_PRICE_DATA_RECORD_RESPONSE: _ClassVar[DTCMessageType]
    HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE: _ClassVar[DTCMessageType]
    HISTORICAL_PRICE_DATA_RESPONSE_TRAILER: _ClassVar[DTCMessageType]
    HISTORICAL_MARKET_DEPTH_DATA_REQUEST: _ClassVar[DTCMessageType]
    HISTORICAL_MARKET_DEPTH_DATA_RESPONSE_HEADER: _ClassVar[DTCMessageType]
    HISTORICAL_MARKET_DEPTH_DATA_REJECT: _ClassVar[DTCMessageType]
    HISTORICAL_MARKET_DEPTH_DATA_RECORD_RESPONSE: _ClassVar[DTCMessageType]
    TRADE_ACCOUNT_TRADING_IS_DISABLED_REQUEST: _ClassVar[DTCMessageType]
    TRADE_ACCOUNT_TRADING_IS_DISABLED_RESPONSE: _ClassVar[DTCMessageType]

class EncodingEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BINARY_ENCODING: _ClassVar[EncodingEnum]
    BINARY_WITH_VARIABLE_LENGTH_STRINGS: _ClassVar[EncodingEnum]
    JSON_ENCODING: _ClassVar[EncodingEnum]
    JSON_COMPACT_ENCODING: _ClassVar[EncodingEnum]
    PROTOCOL_BUFFERS: _ClassVar[EncodingEnum]

class LogonStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGON_STATUS_UNSET: _ClassVar[LogonStatusEnum]
    LOGON_SUCCESS: _ClassVar[LogonStatusEnum]
    LOGON_ERROR: _ClassVar[LogonStatusEnum]
    LOGON_ERROR_NO_RECONNECT: _ClassVar[LogonStatusEnum]
    LOGON_RECONNECT_NEW_ADDRESS: _ClassVar[LogonStatusEnum]

class MessageSupportedEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_UNSUPPORTED: _ClassVar[MessageSupportedEnum]
    MESSAGE_SUPPORTED: _ClassVar[MessageSupportedEnum]

class RequestActionEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUEST_ACTION_UNSET: _ClassVar[RequestActionEnum]
    SUBSCRIBE: _ClassVar[RequestActionEnum]
    UNSUBSCRIBE: _ClassVar[RequestActionEnum]
    SNAPSHOT: _ClassVar[RequestActionEnum]

class UnbundledTradeIndicatorEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNBUNDLED_TRADE_NONE: _ClassVar[UnbundledTradeIndicatorEnum]
    FIRST_SUB_TRADE_OF_UNBUNDLED_TRADE: _ClassVar[UnbundledTradeIndicatorEnum]
    LAST_SUB_TRADE_OF_UNBUNDLED_TRADE: _ClassVar[UnbundledTradeIndicatorEnum]

class TradeConditionEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_CONDITION_NONE: _ClassVar[TradeConditionEnum]
    TRADE_CONDITION_NON_LAST_UPDATE_EQUITY_TRADE: _ClassVar[TradeConditionEnum]
    TRADE_CONDITION_ODD_LOT_EQUITY_TRADE: _ClassVar[TradeConditionEnum]

class OrderStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_STATUS_UNSPECIFIED: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_ORDER_SENT: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_PENDING_OPEN: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_PENDING_CHILD: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_OPEN: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_PENDING_CANCEL_REPLACE: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_PENDING_CANCEL: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_FILLED: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_CANCELED: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_REJECTED: _ClassVar[OrderStatusEnum]
    ORDER_STATUS_PARTIALLY_FILLED: _ClassVar[OrderStatusEnum]

class OrderUpdateReasonEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_UPDATE_REASON_UNSET: _ClassVar[OrderUpdateReasonEnum]
    OPEN_ORDERS_REQUEST_RESPONSE: _ClassVar[OrderUpdateReasonEnum]
    NEW_ORDER_ACCEPTED: _ClassVar[OrderUpdateReasonEnum]
    GENERAL_ORDER_UPDATE: _ClassVar[OrderUpdateReasonEnum]
    ORDER_FILLED: _ClassVar[OrderUpdateReasonEnum]
    ORDER_FILLED_PARTIALLY: _ClassVar[OrderUpdateReasonEnum]
    ORDER_CANCELED: _ClassVar[OrderUpdateReasonEnum]
    ORDER_CANCEL_REPLACE_COMPLETE: _ClassVar[OrderUpdateReasonEnum]
    NEW_ORDER_REJECTED: _ClassVar[OrderUpdateReasonEnum]
    ORDER_CANCEL_REJECTED: _ClassVar[OrderUpdateReasonEnum]
    ORDER_CANCEL_REPLACE_REJECTED: _ClassVar[OrderUpdateReasonEnum]

class AtBidOrAskEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BID_ASK_UNSET: _ClassVar[AtBidOrAskEnum]
    AT_BID: _ClassVar[AtBidOrAskEnum]
    AT_ASK: _ClassVar[AtBidOrAskEnum]

class AtBidOrAskEnum8(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BID_ASK_UNSET_8: _ClassVar[AtBidOrAskEnum8]
    AT_BID_8: _ClassVar[AtBidOrAskEnum8]
    AT_ASK_8: _ClassVar[AtBidOrAskEnum8]

class MarketDepthUpdateTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPTH_UNSET: _ClassVar[MarketDepthUpdateTypeEnum]
    MARKET_DEPTH_INSERT_UPDATE_LEVEL: _ClassVar[MarketDepthUpdateTypeEnum]
    MARKET_DEPTH_DELETE_LEVEL: _ClassVar[MarketDepthUpdateTypeEnum]

class FinalUpdateInBatchEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINAL_UPDATE_UNSET: _ClassVar[FinalUpdateInBatchEnum]
    FINAL_UPDATE_TRUE: _ClassVar[FinalUpdateInBatchEnum]
    FINAL_UPDATE_FALSE: _ClassVar[FinalUpdateInBatchEnum]
    FINAL_UPDATE_BEGIN_BATCH: _ClassVar[FinalUpdateInBatchEnum]

class OrderTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_TYPE_UNSET: _ClassVar[OrderTypeEnum]
    ORDER_TYPE_MARKET: _ClassVar[OrderTypeEnum]
    ORDER_TYPE_LIMIT: _ClassVar[OrderTypeEnum]
    ORDER_TYPE_STOP: _ClassVar[OrderTypeEnum]
    ORDER_TYPE_STOP_LIMIT: _ClassVar[OrderTypeEnum]
    ORDER_TYPE_MARKET_IF_TOUCHED: _ClassVar[OrderTypeEnum]
    ORDER_TYPE_LIMIT_IF_TOUCHED: _ClassVar[OrderTypeEnum]

class TimeInForceEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIF_UNSET: _ClassVar[TimeInForceEnum]
    TIF_DAY: _ClassVar[TimeInForceEnum]
    TIF_GOOD_TILL_CANCELED: _ClassVar[TimeInForceEnum]
    TIF_GOOD_TILL_DATE_TIME: _ClassVar[TimeInForceEnum]
    TIF_IMMEDIATE_OR_CANCEL: _ClassVar[TimeInForceEnum]
    TIF_ALL_OR_NONE: _ClassVar[TimeInForceEnum]
    TIF_FILL_OR_KILL: _ClassVar[TimeInForceEnum]

class BuySellEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUY_SELL_UNSET: _ClassVar[BuySellEnum]
    BUY: _ClassVar[BuySellEnum]
    SELL: _ClassVar[BuySellEnum]

class OpenCloseTradeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_UNSET: _ClassVar[OpenCloseTradeEnum]
    TRADE_OPEN: _ClassVar[OpenCloseTradeEnum]
    TRADE_CLOSE: _ClassVar[OpenCloseTradeEnum]

class PartialFillHandlingEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTIAL_FILL_UNSET: _ClassVar[PartialFillHandlingEnum]
    PARTIAL_FILL_HANDLING_REDUCE_QUANTITY: _ClassVar[PartialFillHandlingEnum]
    PARTIAL_FILL_HANDLING_IMMEDIATE_CANCEL: _ClassVar[PartialFillHandlingEnum]

class MarketDataFeedStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MARKET_DATA_FEED_STATUS_UNSET: _ClassVar[MarketDataFeedStatusEnum]
    MARKET_DATA_FEED_UNAVAILABLE: _ClassVar[MarketDataFeedStatusEnum]
    MARKET_DATA_FEED_AVAILABLE: _ClassVar[MarketDataFeedStatusEnum]

class PriceDisplayFormatEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRICE_DISPLAY_FORMAT_DECIMAL_0: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_1: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_2: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_3: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_4: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_5: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_6: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_7: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_8: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DECIMAL_9: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_256: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_128: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_64: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_32_QUARTERS: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_32_HALVES: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_32: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_16: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_8: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_4: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_DENOMINATOR_2: _ClassVar[PriceDisplayFormatEnum]
    PRICE_DISPLAY_FORMAT_UNSET: _ClassVar[PriceDisplayFormatEnum]

class SecurityTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_TYPE_UNSET: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_FUTURE: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_STOCK: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_FOREX: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_INDEX: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_FUTURES_STRATEGY: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_FUTURES_OPTION: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_STOCK_OPTION: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_INDEX_OPTION: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_BOND: _ClassVar[SecurityTypeEnum]
    SECURITY_TYPE_MUTUAL_FUND: _ClassVar[SecurityTypeEnum]

class PutCallEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PC_UNSET: _ClassVar[PutCallEnum]
    PC_CALL: _ClassVar[PutCallEnum]
    PC_PUT: _ClassVar[PutCallEnum]

class SearchTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_TYPE_UNSET: _ClassVar[SearchTypeEnum]
    SEARCH_TYPE_BY_SYMBOL: _ClassVar[SearchTypeEnum]
    SEARCH_TYPE_BY_DESCRIPTION: _ClassVar[SearchTypeEnum]

class HistoricalDataIntervalEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERVAL_TICK: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_1_SECOND: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_2_SECONDS: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_4_SECONDS: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_5_SECONDS: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_10_SECONDS: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_30_SECONDS: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_1_MINUTE: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_5_MINUTE: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_10_MINUTE: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_15_MINUTE: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_30_MINUTE: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_1_HOUR: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_2_HOURS: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_1_DAY: _ClassVar[HistoricalDataIntervalEnum]
    INTERVAL_1_WEEK: _ClassVar[HistoricalDataIntervalEnum]

class HistoricalPriceDataRejectReasonCodeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HPDR_UNSET: _ClassVar[HistoricalPriceDataRejectReasonCodeEnum]
    HPDR_UNABLE_TO_SERVE_DATA_RETRY_LATER: _ClassVar[HistoricalPriceDataRejectReasonCodeEnum]
    HPDR_UNABLE_TO_SERVE_DATA_DO_NOT_RETRY: _ClassVar[HistoricalPriceDataRejectReasonCodeEnum]
    HPDR_DATA_REQUEST_OUTSIDE_BOUNDS_OF_AVAILABLE_DATA: _ClassVar[HistoricalPriceDataRejectReasonCodeEnum]
    HPDR_GENERAL_REJECT_ERROR: _ClassVar[HistoricalPriceDataRejectReasonCodeEnum]

class TradingStatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADING_STATUS_UNKNOWN: _ClassVar[TradingStatusEnum]
    TRADING_STATUS_PRE_OPEN: _ClassVar[TradingStatusEnum]
    TRADING_STATUS_OPEN: _ClassVar[TradingStatusEnum]
    TRADING_STATUS_CLOSE: _ClassVar[TradingStatusEnum]
    TRADING_STATUS_TRADING_HALT: _ClassVar[TradingStatusEnum]

class MessageSetBoundaryEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_SET_BOUNDARY_UNSET: _ClassVar[MessageSetBoundaryEnum]
    MESSAGE_SET_BOUNDARY_BEGIN: _ClassVar[MessageSetBoundaryEnum]
    MESSAGE_SET_BOUNDARY_END: _ClassVar[MessageSetBoundaryEnum]

class TradingIsDisabledEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADING_IS_DISABLED_RETURN_CURRENT_VALUE: _ClassVar[TradingIsDisabledEnum]
    TRADING_IS_DISABLED_DISABLE: _ClassVar[TradingIsDisabledEnum]
    TRADING_IS_DISABLED_ENABLE: _ClassVar[TradingIsDisabledEnum]
DTC_VERSION_UNSET: DTCVersion
CURRENT_VERSION: DTCVersion
MESSAGE_TYPE_UNSET: DTCMessageType
LOGON_REQUEST: DTCMessageType
LOGON_RESPONSE: DTCMessageType
HEARTBEAT: DTCMessageType
LOGOFF: DTCMessageType
ENCODING_REQUEST: DTCMessageType
ENCODING_RESPONSE: DTCMessageType
MARKET_DATA_REQUEST: DTCMessageType
MARKET_DATA_REJECT: DTCMessageType
MARKET_DATA_SNAPSHOT: DTCMessageType
MARKET_DATA_UPDATE_TRADE: DTCMessageType
MARKET_DATA_UPDATE_TRADE_COMPACT: DTCMessageType
MARKET_DATA_UPDATE_LAST_TRADE_SNAPSHOT: DTCMessageType
MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR: DTCMessageType
MARKET_DATA_UPDATE_TRADE_WITH_UNBUNDLED_INDICATOR_2: DTCMessageType
MARKET_DATA_UPDATE_TRADE_NO_TIMESTAMP: DTCMessageType
MARKET_DATA_UPDATE_BID_ASK: DTCMessageType
MARKET_DATA_UPDATE_BID_ASK_COMPACT: DTCMessageType
MARKET_DATA_UPDATE_BID_ASK_NO_TIMESTAMP: DTCMessageType
MARKET_DATA_UPDATE_BID_ASK_FLOAT_WITH_MICROSECONDS: DTCMessageType
MARKET_DATA_UPDATE_SESSION_OPEN: DTCMessageType
MARKET_DATA_UPDATE_SESSION_HIGH: DTCMessageType
MARKET_DATA_UPDATE_SESSION_LOW: DTCMessageType
MARKET_DATA_UPDATE_SESSION_VOLUME: DTCMessageType
MARKET_DATA_UPDATE_OPEN_INTEREST: DTCMessageType
MARKET_DATA_UPDATE_SESSION_SETTLEMENT: DTCMessageType
MARKET_DATA_UPDATE_SESSION_NUM_TRADES: DTCMessageType
MARKET_DATA_UPDATE_TRADING_SESSION_DATE: DTCMessageType
MARKET_DEPTH_REQUEST: DTCMessageType
MARKET_DEPTH_REJECT: DTCMessageType
MARKET_DEPTH_SNAPSHOT_LEVEL: DTCMessageType
MARKET_DEPTH_SNAPSHOT_LEVEL_FLOAT: DTCMessageType
MARKET_DEPTH_UPDATE_LEVEL: DTCMessageType
MARKET_DEPTH_UPDATE_LEVEL_FLOAT_WITH_MILLISECONDS: DTCMessageType
MARKET_DEPTH_UPDATE_LEVEL_NO_TIMESTAMP: DTCMessageType
MARKET_DATA_FEED_STATUS: DTCMessageType
MARKET_DATA_FEED_SYMBOL_STATUS: DTCMessageType
TRADING_SYMBOL_STATUS: DTCMessageType
MARKET_ORDERS_REQUEST: DTCMessageType
MARKET_ORDERS_REJECT: DTCMessageType
MARKET_ORDERS_ADD: DTCMessageType
MARKET_ORDERS_MODIFY: DTCMessageType
MARKET_ORDERS_REMOVE: DTCMessageType
MARKET_ORDERS_SNAPSHOT_MESSAGE_BOUNDARY: DTCMessageType
SUBMIT_NEW_SINGLE_ORDER: DTCMessageType
SUBMIT_NEW_OCO_ORDER: DTCMessageType
SUBMIT_FLATTEN_POSITION_ORDER: DTCMessageType
FLATTEN_POSITIONS_FOR_TRADE_ACCOUNT: DTCMessageType
CANCEL_ORDER: DTCMessageType
CANCEL_REPLACE_ORDER: DTCMessageType
OPEN_ORDERS_REQUEST: DTCMessageType
OPEN_ORDERS_REJECT: DTCMessageType
ORDER_UPDATE: DTCMessageType
HISTORICAL_ORDER_FILLS_REQUEST: DTCMessageType
HISTORICAL_ORDER_FILL_RESPONSE: DTCMessageType
HISTORICAL_ORDER_FILLS_REJECT: DTCMessageType
CURRENT_POSITIONS_REQUEST: DTCMessageType
CURRENT_POSITIONS_REJECT: DTCMessageType
POSITION_UPDATE: DTCMessageType
ADD_CORRECTING_ORDER_FILL: DTCMessageType
CORRECTING_ORDER_FILL_RESPONSE: DTCMessageType
TRADE_ACCOUNTS_REQUEST: DTCMessageType
TRADE_ACCOUNT_RESPONSE: DTCMessageType
EXCHANGE_LIST_REQUEST: DTCMessageType
EXCHANGE_LIST_RESPONSE: DTCMessageType
SYMBOLS_FOR_EXCHANGE_REQUEST: DTCMessageType
UNDERLYING_SYMBOLS_FOR_EXCHANGE_REQUEST: DTCMessageType
SYMBOLS_FOR_UNDERLYING_REQUEST: DTCMessageType
SECURITY_DEFINITION_FOR_SYMBOL_REQUEST: DTCMessageType
SECURITY_DEFINITION_RESPONSE: DTCMessageType
SYMBOL_SEARCH_REQUEST: DTCMessageType
SECURITY_DEFINITION_REJECT: DTCMessageType
ACCOUNT_BALANCE_REQUEST: DTCMessageType
ACCOUNT_BALANCE_REJECT: DTCMessageType
ACCOUNT_BALANCE_UPDATE: DTCMessageType
ACCOUNT_BALANCE_ADJUSTMENT: DTCMessageType
ACCOUNT_BALANCE_ADJUSTMENT_REJECT: DTCMessageType
ACCOUNT_BALANCE_ADJUSTMENT_COMPLETE: DTCMessageType
HISTORICAL_ACCOUNT_BALANCES_REQUEST: DTCMessageType
HISTORICAL_ACCOUNT_BALANCES_REJECT: DTCMessageType
HISTORICAL_ACCOUNT_BALANCE_RESPONSE: DTCMessageType
USER_MESSAGE: DTCMessageType
GENERAL_LOG_MESSAGE: DTCMessageType
ALERT_MESSAGE: DTCMessageType
JOURNAL_ENTRY_ADD: DTCMessageType
JOURNAL_ENTRIES_REQUEST: DTCMessageType
JOURNAL_ENTRIES_REJECT: DTCMessageType
JOURNAL_ENTRY_RESPONSE: DTCMessageType
HISTORICAL_PRICE_DATA_REQUEST: DTCMessageType
HISTORICAL_PRICE_DATA_RESPONSE_HEADER: DTCMessageType
HISTORICAL_PRICE_DATA_REJECT: DTCMessageType
HISTORICAL_PRICE_DATA_RECORD_RESPONSE: DTCMessageType
HISTORICAL_PRICE_DATA_TICK_RECORD_RESPONSE: DTCMessageType
HISTORICAL_PRICE_DATA_RESPONSE_TRAILER: DTCMessageType
HISTORICAL_MARKET_DEPTH_DATA_REQUEST: DTCMessageType
HISTORICAL_MARKET_DEPTH_DATA_RESPONSE_HEADER: DTCMessageType
HISTORICAL_MARKET_DEPTH_DATA_REJECT: DTCMessageType
HISTORICAL_MARKET_DEPTH_DATA_RECORD_RESPONSE: DTCMessageType
TRADE_ACCOUNT_TRADING_IS_DISABLED_REQUEST: DTCMessageType
TRADE_ACCOUNT_TRADING_IS_DISABLED_RESPONSE: DTCMessageType
BINARY_ENCODING: EncodingEnum
BINARY_WITH_VARIABLE_LENGTH_STRINGS: EncodingEnum
JSON_ENCODING: EncodingEnum
JSON_COMPACT_ENCODING: EncodingEnum
PROTOCOL_BUFFERS: EncodingEnum
LOGON_STATUS_UNSET: LogonStatusEnum
LOGON_SUCCESS: LogonStatusEnum
LOGON_ERROR: LogonStatusEnum
LOGON_ERROR_NO_RECONNECT: LogonStatusEnum
LOGON_RECONNECT_NEW_ADDRESS: LogonStatusEnum
MESSAGE_UNSUPPORTED: MessageSupportedEnum
MESSAGE_SUPPORTED: MessageSupportedEnum
REQUEST_ACTION_UNSET: RequestActionEnum
SUBSCRIBE: RequestActionEnum
UNSUBSCRIBE: RequestActionEnum
SNAPSHOT: RequestActionEnum
UNBUNDLED_TRADE_NONE: UnbundledTradeIndicatorEnum
FIRST_SUB_TRADE_OF_UNBUNDLED_TRADE: UnbundledTradeIndicatorEnum
LAST_SUB_TRADE_OF_UNBUNDLED_TRADE: UnbundledTradeIndicatorEnum
TRADE_CONDITION_NONE: TradeConditionEnum
TRADE_CONDITION_NON_LAST_UPDATE_EQUITY_TRADE: TradeConditionEnum
TRADE_CONDITION_ODD_LOT_EQUITY_TRADE: TradeConditionEnum
ORDER_STATUS_UNSPECIFIED: OrderStatusEnum
ORDER_STATUS_ORDER_SENT: OrderStatusEnum
ORDER_STATUS_PENDING_OPEN: OrderStatusEnum
ORDER_STATUS_PENDING_CHILD: OrderStatusEnum
ORDER_STATUS_OPEN: OrderStatusEnum
ORDER_STATUS_PENDING_CANCEL_REPLACE: OrderStatusEnum
ORDER_STATUS_PENDING_CANCEL: OrderStatusEnum
ORDER_STATUS_FILLED: OrderStatusEnum
ORDER_STATUS_CANCELED: OrderStatusEnum
ORDER_STATUS_REJECTED: OrderStatusEnum
ORDER_STATUS_PARTIALLY_FILLED: OrderStatusEnum
ORDER_UPDATE_REASON_UNSET: OrderUpdateReasonEnum
OPEN_ORDERS_REQUEST_RESPONSE: OrderUpdateReasonEnum
NEW_ORDER_ACCEPTED: OrderUpdateReasonEnum
GENERAL_ORDER_UPDATE: OrderUpdateReasonEnum
ORDER_FILLED: OrderUpdateReasonEnum
ORDER_FILLED_PARTIALLY: OrderUpdateReasonEnum
ORDER_CANCELED: OrderUpdateReasonEnum
ORDER_CANCEL_REPLACE_COMPLETE: OrderUpdateReasonEnum
NEW_ORDER_REJECTED: OrderUpdateReasonEnum
ORDER_CANCEL_REJECTED: OrderUpdateReasonEnum
ORDER_CANCEL_REPLACE_REJECTED: OrderUpdateReasonEnum
BID_ASK_UNSET: AtBidOrAskEnum
AT_BID: AtBidOrAskEnum
AT_ASK: AtBidOrAskEnum
BID_ASK_UNSET_8: AtBidOrAskEnum8
AT_BID_8: AtBidOrAskEnum8
AT_ASK_8: AtBidOrAskEnum8
DEPTH_UNSET: MarketDepthUpdateTypeEnum
MARKET_DEPTH_INSERT_UPDATE_LEVEL: MarketDepthUpdateTypeEnum
MARKET_DEPTH_DELETE_LEVEL: MarketDepthUpdateTypeEnum
FINAL_UPDATE_UNSET: FinalUpdateInBatchEnum
FINAL_UPDATE_TRUE: FinalUpdateInBatchEnum
FINAL_UPDATE_FALSE: FinalUpdateInBatchEnum
FINAL_UPDATE_BEGIN_BATCH: FinalUpdateInBatchEnum
ORDER_TYPE_UNSET: OrderTypeEnum
ORDER_TYPE_MARKET: OrderTypeEnum
ORDER_TYPE_LIMIT: OrderTypeEnum
ORDER_TYPE_STOP: OrderTypeEnum
ORDER_TYPE_STOP_LIMIT: OrderTypeEnum
ORDER_TYPE_MARKET_IF_TOUCHED: OrderTypeEnum
ORDER_TYPE_LIMIT_IF_TOUCHED: OrderTypeEnum
TIF_UNSET: TimeInForceEnum
TIF_DAY: TimeInForceEnum
TIF_GOOD_TILL_CANCELED: TimeInForceEnum
TIF_GOOD_TILL_DATE_TIME: TimeInForceEnum
TIF_IMMEDIATE_OR_CANCEL: TimeInForceEnum
TIF_ALL_OR_NONE: TimeInForceEnum
TIF_FILL_OR_KILL: TimeInForceEnum
BUY_SELL_UNSET: BuySellEnum
BUY: BuySellEnum
SELL: BuySellEnum
TRADE_UNSET: OpenCloseTradeEnum
TRADE_OPEN: OpenCloseTradeEnum
TRADE_CLOSE: OpenCloseTradeEnum
PARTIAL_FILL_UNSET: PartialFillHandlingEnum
PARTIAL_FILL_HANDLING_REDUCE_QUANTITY: PartialFillHandlingEnum
PARTIAL_FILL_HANDLING_IMMEDIATE_CANCEL: PartialFillHandlingEnum
MARKET_DATA_FEED_STATUS_UNSET: MarketDataFeedStatusEnum
MARKET_DATA_FEED_UNAVAILABLE: MarketDataFeedStatusEnum
MARKET_DATA_FEED_AVAILABLE: MarketDataFeedStatusEnum
PRICE_DISPLAY_FORMAT_DECIMAL_0: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_1: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_2: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_3: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_4: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_5: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_6: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_7: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_8: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DECIMAL_9: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_256: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_128: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_64: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_32_QUARTERS: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_32_HALVES: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_32: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_16: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_8: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_4: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_DENOMINATOR_2: PriceDisplayFormatEnum
PRICE_DISPLAY_FORMAT_UNSET: PriceDisplayFormatEnum
SECURITY_TYPE_UNSET: SecurityTypeEnum
SECURITY_TYPE_FUTURE: SecurityTypeEnum
SECURITY_TYPE_STOCK: SecurityTypeEnum
SECURITY_TYPE_FOREX: SecurityTypeEnum
SECURITY_TYPE_INDEX: SecurityTypeEnum
SECURITY_TYPE_FUTURES_STRATEGY: SecurityTypeEnum
SECURITY_TYPE_FUTURES_OPTION: SecurityTypeEnum
SECURITY_TYPE_STOCK_OPTION: SecurityTypeEnum
SECURITY_TYPE_INDEX_OPTION: SecurityTypeEnum
SECURITY_TYPE_BOND: SecurityTypeEnum
SECURITY_TYPE_MUTUAL_FUND: SecurityTypeEnum
PC_UNSET: PutCallEnum
PC_CALL: PutCallEnum
PC_PUT: PutCallEnum
SEARCH_TYPE_UNSET: SearchTypeEnum
SEARCH_TYPE_BY_SYMBOL: SearchTypeEnum
SEARCH_TYPE_BY_DESCRIPTION: SearchTypeEnum
INTERVAL_TICK: HistoricalDataIntervalEnum
INTERVAL_1_SECOND: HistoricalDataIntervalEnum
INTERVAL_2_SECONDS: HistoricalDataIntervalEnum
INTERVAL_4_SECONDS: HistoricalDataIntervalEnum
INTERVAL_5_SECONDS: HistoricalDataIntervalEnum
INTERVAL_10_SECONDS: HistoricalDataIntervalEnum
INTERVAL_30_SECONDS: HistoricalDataIntervalEnum
INTERVAL_1_MINUTE: HistoricalDataIntervalEnum
INTERVAL_5_MINUTE: HistoricalDataIntervalEnum
INTERVAL_10_MINUTE: HistoricalDataIntervalEnum
INTERVAL_15_MINUTE: HistoricalDataIntervalEnum
INTERVAL_30_MINUTE: HistoricalDataIntervalEnum
INTERVAL_1_HOUR: HistoricalDataIntervalEnum
INTERVAL_2_HOURS: HistoricalDataIntervalEnum
INTERVAL_1_DAY: HistoricalDataIntervalEnum
INTERVAL_1_WEEK: HistoricalDataIntervalEnum
HPDR_UNSET: HistoricalPriceDataRejectReasonCodeEnum
HPDR_UNABLE_TO_SERVE_DATA_RETRY_LATER: HistoricalPriceDataRejectReasonCodeEnum
HPDR_UNABLE_TO_SERVE_DATA_DO_NOT_RETRY: HistoricalPriceDataRejectReasonCodeEnum
HPDR_DATA_REQUEST_OUTSIDE_BOUNDS_OF_AVAILABLE_DATA: HistoricalPriceDataRejectReasonCodeEnum
HPDR_GENERAL_REJECT_ERROR: HistoricalPriceDataRejectReasonCodeEnum
TRADING_STATUS_UNKNOWN: TradingStatusEnum
TRADING_STATUS_PRE_OPEN: TradingStatusEnum
TRADING_STATUS_OPEN: TradingStatusEnum
TRADING_STATUS_CLOSE: TradingStatusEnum
TRADING_STATUS_TRADING_HALT: TradingStatusEnum
MESSAGE_SET_BOUNDARY_UNSET: MessageSetBoundaryEnum
MESSAGE_SET_BOUNDARY_BEGIN: MessageSetBoundaryEnum
MESSAGE_SET_BOUNDARY_END: MessageSetBoundaryEnum
TRADING_IS_DISABLED_RETURN_CURRENT_VALUE: TradingIsDisabledEnum
TRADING_IS_DISABLED_DISABLE: TradingIsDisabledEnum
TRADING_IS_DISABLED_ENABLE: TradingIsDisabledEnum

class EncodingRequest(_message.Message):
    __slots__ = ("ProtocolVersion", "Encoding", "ProtocolType")
    PROTOCOLVERSION_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLTYPE_FIELD_NUMBER: _ClassVar[int]
    ProtocolVersion: int
    Encoding: EncodingEnum
    ProtocolType: str
    def __init__(self, ProtocolVersion: _Optional[int] = ..., Encoding: _Optional[_Union[EncodingEnum, str]] = ..., ProtocolType: _Optional[str] = ...) -> None: ...

class EncodingResponse(_message.Message):
    __slots__ = ("ProtocolVersion", "Encoding", "ProtocolType")
    PROTOCOLVERSION_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLTYPE_FIELD_NUMBER: _ClassVar[int]
    ProtocolVersion: int
    Encoding: EncodingEnum
    ProtocolType: str
    def __init__(self, ProtocolVersion: _Optional[int] = ..., Encoding: _Optional[_Union[EncodingEnum, str]] = ..., ProtocolType: _Optional[str] = ...) -> None: ...

class LogonRequest(_message.Message):
    __slots__ = ("ProtocolVersion", "Username", "Password", "GeneralTextData", "Integer_1", "Integer_2", "HeartbeatIntervalInSeconds", "Unused1", "TradeAccount", "HardwareIdentifier", "ClientName", "MarketDataTransmissionInterval")
    PROTOCOLVERSION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    GENERALTEXTDATA_FIELD_NUMBER: _ClassVar[int]
    INTEGER_1_FIELD_NUMBER: _ClassVar[int]
    INTEGER_2_FIELD_NUMBER: _ClassVar[int]
    HEARTBEATINTERVALINSECONDS_FIELD_NUMBER: _ClassVar[int]
    UNUSED1_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    HARDWAREIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CLIENTNAME_FIELD_NUMBER: _ClassVar[int]
    MARKETDATATRANSMISSIONINTERVAL_FIELD_NUMBER: _ClassVar[int]
    ProtocolVersion: int
    Username: str
    Password: str
    GeneralTextData: str
    Integer_1: int
    Integer_2: int
    HeartbeatIntervalInSeconds: int
    Unused1: int
    TradeAccount: str
    HardwareIdentifier: str
    ClientName: str
    MarketDataTransmissionInterval: int
    def __init__(self, ProtocolVersion: _Optional[int] = ..., Username: _Optional[str] = ..., Password: _Optional[str] = ..., GeneralTextData: _Optional[str] = ..., Integer_1: _Optional[int] = ..., Integer_2: _Optional[int] = ..., HeartbeatIntervalInSeconds: _Optional[int] = ..., Unused1: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., HardwareIdentifier: _Optional[str] = ..., ClientName: _Optional[str] = ..., MarketDataTransmissionInterval: _Optional[int] = ...) -> None: ...

class LogonResponse(_message.Message):
    __slots__ = ("ProtocolVersion", "Result", "ResultText", "ReconnectAddress", "Integer_1", "ServerName", "MarketDepthUpdatesBestBidAndAsk", "TradingIsSupported", "OCOOrdersSupported", "OrderCancelReplaceSupported", "SymbolExchangeDelimiter", "SecurityDefinitionsSupported", "HistoricalPriceDataSupported", "ResubscribeWhenMarketDataFeedAvailable", "MarketDepthIsSupported", "OneHistoricalPriceDataRequestPerConnection", "BracketOrdersSupported", "Unused_1", "UsesMultiplePositionsPerSymbolAndTradeAccount", "MarketDataSupported")
    PROTOCOLVERSION_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULTTEXT_FIELD_NUMBER: _ClassVar[int]
    RECONNECTADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTEGER_1_FIELD_NUMBER: _ClassVar[int]
    SERVERNAME_FIELD_NUMBER: _ClassVar[int]
    MARKETDEPTHUPDATESBESTBIDANDASK_FIELD_NUMBER: _ClassVar[int]
    TRADINGISSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    OCOORDERSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ORDERCANCELREPLACESUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SYMBOLEXCHANGEDELIMITER_FIELD_NUMBER: _ClassVar[int]
    SECURITYDEFINITIONSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HISTORICALPRICEDATASUPPORTED_FIELD_NUMBER: _ClassVar[int]
    RESUBSCRIBEWHENMARKETDATAFEEDAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MARKETDEPTHISSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ONEHISTORICALPRICEDATAREQUESTPERCONNECTION_FIELD_NUMBER: _ClassVar[int]
    BRACKETORDERSSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    UNUSED_1_FIELD_NUMBER: _ClassVar[int]
    USESMULTIPLEPOSITIONSPERSYMBOLANDTRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MARKETDATASUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ProtocolVersion: int
    Result: LogonStatusEnum
    ResultText: str
    ReconnectAddress: str
    Integer_1: int
    ServerName: str
    MarketDepthUpdatesBestBidAndAsk: int
    TradingIsSupported: int
    OCOOrdersSupported: int
    OrderCancelReplaceSupported: int
    SymbolExchangeDelimiter: str
    SecurityDefinitionsSupported: int
    HistoricalPriceDataSupported: int
    ResubscribeWhenMarketDataFeedAvailable: int
    MarketDepthIsSupported: int
    OneHistoricalPriceDataRequestPerConnection: int
    BracketOrdersSupported: int
    Unused_1: int
    UsesMultiplePositionsPerSymbolAndTradeAccount: int
    MarketDataSupported: int
    def __init__(self, ProtocolVersion: _Optional[int] = ..., Result: _Optional[_Union[LogonStatusEnum, str]] = ..., ResultText: _Optional[str] = ..., ReconnectAddress: _Optional[str] = ..., Integer_1: _Optional[int] = ..., ServerName: _Optional[str] = ..., MarketDepthUpdatesBestBidAndAsk: _Optional[int] = ..., TradingIsSupported: _Optional[int] = ..., OCOOrdersSupported: _Optional[int] = ..., OrderCancelReplaceSupported: _Optional[int] = ..., SymbolExchangeDelimiter: _Optional[str] = ..., SecurityDefinitionsSupported: _Optional[int] = ..., HistoricalPriceDataSupported: _Optional[int] = ..., ResubscribeWhenMarketDataFeedAvailable: _Optional[int] = ..., MarketDepthIsSupported: _Optional[int] = ..., OneHistoricalPriceDataRequestPerConnection: _Optional[int] = ..., BracketOrdersSupported: _Optional[int] = ..., Unused_1: _Optional[int] = ..., UsesMultiplePositionsPerSymbolAndTradeAccount: _Optional[int] = ..., MarketDataSupported: _Optional[int] = ...) -> None: ...

class Logoff(_message.Message):
    __slots__ = ("Reason", "DoNotReconnect")
    REASON_FIELD_NUMBER: _ClassVar[int]
    DONOTRECONNECT_FIELD_NUMBER: _ClassVar[int]
    Reason: str
    DoNotReconnect: int
    def __init__(self, Reason: _Optional[str] = ..., DoNotReconnect: _Optional[int] = ...) -> None: ...

class Heartbeat(_message.Message):
    __slots__ = ("NumDroppedMessages", "CurrentDateTime")
    NUMDROPPEDMESSAGES_FIELD_NUMBER: _ClassVar[int]
    CURRENTDATETIME_FIELD_NUMBER: _ClassVar[int]
    NumDroppedMessages: int
    CurrentDateTime: int
    def __init__(self, NumDroppedMessages: _Optional[int] = ..., CurrentDateTime: _Optional[int] = ...) -> None: ...

class MarketDataFeedStatus(_message.Message):
    __slots__ = ("Status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Status: MarketDataFeedStatusEnum
    def __init__(self, Status: _Optional[_Union[MarketDataFeedStatusEnum, str]] = ...) -> None: ...

class MarketDataFeedSymbolStatus(_message.Message):
    __slots__ = ("SymbolID", "Status")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Status: MarketDataFeedStatusEnum
    def __init__(self, SymbolID: _Optional[int] = ..., Status: _Optional[_Union[MarketDataFeedStatusEnum, str]] = ...) -> None: ...

class TradingSymbolStatus(_message.Message):
    __slots__ = ("SymbolID", "Status")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Status: TradingStatusEnum
    def __init__(self, SymbolID: _Optional[int] = ..., Status: _Optional[_Union[TradingStatusEnum, str]] = ...) -> None: ...

class MarketDataRequest(_message.Message):
    __slots__ = ("RequestAction", "SymbolID", "Symbol", "Exchange", "IntervalForSnapshotUpdatesInMilliseconds")
    REQUESTACTION_FIELD_NUMBER: _ClassVar[int]
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    INTERVALFORSNAPSHOTUPDATESINMILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    RequestAction: RequestActionEnum
    SymbolID: int
    Symbol: str
    Exchange: str
    IntervalForSnapshotUpdatesInMilliseconds: int
    def __init__(self, RequestAction: _Optional[_Union[RequestActionEnum, str]] = ..., SymbolID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., IntervalForSnapshotUpdatesInMilliseconds: _Optional[int] = ...) -> None: ...

class MarketDepthRequest(_message.Message):
    __slots__ = ("RequestAction", "SymbolID", "Symbol", "Exchange", "NumLevels")
    REQUESTACTION_FIELD_NUMBER: _ClassVar[int]
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    NUMLEVELS_FIELD_NUMBER: _ClassVar[int]
    RequestAction: RequestActionEnum
    SymbolID: int
    Symbol: str
    Exchange: str
    NumLevels: int
    def __init__(self, RequestAction: _Optional[_Union[RequestActionEnum, str]] = ..., SymbolID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., NumLevels: _Optional[int] = ...) -> None: ...

class MarketDataReject(_message.Message):
    __slots__ = ("SymbolID", "RejectText")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    RejectText: str
    def __init__(self, SymbolID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class MarketDataSnapshot(_message.Message):
    __slots__ = ("SymbolID", "SessionSettlementPrice", "SessionOpenPrice", "SessionHighPrice", "SessionLowPrice", "SessionVolume", "SessionNumTrades", "OpenInterest", "BidPrice", "AskPrice", "AskQuantity", "BidQuantity", "LastTradePrice", "LastTradeVolume", "LastTradeDateTime", "BidAskDateTime", "SessionSettlementDateTime", "TradingSessionDate", "TradingStatus", "MarketDepthUpdateDateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SESSIONSETTLEMENTPRICE_FIELD_NUMBER: _ClassVar[int]
    SESSIONOPENPRICE_FIELD_NUMBER: _ClassVar[int]
    SESSIONHIGHPRICE_FIELD_NUMBER: _ClassVar[int]
    SESSIONLOWPRICE_FIELD_NUMBER: _ClassVar[int]
    SESSIONVOLUME_FIELD_NUMBER: _ClassVar[int]
    SESSIONNUMTRADES_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    LASTTRADEPRICE_FIELD_NUMBER: _ClassVar[int]
    LASTTRADEVOLUME_FIELD_NUMBER: _ClassVar[int]
    LASTTRADEDATETIME_FIELD_NUMBER: _ClassVar[int]
    BIDASKDATETIME_FIELD_NUMBER: _ClassVar[int]
    SESSIONSETTLEMENTDATETIME_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    TRADINGSTATUS_FIELD_NUMBER: _ClassVar[int]
    MARKETDEPTHUPDATEDATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    SessionSettlementPrice: float
    SessionOpenPrice: float
    SessionHighPrice: float
    SessionLowPrice: float
    SessionVolume: float
    SessionNumTrades: int
    OpenInterest: int
    BidPrice: float
    AskPrice: float
    AskQuantity: float
    BidQuantity: float
    LastTradePrice: float
    LastTradeVolume: float
    LastTradeDateTime: float
    BidAskDateTime: float
    SessionSettlementDateTime: int
    TradingSessionDate: int
    TradingStatus: TradingStatusEnum
    MarketDepthUpdateDateTime: float
    def __init__(self, SymbolID: _Optional[int] = ..., SessionSettlementPrice: _Optional[float] = ..., SessionOpenPrice: _Optional[float] = ..., SessionHighPrice: _Optional[float] = ..., SessionLowPrice: _Optional[float] = ..., SessionVolume: _Optional[float] = ..., SessionNumTrades: _Optional[int] = ..., OpenInterest: _Optional[int] = ..., BidPrice: _Optional[float] = ..., AskPrice: _Optional[float] = ..., AskQuantity: _Optional[float] = ..., BidQuantity: _Optional[float] = ..., LastTradePrice: _Optional[float] = ..., LastTradeVolume: _Optional[float] = ..., LastTradeDateTime: _Optional[float] = ..., BidAskDateTime: _Optional[float] = ..., SessionSettlementDateTime: _Optional[int] = ..., TradingSessionDate: _Optional[int] = ..., TradingStatus: _Optional[_Union[TradingStatusEnum, str]] = ..., MarketDepthUpdateDateTime: _Optional[float] = ...) -> None: ...

class MarketDepthSnapshotLevel(_message.Message):
    __slots__ = ("SymbolID", "Side", "Price", "Quantity", "Level", "IsFirstMessageInBatch", "IsLastMessageInBatch", "DateTime", "NumOrders")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    ISFIRSTMESSAGEINBATCH_FIELD_NUMBER: _ClassVar[int]
    ISLASTMESSAGEINBATCH_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    NUMORDERS_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Side: AtBidOrAskEnum
    Price: float
    Quantity: float
    Level: int
    IsFirstMessageInBatch: int
    IsLastMessageInBatch: int
    DateTime: float
    NumOrders: int
    def __init__(self, SymbolID: _Optional[int] = ..., Side: _Optional[_Union[AtBidOrAskEnum, str]] = ..., Price: _Optional[float] = ..., Quantity: _Optional[float] = ..., Level: _Optional[int] = ..., IsFirstMessageInBatch: _Optional[int] = ..., IsLastMessageInBatch: _Optional[int] = ..., DateTime: _Optional[float] = ..., NumOrders: _Optional[int] = ...) -> None: ...

class MarketDepthSnapshotLevelFloat(_message.Message):
    __slots__ = ("SymbolID", "Price", "Quantity", "NumOrders", "Level", "Side", "FinalUpdateInBatch")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    NUMORDERS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    FINALUPDATEINBATCH_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    Quantity: float
    NumOrders: int
    Level: int
    Side: AtBidOrAskEnum8
    FinalUpdateInBatch: FinalUpdateInBatchEnum
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., Quantity: _Optional[float] = ..., NumOrders: _Optional[int] = ..., Level: _Optional[int] = ..., Side: _Optional[_Union[AtBidOrAskEnum8, str]] = ..., FinalUpdateInBatch: _Optional[_Union[FinalUpdateInBatchEnum, str]] = ...) -> None: ...

class MarketDepthUpdateLevel(_message.Message):
    __slots__ = ("SymbolID", "Side", "Price", "Quantity", "UpdateType", "DateTime", "NumOrders", "FinalUpdateInBatch", "Level")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UPDATETYPE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    NUMORDERS_FIELD_NUMBER: _ClassVar[int]
    FINALUPDATEINBATCH_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Side: AtBidOrAskEnum
    Price: float
    Quantity: float
    UpdateType: MarketDepthUpdateTypeEnum
    DateTime: float
    NumOrders: int
    FinalUpdateInBatch: FinalUpdateInBatchEnum
    Level: int
    def __init__(self, SymbolID: _Optional[int] = ..., Side: _Optional[_Union[AtBidOrAskEnum, str]] = ..., Price: _Optional[float] = ..., Quantity: _Optional[float] = ..., UpdateType: _Optional[_Union[MarketDepthUpdateTypeEnum, str]] = ..., DateTime: _Optional[float] = ..., NumOrders: _Optional[int] = ..., FinalUpdateInBatch: _Optional[_Union[FinalUpdateInBatchEnum, str]] = ..., Level: _Optional[int] = ...) -> None: ...

class MarketDepthUpdateLevelFloatWithMilliseconds(_message.Message):
    __slots__ = ("SymbolID", "DateTime", "Price", "Quantity", "Side", "UpdateType", "NumOrders", "FinalUpdateInBatch", "Level")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UPDATETYPE_FIELD_NUMBER: _ClassVar[int]
    NUMORDERS_FIELD_NUMBER: _ClassVar[int]
    FINALUPDATEINBATCH_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    DateTime: int
    Price: float
    Quantity: float
    Side: int
    UpdateType: int
    NumOrders: int
    FinalUpdateInBatch: FinalUpdateInBatchEnum
    Level: int
    def __init__(self, SymbolID: _Optional[int] = ..., DateTime: _Optional[int] = ..., Price: _Optional[float] = ..., Quantity: _Optional[float] = ..., Side: _Optional[int] = ..., UpdateType: _Optional[int] = ..., NumOrders: _Optional[int] = ..., FinalUpdateInBatch: _Optional[_Union[FinalUpdateInBatchEnum, str]] = ..., Level: _Optional[int] = ...) -> None: ...

class MarketDepthUpdateLevelNoTimestamp(_message.Message):
    __slots__ = ("SymbolID", "Price", "Quantity", "NumOrders", "Side", "UpdateType", "FinalUpdateInBatch", "Level")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    NUMORDERS_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UPDATETYPE_FIELD_NUMBER: _ClassVar[int]
    FINALUPDATEINBATCH_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    Quantity: float
    NumOrders: int
    Side: int
    UpdateType: int
    FinalUpdateInBatch: FinalUpdateInBatchEnum
    Level: int
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., Quantity: _Optional[float] = ..., NumOrders: _Optional[int] = ..., Side: _Optional[int] = ..., UpdateType: _Optional[int] = ..., FinalUpdateInBatch: _Optional[_Union[FinalUpdateInBatchEnum, str]] = ..., Level: _Optional[int] = ...) -> None: ...

class MarketDataUpdateSessionSettlement(_message.Message):
    __slots__ = ("SymbolID", "Price", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    DateTime: int
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., DateTime: _Optional[int] = ...) -> None: ...

class MarketDataUpdateSessionOpen(_message.Message):
    __slots__ = ("SymbolID", "Price", "TradingSessionDate")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    TradingSessionDate: int
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., TradingSessionDate: _Optional[int] = ...) -> None: ...

class MarketDataUpdateSessionNumTrades(_message.Message):
    __slots__ = ("SymbolID", "NumTrades", "TradingSessionDate")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    NUMTRADES_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    NumTrades: int
    TradingSessionDate: int
    def __init__(self, SymbolID: _Optional[int] = ..., NumTrades: _Optional[int] = ..., TradingSessionDate: _Optional[int] = ...) -> None: ...

class MarketDataUpdateTradingSessionDate(_message.Message):
    __slots__ = ("SymbolID", "Date")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Date: int
    def __init__(self, SymbolID: _Optional[int] = ..., Date: _Optional[int] = ...) -> None: ...

class MarketDepthReject(_message.Message):
    __slots__ = ("SymbolID", "RejectText")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    RejectText: str
    def __init__(self, SymbolID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class MarketDataUpdateTrade(_message.Message):
    __slots__ = ("SymbolID", "AtBidOrAsk", "Price", "Volume", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    ATBIDORASK_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    AtBidOrAsk: AtBidOrAskEnum
    Price: float
    Volume: float
    DateTime: float
    def __init__(self, SymbolID: _Optional[int] = ..., AtBidOrAsk: _Optional[_Union[AtBidOrAskEnum, str]] = ..., Price: _Optional[float] = ..., Volume: _Optional[float] = ..., DateTime: _Optional[float] = ...) -> None: ...

class MarketDataUpdateTradeCompact(_message.Message):
    __slots__ = ("Price", "Volume", "DateTime", "SymbolID", "AtBidOrAsk")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    ATBIDORASK_FIELD_NUMBER: _ClassVar[int]
    Price: float
    Volume: float
    DateTime: int
    SymbolID: int
    AtBidOrAsk: AtBidOrAskEnum
    def __init__(self, Price: _Optional[float] = ..., Volume: _Optional[float] = ..., DateTime: _Optional[int] = ..., SymbolID: _Optional[int] = ..., AtBidOrAsk: _Optional[_Union[AtBidOrAskEnum, str]] = ...) -> None: ...

class MarketDataUpdateLastTradeSnapshot(_message.Message):
    __slots__ = ("SymbolID", "LastTradePrice", "LastTradeVolume", "LastTradeDateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    LASTTRADEPRICE_FIELD_NUMBER: _ClassVar[int]
    LASTTRADEVOLUME_FIELD_NUMBER: _ClassVar[int]
    LASTTRADEDATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    LastTradePrice: float
    LastTradeVolume: float
    LastTradeDateTime: float
    def __init__(self, SymbolID: _Optional[int] = ..., LastTradePrice: _Optional[float] = ..., LastTradeVolume: _Optional[float] = ..., LastTradeDateTime: _Optional[float] = ...) -> None: ...

class MarketDataUpdateTradeWithUnbundledIndicator(_message.Message):
    __slots__ = ("SymbolID", "AtBidOrAsk", "UnbundledTradeIndicator", "Price", "Volume", "DateTime", "TradeCondition")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    ATBIDORASK_FIELD_NUMBER: _ClassVar[int]
    UNBUNDLEDTRADEINDICATOR_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    TRADECONDITION_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    AtBidOrAsk: AtBidOrAskEnum8
    UnbundledTradeIndicator: UnbundledTradeIndicatorEnum
    Price: float
    Volume: int
    DateTime: float
    TradeCondition: TradeConditionEnum
    def __init__(self, SymbolID: _Optional[int] = ..., AtBidOrAsk: _Optional[_Union[AtBidOrAskEnum8, str]] = ..., UnbundledTradeIndicator: _Optional[_Union[UnbundledTradeIndicatorEnum, str]] = ..., Price: _Optional[float] = ..., Volume: _Optional[int] = ..., DateTime: _Optional[float] = ..., TradeCondition: _Optional[_Union[TradeConditionEnum, str]] = ...) -> None: ...

class MarketDataUpdateTradeWithUnbundledIndicator2(_message.Message):
    __slots__ = ("SymbolID", "Price", "Volume", "DateTime", "AtBidOrAsk", "UnbundledTradeIndicator", "TradeCondition")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    ATBIDORASK_FIELD_NUMBER: _ClassVar[int]
    UNBUNDLEDTRADEINDICATOR_FIELD_NUMBER: _ClassVar[int]
    TRADECONDITION_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    Volume: int
    DateTime: int
    AtBidOrAsk: AtBidOrAskEnum8
    UnbundledTradeIndicator: UnbundledTradeIndicatorEnum
    TradeCondition: TradeConditionEnum
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., Volume: _Optional[int] = ..., DateTime: _Optional[int] = ..., AtBidOrAsk: _Optional[_Union[AtBidOrAskEnum8, str]] = ..., UnbundledTradeIndicator: _Optional[_Union[UnbundledTradeIndicatorEnum, str]] = ..., TradeCondition: _Optional[_Union[TradeConditionEnum, str]] = ...) -> None: ...

class MarketDataUpdateTradeNoTimestamp(_message.Message):
    __slots__ = ("SymbolID", "Price", "Volume", "AtBidOrAsk", "UnbundledTradeIndicator", "TradeCondition")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    ATBIDORASK_FIELD_NUMBER: _ClassVar[int]
    UNBUNDLEDTRADEINDICATOR_FIELD_NUMBER: _ClassVar[int]
    TRADECONDITION_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    Volume: int
    AtBidOrAsk: AtBidOrAskEnum8
    UnbundledTradeIndicator: UnbundledTradeIndicatorEnum
    TradeCondition: TradeConditionEnum
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., Volume: _Optional[int] = ..., AtBidOrAsk: _Optional[_Union[AtBidOrAskEnum8, str]] = ..., UnbundledTradeIndicator: _Optional[_Union[UnbundledTradeIndicatorEnum, str]] = ..., TradeCondition: _Optional[_Union[TradeConditionEnum, str]] = ...) -> None: ...

class MarketDataUpdateBidAsk(_message.Message):
    __slots__ = ("SymbolID", "BidPrice", "BidQuantity", "AskPrice", "AskQuantity", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ASKPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    BidPrice: float
    BidQuantity: float
    AskPrice: float
    AskQuantity: float
    DateTime: int
    def __init__(self, SymbolID: _Optional[int] = ..., BidPrice: _Optional[float] = ..., BidQuantity: _Optional[float] = ..., AskPrice: _Optional[float] = ..., AskQuantity: _Optional[float] = ..., DateTime: _Optional[int] = ...) -> None: ...

class MarketDataUpdateBidAsk2(_message.Message):
    __slots__ = ("SymbolID", "BidPrice", "BidQuantity", "AskPrice", "AskQuantity", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ASKPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    BidPrice: float
    BidQuantity: float
    AskPrice: float
    AskQuantity: float
    DateTime: int
    def __init__(self, SymbolID: _Optional[int] = ..., BidPrice: _Optional[float] = ..., BidQuantity: _Optional[float] = ..., AskPrice: _Optional[float] = ..., AskQuantity: _Optional[float] = ..., DateTime: _Optional[int] = ...) -> None: ...

class MarketDataUpdateBidAskCompact(_message.Message):
    __slots__ = ("BidPrice", "BidQuantity", "AskPrice", "AskQuantity", "DateTime", "SymbolID")
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ASKPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    BidPrice: float
    BidQuantity: float
    AskPrice: float
    AskQuantity: float
    DateTime: int
    SymbolID: int
    def __init__(self, BidPrice: _Optional[float] = ..., BidQuantity: _Optional[float] = ..., AskPrice: _Optional[float] = ..., AskQuantity: _Optional[float] = ..., DateTime: _Optional[int] = ..., SymbolID: _Optional[int] = ...) -> None: ...

class MarketDataUpdateBidAskNoTimeStamp(_message.Message):
    __slots__ = ("SymbolID", "BidPrice", "BidQuantity", "AskPrice", "AskQuantity")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ASKPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    BidPrice: float
    BidQuantity: int
    AskPrice: float
    AskQuantity: int
    def __init__(self, SymbolID: _Optional[int] = ..., BidPrice: _Optional[float] = ..., BidQuantity: _Optional[int] = ..., AskPrice: _Optional[float] = ..., AskQuantity: _Optional[int] = ...) -> None: ...

class MarketDataUpdateBidAskFloatWithMicroseconds(_message.Message):
    __slots__ = ("SymbolID", "BidPrice", "BidQuantity", "AskPrice", "AskQuantity", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    BIDPRICE_FIELD_NUMBER: _ClassVar[int]
    BIDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ASKPRICE_FIELD_NUMBER: _ClassVar[int]
    ASKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    BidPrice: float
    BidQuantity: float
    AskPrice: float
    AskQuantity: float
    DateTime: int
    def __init__(self, SymbolID: _Optional[int] = ..., BidPrice: _Optional[float] = ..., BidQuantity: _Optional[float] = ..., AskPrice: _Optional[float] = ..., AskQuantity: _Optional[float] = ..., DateTime: _Optional[int] = ...) -> None: ...

class MarketDataUpdateSessionVolume(_message.Message):
    __slots__ = ("SymbolID", "Volume", "TradingSessionDate", "IsFinalSessionVolume")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    ISFINALSESSIONVOLUME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Volume: float
    TradingSessionDate: int
    IsFinalSessionVolume: int
    def __init__(self, SymbolID: _Optional[int] = ..., Volume: _Optional[float] = ..., TradingSessionDate: _Optional[int] = ..., IsFinalSessionVolume: _Optional[int] = ...) -> None: ...

class MarketDataUpdateOpenInterest(_message.Message):
    __slots__ = ("SymbolID", "OpenInterest", "TradingSessionDate")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    OpenInterest: int
    TradingSessionDate: int
    def __init__(self, SymbolID: _Optional[int] = ..., OpenInterest: _Optional[int] = ..., TradingSessionDate: _Optional[int] = ...) -> None: ...

class MarketDataUpdateSessionHigh(_message.Message):
    __slots__ = ("SymbolID", "Price", "TradingSessionDate")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    TradingSessionDate: int
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., TradingSessionDate: _Optional[int] = ...) -> None: ...

class MarketDataUpdateSessionLow(_message.Message):
    __slots__ = ("SymbolID", "Price", "TradingSessionDate")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TRADINGSESSIONDATE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    TradingSessionDate: int
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., TradingSessionDate: _Optional[int] = ...) -> None: ...

class MarketOrdersRequest(_message.Message):
    __slots__ = ("RequestAction", "SymbolID", "Symbol", "Exchange", "SendQuantitiesGreaterOrEqualTo")
    REQUESTACTION_FIELD_NUMBER: _ClassVar[int]
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SENDQUANTITIESGREATEROREQUALTO_FIELD_NUMBER: _ClassVar[int]
    RequestAction: RequestActionEnum
    SymbolID: int
    Symbol: str
    Exchange: str
    SendQuantitiesGreaterOrEqualTo: int
    def __init__(self, RequestAction: _Optional[_Union[RequestActionEnum, str]] = ..., SymbolID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., SendQuantitiesGreaterOrEqualTo: _Optional[int] = ...) -> None: ...

class MarketOrdersReject(_message.Message):
    __slots__ = ("SymbolID", "RejectText")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    RejectText: str
    def __init__(self, SymbolID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class MarketOrdersAdd(_message.Message):
    __slots__ = ("SymbolID", "Side", "Price", "Quantity", "OrderID", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Side: BuySellEnum
    Price: float
    Quantity: int
    OrderID: int
    DateTime: int
    def __init__(self, SymbolID: _Optional[int] = ..., Side: _Optional[_Union[BuySellEnum, str]] = ..., Price: _Optional[float] = ..., Quantity: _Optional[int] = ..., OrderID: _Optional[int] = ..., DateTime: _Optional[int] = ...) -> None: ...

class MarketOrdersModify(_message.Message):
    __slots__ = ("SymbolID", "Side", "Price", "Quantity", "OrderID", "PriorPrice", "PriorQuantity", "PriorOrderID", "DateTime")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    PRIORPRICE_FIELD_NUMBER: _ClassVar[int]
    PRIORQUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRIORORDERID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Side: BuySellEnum
    Price: float
    Quantity: int
    OrderID: int
    PriorPrice: float
    PriorQuantity: int
    PriorOrderID: int
    DateTime: int
    def __init__(self, SymbolID: _Optional[int] = ..., Side: _Optional[_Union[BuySellEnum, str]] = ..., Price: _Optional[float] = ..., Quantity: _Optional[int] = ..., OrderID: _Optional[int] = ..., PriorPrice: _Optional[float] = ..., PriorQuantity: _Optional[int] = ..., PriorOrderID: _Optional[int] = ..., DateTime: _Optional[int] = ...) -> None: ...

class MarketOrdersRemove(_message.Message):
    __slots__ = ("SymbolID", "Price", "Quantity", "OrderID", "DateTime", "Side")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    Price: float
    Quantity: int
    OrderID: int
    DateTime: int
    Side: BuySellEnum
    def __init__(self, SymbolID: _Optional[int] = ..., Price: _Optional[float] = ..., Quantity: _Optional[int] = ..., OrderID: _Optional[int] = ..., DateTime: _Optional[int] = ..., Side: _Optional[_Union[BuySellEnum, str]] = ...) -> None: ...

class MarketOrdersSnapshotMessageBoundary(_message.Message):
    __slots__ = ("SymbolID", "MessageBoundary")
    SYMBOLID_FIELD_NUMBER: _ClassVar[int]
    MESSAGEBOUNDARY_FIELD_NUMBER: _ClassVar[int]
    SymbolID: int
    MessageBoundary: MessageSetBoundaryEnum
    def __init__(self, SymbolID: _Optional[int] = ..., MessageBoundary: _Optional[_Union[MessageSetBoundaryEnum, str]] = ...) -> None: ...

class SubmitNewSingleOrder(_message.Message):
    __slots__ = ("Symbol", "Exchange", "TradeAccount", "ClientOrderID", "OrderType", "BuySell", "Price1", "Price2", "Quantity", "TimeInForce", "GoodTillDateTime", "IsAutomatedOrder", "IsParentOrder", "FreeFormText", "OpenOrClose", "MaxShowQuantity", "Price1AsString", "Price2AsString", "IntendedPositionQuantity")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_FIELD_NUMBER: _ClassVar[int]
    PRICE1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    ISAUTOMATEDORDER_FIELD_NUMBER: _ClassVar[int]
    ISPARENTORDER_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    OPENORCLOSE_FIELD_NUMBER: _ClassVar[int]
    MAXSHOWQUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE1ASSTRING_FIELD_NUMBER: _ClassVar[int]
    PRICE2ASSTRING_FIELD_NUMBER: _ClassVar[int]
    INTENDEDPOSITIONQUANTITY_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Exchange: str
    TradeAccount: str
    ClientOrderID: str
    OrderType: OrderTypeEnum
    BuySell: BuySellEnum
    Price1: float
    Price2: float
    Quantity: float
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    IsAutomatedOrder: int
    IsParentOrder: int
    FreeFormText: str
    OpenOrClose: OpenCloseTradeEnum
    MaxShowQuantity: float
    Price1AsString: str
    Price2AsString: str
    IntendedPositionQuantity: float
    def __init__(self, Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., OrderType: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell: _Optional[_Union[BuySellEnum, str]] = ..., Price1: _Optional[float] = ..., Price2: _Optional[float] = ..., Quantity: _Optional[float] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., IsAutomatedOrder: _Optional[int] = ..., IsParentOrder: _Optional[int] = ..., FreeFormText: _Optional[str] = ..., OpenOrClose: _Optional[_Union[OpenCloseTradeEnum, str]] = ..., MaxShowQuantity: _Optional[float] = ..., Price1AsString: _Optional[str] = ..., Price2AsString: _Optional[str] = ..., IntendedPositionQuantity: _Optional[float] = ...) -> None: ...

class SubmitNewSingleOrderInt(_message.Message):
    __slots__ = ("Symbol", "Exchange", "TradeAccount", "ClientOrderID", "OrderType", "BuySell", "Price1", "Price2", "Divisor", "Quantity", "TimeInForce", "GoodTillDateTime", "IsAutomatedOrder", "IsParentOrder", "FreeFormText", "OpenOrClose")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_FIELD_NUMBER: _ClassVar[int]
    PRICE1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_FIELD_NUMBER: _ClassVar[int]
    DIVISOR_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    ISAUTOMATEDORDER_FIELD_NUMBER: _ClassVar[int]
    ISPARENTORDER_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    OPENORCLOSE_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Exchange: str
    TradeAccount: str
    ClientOrderID: str
    OrderType: OrderTypeEnum
    BuySell: BuySellEnum
    Price1: int
    Price2: int
    Divisor: float
    Quantity: int
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    IsAutomatedOrder: int
    IsParentOrder: int
    FreeFormText: str
    OpenOrClose: OpenCloseTradeEnum
    def __init__(self, Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., OrderType: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell: _Optional[_Union[BuySellEnum, str]] = ..., Price1: _Optional[int] = ..., Price2: _Optional[int] = ..., Divisor: _Optional[float] = ..., Quantity: _Optional[int] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., IsAutomatedOrder: _Optional[int] = ..., IsParentOrder: _Optional[int] = ..., FreeFormText: _Optional[str] = ..., OpenOrClose: _Optional[_Union[OpenCloseTradeEnum, str]] = ...) -> None: ...

class SubmitFlattenPositionOrder(_message.Message):
    __slots__ = ("Symbol", "Exchange", "TradeAccount", "ClientOrderID", "FreeFormText", "IsAutomatedOrder")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    ISAUTOMATEDORDER_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Exchange: str
    TradeAccount: str
    ClientOrderID: str
    FreeFormText: str
    IsAutomatedOrder: int
    def __init__(self, Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., FreeFormText: _Optional[str] = ..., IsAutomatedOrder: _Optional[int] = ...) -> None: ...

class FlattenPositionsForTradeAccount(_message.Message):
    __slots__ = ("TradeAccount", "ClientOrderID", "FreeFormText", "IsAutomatedOrder")
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    ISAUTOMATEDORDER_FIELD_NUMBER: _ClassVar[int]
    TradeAccount: str
    ClientOrderID: str
    FreeFormText: str
    IsAutomatedOrder: int
    def __init__(self, TradeAccount: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., FreeFormText: _Optional[str] = ..., IsAutomatedOrder: _Optional[int] = ...) -> None: ...

class CancelReplaceOrder(_message.Message):
    __slots__ = ("ServerOrderID", "ClientOrderID", "Price1", "Price2", "Quantity", "Price1IsSet", "Price2IsSet", "TimeInForce", "GoodTillDateTime", "UpdatePrice1OffsetToParent", "TradeAccount", "Price1AsString", "Price2AsString")
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    PRICE1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE1ISSET_FIELD_NUMBER: _ClassVar[int]
    PRICE2ISSET_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    UPDATEPRICE1OFFSETTOPARENT_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE1ASSTRING_FIELD_NUMBER: _ClassVar[int]
    PRICE2ASSTRING_FIELD_NUMBER: _ClassVar[int]
    ServerOrderID: str
    ClientOrderID: str
    Price1: float
    Price2: float
    Quantity: float
    Price1IsSet: int
    Price2IsSet: int
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    UpdatePrice1OffsetToParent: int
    TradeAccount: str
    Price1AsString: str
    Price2AsString: str
    def __init__(self, ServerOrderID: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., Price1: _Optional[float] = ..., Price2: _Optional[float] = ..., Quantity: _Optional[float] = ..., Price1IsSet: _Optional[int] = ..., Price2IsSet: _Optional[int] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., UpdatePrice1OffsetToParent: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., Price1AsString: _Optional[str] = ..., Price2AsString: _Optional[str] = ...) -> None: ...

class CancelReplaceOrderInt(_message.Message):
    __slots__ = ("ServerOrderID", "ClientOrderID", "Price1", "Price2", "Divisor", "Quantity", "Price1IsSet", "Price2IsSet", "TimeInForce", "GoodTillDateTime", "UpdatePrice1OffsetToParent")
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    PRICE1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_FIELD_NUMBER: _ClassVar[int]
    DIVISOR_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE1ISSET_FIELD_NUMBER: _ClassVar[int]
    PRICE2ISSET_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    UPDATEPRICE1OFFSETTOPARENT_FIELD_NUMBER: _ClassVar[int]
    ServerOrderID: str
    ClientOrderID: str
    Price1: int
    Price2: int
    Divisor: float
    Quantity: int
    Price1IsSet: int
    Price2IsSet: int
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    UpdatePrice1OffsetToParent: int
    def __init__(self, ServerOrderID: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., Price1: _Optional[int] = ..., Price2: _Optional[int] = ..., Divisor: _Optional[float] = ..., Quantity: _Optional[int] = ..., Price1IsSet: _Optional[int] = ..., Price2IsSet: _Optional[int] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., UpdatePrice1OffsetToParent: _Optional[int] = ...) -> None: ...

class CancelOrder(_message.Message):
    __slots__ = ("ServerOrderID", "ClientOrderID", "TradeAccount")
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ServerOrderID: str
    ClientOrderID: str
    TradeAccount: str
    def __init__(self, ServerOrderID: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class SubmitNewOCOOrder(_message.Message):
    __slots__ = ("Symbol", "Exchange", "ClientOrderID_1", "OrderType_1", "BuySell_1", "Price1_1", "Price2_1", "Quantity_1", "ClientOrderID_2", "OrderType_2", "BuySell_2", "Price1_2", "Price2_2", "Quantity_2", "TimeInForce", "GoodTillDateTime", "TradeAccount", "IsAutomatedOrder", "ParentTriggerClientOrderID", "FreeFormText", "OpenOrClose", "PartialFillHandling", "UseOffsets", "OffsetFromParent1", "OffsetFromParent2", "MaintainSamePricesOnParentFill", "Price1_1AsString", "Price2_1AsString", "Price1_2AsString", "Price2_2AsString")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_1_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_1_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_1_FIELD_NUMBER: _ClassVar[int]
    PRICE1_1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_1_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_1_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_2_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_2_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_2_FIELD_NUMBER: _ClassVar[int]
    PRICE1_2_FIELD_NUMBER: _ClassVar[int]
    PRICE2_2_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_2_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISAUTOMATEDORDER_FIELD_NUMBER: _ClassVar[int]
    PARENTTRIGGERCLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    OPENORCLOSE_FIELD_NUMBER: _ClassVar[int]
    PARTIALFILLHANDLING_FIELD_NUMBER: _ClassVar[int]
    USEOFFSETS_FIELD_NUMBER: _ClassVar[int]
    OFFSETFROMPARENT1_FIELD_NUMBER: _ClassVar[int]
    OFFSETFROMPARENT2_FIELD_NUMBER: _ClassVar[int]
    MAINTAINSAMEPRICESONPARENTFILL_FIELD_NUMBER: _ClassVar[int]
    PRICE1_1ASSTRING_FIELD_NUMBER: _ClassVar[int]
    PRICE2_1ASSTRING_FIELD_NUMBER: _ClassVar[int]
    PRICE1_2ASSTRING_FIELD_NUMBER: _ClassVar[int]
    PRICE2_2ASSTRING_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Exchange: str
    ClientOrderID_1: str
    OrderType_1: OrderTypeEnum
    BuySell_1: BuySellEnum
    Price1_1: float
    Price2_1: float
    Quantity_1: float
    ClientOrderID_2: str
    OrderType_2: OrderTypeEnum
    BuySell_2: BuySellEnum
    Price1_2: float
    Price2_2: float
    Quantity_2: float
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    TradeAccount: str
    IsAutomatedOrder: int
    ParentTriggerClientOrderID: str
    FreeFormText: str
    OpenOrClose: OpenCloseTradeEnum
    PartialFillHandling: PartialFillHandlingEnum
    UseOffsets: int
    OffsetFromParent1: float
    OffsetFromParent2: float
    MaintainSamePricesOnParentFill: int
    Price1_1AsString: str
    Price2_1AsString: str
    Price1_2AsString: str
    Price2_2AsString: str
    def __init__(self, Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., ClientOrderID_1: _Optional[str] = ..., OrderType_1: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell_1: _Optional[_Union[BuySellEnum, str]] = ..., Price1_1: _Optional[float] = ..., Price2_1: _Optional[float] = ..., Quantity_1: _Optional[float] = ..., ClientOrderID_2: _Optional[str] = ..., OrderType_2: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell_2: _Optional[_Union[BuySellEnum, str]] = ..., Price1_2: _Optional[float] = ..., Price2_2: _Optional[float] = ..., Quantity_2: _Optional[float] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., IsAutomatedOrder: _Optional[int] = ..., ParentTriggerClientOrderID: _Optional[str] = ..., FreeFormText: _Optional[str] = ..., OpenOrClose: _Optional[_Union[OpenCloseTradeEnum, str]] = ..., PartialFillHandling: _Optional[_Union[PartialFillHandlingEnum, str]] = ..., UseOffsets: _Optional[int] = ..., OffsetFromParent1: _Optional[float] = ..., OffsetFromParent2: _Optional[float] = ..., MaintainSamePricesOnParentFill: _Optional[int] = ..., Price1_1AsString: _Optional[str] = ..., Price2_1AsString: _Optional[str] = ..., Price1_2AsString: _Optional[str] = ..., Price2_2AsString: _Optional[str] = ...) -> None: ...

class SubmitNewOCOOrderInt(_message.Message):
    __slots__ = ("Symbol", "Exchange", "ClientOrderID_1", "OrderType_1", "BuySell_1", "Price1_1", "Price2_1", "Quantity_1", "ClientOrderID_2", "OrderType_2", "BuySell_2", "Price1_2", "Price2_2", "Quantity_2", "TimeInForce", "GoodTillDateTime", "TradeAccount", "IsAutomatedOrder", "ParentTriggerClientOrderID", "FreeFormText", "Divisor", "OpenOrClose", "PartialFillHandling")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_1_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_1_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_1_FIELD_NUMBER: _ClassVar[int]
    PRICE1_1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_1_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_1_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_2_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_2_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_2_FIELD_NUMBER: _ClassVar[int]
    PRICE1_2_FIELD_NUMBER: _ClassVar[int]
    PRICE2_2_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_2_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISAUTOMATEDORDER_FIELD_NUMBER: _ClassVar[int]
    PARENTTRIGGERCLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    DIVISOR_FIELD_NUMBER: _ClassVar[int]
    OPENORCLOSE_FIELD_NUMBER: _ClassVar[int]
    PARTIALFILLHANDLING_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Exchange: str
    ClientOrderID_1: str
    OrderType_1: OrderTypeEnum
    BuySell_1: BuySellEnum
    Price1_1: int
    Price2_1: int
    Quantity_1: int
    ClientOrderID_2: str
    OrderType_2: OrderTypeEnum
    BuySell_2: BuySellEnum
    Price1_2: int
    Price2_2: int
    Quantity_2: int
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    TradeAccount: str
    IsAutomatedOrder: int
    ParentTriggerClientOrderID: str
    FreeFormText: str
    Divisor: float
    OpenOrClose: OpenCloseTradeEnum
    PartialFillHandling: PartialFillHandlingEnum
    def __init__(self, Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., ClientOrderID_1: _Optional[str] = ..., OrderType_1: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell_1: _Optional[_Union[BuySellEnum, str]] = ..., Price1_1: _Optional[int] = ..., Price2_1: _Optional[int] = ..., Quantity_1: _Optional[int] = ..., ClientOrderID_2: _Optional[str] = ..., OrderType_2: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell_2: _Optional[_Union[BuySellEnum, str]] = ..., Price1_2: _Optional[int] = ..., Price2_2: _Optional[int] = ..., Quantity_2: _Optional[int] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., IsAutomatedOrder: _Optional[int] = ..., ParentTriggerClientOrderID: _Optional[str] = ..., FreeFormText: _Optional[str] = ..., Divisor: _Optional[float] = ..., OpenOrClose: _Optional[_Union[OpenCloseTradeEnum, str]] = ..., PartialFillHandling: _Optional[_Union[PartialFillHandlingEnum, str]] = ...) -> None: ...

class OpenOrdersRequest(_message.Message):
    __slots__ = ("RequestID", "RequestAllOrders", "ServerOrderID", "TradeAccount")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REQUESTALLORDERS_FIELD_NUMBER: _ClassVar[int]
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RequestAllOrders: int
    ServerOrderID: str
    TradeAccount: str
    def __init__(self, RequestID: _Optional[int] = ..., RequestAllOrders: _Optional[int] = ..., ServerOrderID: _Optional[str] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class HistoricalOrderFillsRequest(_message.Message):
    __slots__ = ("RequestID", "ServerOrderID", "NumberOfDays", "TradeAccount", "StartDateTime")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFDAYS_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    ServerOrderID: str
    NumberOfDays: int
    TradeAccount: str
    StartDateTime: int
    def __init__(self, RequestID: _Optional[int] = ..., ServerOrderID: _Optional[str] = ..., NumberOfDays: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., StartDateTime: _Optional[int] = ...) -> None: ...

class HistoricalOrderFillsReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class CurrentPositionsRequest(_message.Message):
    __slots__ = ("RequestID", "TradeAccount")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TradeAccount: str
    def __init__(self, RequestID: _Optional[int] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class CurrentPositionsReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class OrderUpdate(_message.Message):
    __slots__ = ("RequestID", "TotalNumMessages", "MessageNumber", "Symbol", "Exchange", "PreviousServerOrderID", "ServerOrderID", "ClientOrderID", "ExchangeOrderID", "OrderStatus", "OrderUpdateReason", "OrderType", "BuySell", "Price1", "Price2", "TimeInForce", "GoodTillDateTime", "OrderQuantity", "FilledQuantity", "RemainingQuantity", "AverageFillPrice", "LastFillPrice", "LastFillDateTime", "LastFillQuantity", "LastFillExecutionID", "TradeAccount", "InfoText", "NoOrders", "ParentServerOrderID", "OCOLinkedOrderServerOrderID", "OpenOrClose", "PreviousClientOrderID", "FreeFormText", "OrderReceivedDateTime", "LatestTransactionDateTime", "Username")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TOTALNUMMESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSSERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEORDERID_FIELD_NUMBER: _ClassVar[int]
    ORDERSTATUS_FIELD_NUMBER: _ClassVar[int]
    ORDERUPDATEREASON_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_FIELD_NUMBER: _ClassVar[int]
    PRICE1_FIELD_NUMBER: _ClassVar[int]
    PRICE2_FIELD_NUMBER: _ClassVar[int]
    TIMEINFORCE_FIELD_NUMBER: _ClassVar[int]
    GOODTILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    ORDERQUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    REMAININGQUANTITY_FIELD_NUMBER: _ClassVar[int]
    AVERAGEFILLPRICE_FIELD_NUMBER: _ClassVar[int]
    LASTFILLPRICE_FIELD_NUMBER: _ClassVar[int]
    LASTFILLDATETIME_FIELD_NUMBER: _ClassVar[int]
    LASTFILLQUANTITY_FIELD_NUMBER: _ClassVar[int]
    LASTFILLEXECUTIONID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    INFOTEXT_FIELD_NUMBER: _ClassVar[int]
    NOORDERS_FIELD_NUMBER: _ClassVar[int]
    PARENTSERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    OCOLINKEDORDERSERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    OPENORCLOSE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSCLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    ORDERRECEIVEDDATETIME_FIELD_NUMBER: _ClassVar[int]
    LATESTTRANSACTIONDATETIME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TotalNumMessages: int
    MessageNumber: int
    Symbol: str
    Exchange: str
    PreviousServerOrderID: str
    ServerOrderID: str
    ClientOrderID: str
    ExchangeOrderID: str
    OrderStatus: OrderStatusEnum
    OrderUpdateReason: OrderUpdateReasonEnum
    OrderType: OrderTypeEnum
    BuySell: BuySellEnum
    Price1: float
    Price2: float
    TimeInForce: TimeInForceEnum
    GoodTillDateTime: int
    OrderQuantity: float
    FilledQuantity: float
    RemainingQuantity: float
    AverageFillPrice: float
    LastFillPrice: float
    LastFillDateTime: int
    LastFillQuantity: float
    LastFillExecutionID: str
    TradeAccount: str
    InfoText: str
    NoOrders: int
    ParentServerOrderID: str
    OCOLinkedOrderServerOrderID: str
    OpenOrClose: OpenCloseTradeEnum
    PreviousClientOrderID: str
    FreeFormText: str
    OrderReceivedDateTime: int
    LatestTransactionDateTime: float
    Username: str
    def __init__(self, RequestID: _Optional[int] = ..., TotalNumMessages: _Optional[int] = ..., MessageNumber: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., PreviousServerOrderID: _Optional[str] = ..., ServerOrderID: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., ExchangeOrderID: _Optional[str] = ..., OrderStatus: _Optional[_Union[OrderStatusEnum, str]] = ..., OrderUpdateReason: _Optional[_Union[OrderUpdateReasonEnum, str]] = ..., OrderType: _Optional[_Union[OrderTypeEnum, str]] = ..., BuySell: _Optional[_Union[BuySellEnum, str]] = ..., Price1: _Optional[float] = ..., Price2: _Optional[float] = ..., TimeInForce: _Optional[_Union[TimeInForceEnum, str]] = ..., GoodTillDateTime: _Optional[int] = ..., OrderQuantity: _Optional[float] = ..., FilledQuantity: _Optional[float] = ..., RemainingQuantity: _Optional[float] = ..., AverageFillPrice: _Optional[float] = ..., LastFillPrice: _Optional[float] = ..., LastFillDateTime: _Optional[int] = ..., LastFillQuantity: _Optional[float] = ..., LastFillExecutionID: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., InfoText: _Optional[str] = ..., NoOrders: _Optional[int] = ..., ParentServerOrderID: _Optional[str] = ..., OCOLinkedOrderServerOrderID: _Optional[str] = ..., OpenOrClose: _Optional[_Union[OpenCloseTradeEnum, str]] = ..., PreviousClientOrderID: _Optional[str] = ..., FreeFormText: _Optional[str] = ..., OrderReceivedDateTime: _Optional[int] = ..., LatestTransactionDateTime: _Optional[float] = ..., Username: _Optional[str] = ...) -> None: ...

class OpenOrdersReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class HistoricalOrderFillResponse(_message.Message):
    __slots__ = ("RequestID", "TotalNumberMessages", "MessageNumber", "Symbol", "Exchange", "ServerOrderID", "BuySell", "Price", "DateTime", "Quantity", "UniqueExecutionID", "TradeAccount", "OpenClose", "NoOrderFills", "InfoText", "HighPriceDuringPosition", "LowPriceDuringPosition", "PositionQuantity", "Username", "ExchangeOrderID", "SenderSubID")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TOTALNUMBERMESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SERVERORDERID_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIQUEEXECUTIONID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    OPENCLOSE_FIELD_NUMBER: _ClassVar[int]
    NOORDERFILLS_FIELD_NUMBER: _ClassVar[int]
    INFOTEXT_FIELD_NUMBER: _ClassVar[int]
    HIGHPRICEDURINGPOSITION_FIELD_NUMBER: _ClassVar[int]
    LOWPRICEDURINGPOSITION_FIELD_NUMBER: _ClassVar[int]
    POSITIONQUANTITY_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGEORDERID_FIELD_NUMBER: _ClassVar[int]
    SENDERSUBID_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TotalNumberMessages: int
    MessageNumber: int
    Symbol: str
    Exchange: str
    ServerOrderID: str
    BuySell: BuySellEnum
    Price: float
    DateTime: int
    Quantity: float
    UniqueExecutionID: str
    TradeAccount: str
    OpenClose: OpenCloseTradeEnum
    NoOrderFills: int
    InfoText: str
    HighPriceDuringPosition: float
    LowPriceDuringPosition: float
    PositionQuantity: float
    Username: str
    ExchangeOrderID: str
    SenderSubID: str
    def __init__(self, RequestID: _Optional[int] = ..., TotalNumberMessages: _Optional[int] = ..., MessageNumber: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., ServerOrderID: _Optional[str] = ..., BuySell: _Optional[_Union[BuySellEnum, str]] = ..., Price: _Optional[float] = ..., DateTime: _Optional[int] = ..., Quantity: _Optional[float] = ..., UniqueExecutionID: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., OpenClose: _Optional[_Union[OpenCloseTradeEnum, str]] = ..., NoOrderFills: _Optional[int] = ..., InfoText: _Optional[str] = ..., HighPriceDuringPosition: _Optional[float] = ..., LowPriceDuringPosition: _Optional[float] = ..., PositionQuantity: _Optional[float] = ..., Username: _Optional[str] = ..., ExchangeOrderID: _Optional[str] = ..., SenderSubID: _Optional[str] = ...) -> None: ...

class PositionUpdate(_message.Message):
    __slots__ = ("RequestID", "TotalNumberMessages", "MessageNumber", "Symbol", "Exchange", "Quantity", "AveragePrice", "PositionIdentifier", "TradeAccount", "NoPositions", "Unsolicited", "MarginRequirement", "EntryDateTime", "OpenProfitLoss", "HighPriceDuringPosition", "LowPriceDuringPosition", "QuantityLimit", "MaxPotentialPostionQuantity")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TOTALNUMBERMESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AVERAGEPRICE_FIELD_NUMBER: _ClassVar[int]
    POSITIONIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NOPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    UNSOLICITED_FIELD_NUMBER: _ClassVar[int]
    MARGINREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    ENTRYDATETIME_FIELD_NUMBER: _ClassVar[int]
    OPENPROFITLOSS_FIELD_NUMBER: _ClassVar[int]
    HIGHPRICEDURINGPOSITION_FIELD_NUMBER: _ClassVar[int]
    LOWPRICEDURINGPOSITION_FIELD_NUMBER: _ClassVar[int]
    QUANTITYLIMIT_FIELD_NUMBER: _ClassVar[int]
    MAXPOTENTIALPOSTIONQUANTITY_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TotalNumberMessages: int
    MessageNumber: int
    Symbol: str
    Exchange: str
    Quantity: float
    AveragePrice: float
    PositionIdentifier: str
    TradeAccount: str
    NoPositions: int
    Unsolicited: int
    MarginRequirement: float
    EntryDateTime: int
    OpenProfitLoss: float
    HighPriceDuringPosition: float
    LowPriceDuringPosition: float
    QuantityLimit: float
    MaxPotentialPostionQuantity: float
    def __init__(self, RequestID: _Optional[int] = ..., TotalNumberMessages: _Optional[int] = ..., MessageNumber: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., Quantity: _Optional[float] = ..., AveragePrice: _Optional[float] = ..., PositionIdentifier: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., NoPositions: _Optional[int] = ..., Unsolicited: _Optional[int] = ..., MarginRequirement: _Optional[float] = ..., EntryDateTime: _Optional[int] = ..., OpenProfitLoss: _Optional[float] = ..., HighPriceDuringPosition: _Optional[float] = ..., LowPriceDuringPosition: _Optional[float] = ..., QuantityLimit: _Optional[float] = ..., MaxPotentialPostionQuantity: _Optional[float] = ...) -> None: ...

class AddCorrectingOrderFill(_message.Message):
    __slots__ = ("Symbol", "Exchange", "TradeAccount", "ClientOrderID", "BuySell", "FillPrice", "FillQuantity", "FreeFormText")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    BUYSELL_FIELD_NUMBER: _ClassVar[int]
    FILLPRICE_FIELD_NUMBER: _ClassVar[int]
    FILLQUANTITY_FIELD_NUMBER: _ClassVar[int]
    FREEFORMTEXT_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Exchange: str
    TradeAccount: str
    ClientOrderID: str
    BuySell: BuySellEnum
    FillPrice: float
    FillQuantity: float
    FreeFormText: str
    def __init__(self, Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., ClientOrderID: _Optional[str] = ..., BuySell: _Optional[_Union[BuySellEnum, str]] = ..., FillPrice: _Optional[float] = ..., FillQuantity: _Optional[float] = ..., FreeFormText: _Optional[str] = ...) -> None: ...

class CorrectingOrderFillResponse(_message.Message):
    __slots__ = ("ClientOrderID", "ResultText", "IsError")
    CLIENTORDERID_FIELD_NUMBER: _ClassVar[int]
    RESULTTEXT_FIELD_NUMBER: _ClassVar[int]
    ISERROR_FIELD_NUMBER: _ClassVar[int]
    ClientOrderID: str
    ResultText: str
    IsError: int
    def __init__(self, ClientOrderID: _Optional[str] = ..., ResultText: _Optional[str] = ..., IsError: _Optional[int] = ...) -> None: ...

class TradeAccountsRequest(_message.Message):
    __slots__ = ("RequestID",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    def __init__(self, RequestID: _Optional[int] = ...) -> None: ...

class TradeAccountResponse(_message.Message):
    __slots__ = ("TotalNumberMessages", "MessageNumber", "TradeAccount", "RequestID")
    TOTALNUMBERMESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TotalNumberMessages: int
    MessageNumber: int
    TradeAccount: str
    RequestID: int
    def __init__(self, TotalNumberMessages: _Optional[int] = ..., MessageNumber: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., RequestID: _Optional[int] = ...) -> None: ...

class ExchangeListRequest(_message.Message):
    __slots__ = ("RequestID",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    def __init__(self, RequestID: _Optional[int] = ...) -> None: ...

class ExchangeListResponse(_message.Message):
    __slots__ = ("RequestID", "Exchange", "IsFinalMessage", "Description")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    ISFINALMESSAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Exchange: str
    IsFinalMessage: int
    Description: str
    def __init__(self, RequestID: _Optional[int] = ..., Exchange: _Optional[str] = ..., IsFinalMessage: _Optional[int] = ..., Description: _Optional[str] = ...) -> None: ...

class SymbolsForExchangeRequest(_message.Message):
    __slots__ = ("RequestID", "Exchange", "SecurityType", "RequestAction", "Symbol")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTACTION_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Exchange: str
    SecurityType: SecurityTypeEnum
    RequestAction: RequestActionEnum
    Symbol: str
    def __init__(self, RequestID: _Optional[int] = ..., Exchange: _Optional[str] = ..., SecurityType: _Optional[_Union[SecurityTypeEnum, str]] = ..., RequestAction: _Optional[_Union[RequestActionEnum, str]] = ..., Symbol: _Optional[str] = ...) -> None: ...

class UnderlyingSymbolsForExchangeRequest(_message.Message):
    __slots__ = ("RequestID", "Exchange", "SecurityType")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Exchange: str
    SecurityType: SecurityTypeEnum
    def __init__(self, RequestID: _Optional[int] = ..., Exchange: _Optional[str] = ..., SecurityType: _Optional[_Union[SecurityTypeEnum, str]] = ...) -> None: ...

class SymbolsForUnderlyingRequest(_message.Message):
    __slots__ = ("RequestID", "UnderlyingSymbol", "Exchange", "SecurityType")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    UnderlyingSymbol: str
    Exchange: str
    SecurityType: SecurityTypeEnum
    def __init__(self, RequestID: _Optional[int] = ..., UnderlyingSymbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., SecurityType: _Optional[_Union[SecurityTypeEnum, str]] = ...) -> None: ...

class SymbolSearchRequest(_message.Message):
    __slots__ = ("RequestID", "SearchText", "Exchange", "SecurityType", "SearchType")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SEARCHTEXT_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCHTYPE_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    SearchText: str
    Exchange: str
    SecurityType: SecurityTypeEnum
    SearchType: SearchTypeEnum
    def __init__(self, RequestID: _Optional[int] = ..., SearchText: _Optional[str] = ..., Exchange: _Optional[str] = ..., SecurityType: _Optional[_Union[SecurityTypeEnum, str]] = ..., SearchType: _Optional[_Union[SearchTypeEnum, str]] = ...) -> None: ...

class SecurityDefinitionForSymbolRequest(_message.Message):
    __slots__ = ("RequestID", "Symbol", "Exchange")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Symbol: str
    Exchange: str
    def __init__(self, RequestID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ...) -> None: ...

class SecurityDefinitionResponse(_message.Message):
    __slots__ = ("RequestID", "Symbol", "Exchange", "SecurityType", "Description", "MinPriceIncrement", "PriceDisplayFormat", "CurrencyValuePerIncrement", "IsFinalMessage", "FloatToIntPriceMultiplier", "IntToFloatPriceDivisor", "UnderlyingSymbol", "UpdatesBidAskOnly", "StrikePrice", "PutOrCall", "ShortInterest", "SecurityExpirationDate", "BuyRolloverInterest", "SellRolloverInterest", "EarningsPerShare", "SharesOutstanding", "IntToFloatQuantityDivisor", "HasMarketDepthData", "DisplayPriceMultiplier", "ExchangeSymbol", "InitialMarginRequirement", "MaintenanceMarginRequirement", "Currency", "ContractSize", "OpenInterest", "RolloverDate", "IsDelayed", "SecurityIdentifier", "ProductIdentifier")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MINPRICEINCREMENT_FIELD_NUMBER: _ClassVar[int]
    PRICEDISPLAYFORMAT_FIELD_NUMBER: _ClassVar[int]
    CURRENCYVALUEPERINCREMENT_FIELD_NUMBER: _ClassVar[int]
    ISFINALMESSAGE_FIELD_NUMBER: _ClassVar[int]
    FLOATTOINTPRICEMULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    INTTOFLOATPRICEDIVISOR_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    UPDATESBIDASKONLY_FIELD_NUMBER: _ClassVar[int]
    STRIKEPRICE_FIELD_NUMBER: _ClassVar[int]
    PUTORCALL_FIELD_NUMBER: _ClassVar[int]
    SHORTINTEREST_FIELD_NUMBER: _ClassVar[int]
    SECURITYEXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    BUYROLLOVERINTEREST_FIELD_NUMBER: _ClassVar[int]
    SELLROLLOVERINTEREST_FIELD_NUMBER: _ClassVar[int]
    EARNINGSPERSHARE_FIELD_NUMBER: _ClassVar[int]
    SHARESOUTSTANDING_FIELD_NUMBER: _ClassVar[int]
    INTTOFLOATQUANTITYDIVISOR_FIELD_NUMBER: _ClassVar[int]
    HASMARKETDEPTHDATA_FIELD_NUMBER: _ClassVar[int]
    DISPLAYPRICEMULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    EXCHANGESYMBOL_FIELD_NUMBER: _ClassVar[int]
    INITIALMARGINREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCEMARGINREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CONTRACTSIZE_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    ROLLOVERDATE_FIELD_NUMBER: _ClassVar[int]
    ISDELAYED_FIELD_NUMBER: _ClassVar[int]
    SECURITYIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PRODUCTIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Symbol: str
    Exchange: str
    SecurityType: SecurityTypeEnum
    Description: str
    MinPriceIncrement: float
    PriceDisplayFormat: PriceDisplayFormatEnum
    CurrencyValuePerIncrement: float
    IsFinalMessage: int
    FloatToIntPriceMultiplier: float
    IntToFloatPriceDivisor: float
    UnderlyingSymbol: str
    UpdatesBidAskOnly: int
    StrikePrice: float
    PutOrCall: PutCallEnum
    ShortInterest: int
    SecurityExpirationDate: int
    BuyRolloverInterest: float
    SellRolloverInterest: float
    EarningsPerShare: float
    SharesOutstanding: int
    IntToFloatQuantityDivisor: float
    HasMarketDepthData: int
    DisplayPriceMultiplier: float
    ExchangeSymbol: str
    InitialMarginRequirement: float
    MaintenanceMarginRequirement: float
    Currency: str
    ContractSize: float
    OpenInterest: int
    RolloverDate: int
    IsDelayed: int
    SecurityIdentifier: int
    ProductIdentifier: str
    def __init__(self, RequestID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., SecurityType: _Optional[_Union[SecurityTypeEnum, str]] = ..., Description: _Optional[str] = ..., MinPriceIncrement: _Optional[float] = ..., PriceDisplayFormat: _Optional[_Union[PriceDisplayFormatEnum, str]] = ..., CurrencyValuePerIncrement: _Optional[float] = ..., IsFinalMessage: _Optional[int] = ..., FloatToIntPriceMultiplier: _Optional[float] = ..., IntToFloatPriceDivisor: _Optional[float] = ..., UnderlyingSymbol: _Optional[str] = ..., UpdatesBidAskOnly: _Optional[int] = ..., StrikePrice: _Optional[float] = ..., PutOrCall: _Optional[_Union[PutCallEnum, str]] = ..., ShortInterest: _Optional[int] = ..., SecurityExpirationDate: _Optional[int] = ..., BuyRolloverInterest: _Optional[float] = ..., SellRolloverInterest: _Optional[float] = ..., EarningsPerShare: _Optional[float] = ..., SharesOutstanding: _Optional[int] = ..., IntToFloatQuantityDivisor: _Optional[float] = ..., HasMarketDepthData: _Optional[int] = ..., DisplayPriceMultiplier: _Optional[float] = ..., ExchangeSymbol: _Optional[str] = ..., InitialMarginRequirement: _Optional[float] = ..., MaintenanceMarginRequirement: _Optional[float] = ..., Currency: _Optional[str] = ..., ContractSize: _Optional[float] = ..., OpenInterest: _Optional[int] = ..., RolloverDate: _Optional[int] = ..., IsDelayed: _Optional[int] = ..., SecurityIdentifier: _Optional[int] = ..., ProductIdentifier: _Optional[str] = ...) -> None: ...

class SecurityDefinitionReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class AccountBalanceRequest(_message.Message):
    __slots__ = ("RequestID", "TradeAccount")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TradeAccount: str
    def __init__(self, RequestID: _Optional[int] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class AccountBalanceReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class AccountBalanceUpdate(_message.Message):
    __slots__ = ("RequestID", "CashBalance", "BalanceAvailableForNewPositions", "AccountCurrency", "TradeAccount", "SecuritiesValue", "MarginRequirement", "TotalNumberMessages", "MessageNumber", "NoAccountBalances", "Unsolicited", "OpenPositionsProfitLoss", "DailyProfitLoss", "InfoText", "TransactionIdentifier", "DailyNetLossLimit", "TrailingAccountValueToLimitPositions", "DailyNetLossLimitReached", "IsUnderRequiredMargin", "ClosePositionsAtEndOfDay", "TradingIsDisabled", "Description", "IsUnderRequiredAccountValue", "TransactionDateTime", "MarginRequirementFull", "MarginRequirementFullPositionsOnly", "PeakMarginRequirement", "IntroducingBroker")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    CASHBALANCE_FIELD_NUMBER: _ClassVar[int]
    BALANCEAVAILABLEFORNEWPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTCURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SECURITIESVALUE_FIELD_NUMBER: _ClassVar[int]
    MARGINREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    TOTALNUMBERMESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    NOACCOUNTBALANCES_FIELD_NUMBER: _ClassVar[int]
    UNSOLICITED_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSPROFITLOSS_FIELD_NUMBER: _ClassVar[int]
    DAILYPROFITLOSS_FIELD_NUMBER: _ClassVar[int]
    INFOTEXT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DAILYNETLOSSLIMIT_FIELD_NUMBER: _ClassVar[int]
    TRAILINGACCOUNTVALUETOLIMITPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    DAILYNETLOSSLIMITREACHED_FIELD_NUMBER: _ClassVar[int]
    ISUNDERREQUIREDMARGIN_FIELD_NUMBER: _ClassVar[int]
    CLOSEPOSITIONSATENDOFDAY_FIELD_NUMBER: _ClassVar[int]
    TRADINGISDISABLED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ISUNDERREQUIREDACCOUNTVALUE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONDATETIME_FIELD_NUMBER: _ClassVar[int]
    MARGINREQUIREMENTFULL_FIELD_NUMBER: _ClassVar[int]
    MARGINREQUIREMENTFULLPOSITIONSONLY_FIELD_NUMBER: _ClassVar[int]
    PEAKMARGINREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    INTRODUCINGBROKER_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    CashBalance: float
    BalanceAvailableForNewPositions: float
    AccountCurrency: str
    TradeAccount: str
    SecuritiesValue: float
    MarginRequirement: float
    TotalNumberMessages: int
    MessageNumber: int
    NoAccountBalances: int
    Unsolicited: int
    OpenPositionsProfitLoss: float
    DailyProfitLoss: float
    InfoText: str
    TransactionIdentifier: int
    DailyNetLossLimit: float
    TrailingAccountValueToLimitPositions: float
    DailyNetLossLimitReached: int
    IsUnderRequiredMargin: int
    ClosePositionsAtEndOfDay: int
    TradingIsDisabled: int
    Description: str
    IsUnderRequiredAccountValue: int
    TransactionDateTime: int
    MarginRequirementFull: float
    MarginRequirementFullPositionsOnly: float
    PeakMarginRequirement: float
    IntroducingBroker: str
    def __init__(self, RequestID: _Optional[int] = ..., CashBalance: _Optional[float] = ..., BalanceAvailableForNewPositions: _Optional[float] = ..., AccountCurrency: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., SecuritiesValue: _Optional[float] = ..., MarginRequirement: _Optional[float] = ..., TotalNumberMessages: _Optional[int] = ..., MessageNumber: _Optional[int] = ..., NoAccountBalances: _Optional[int] = ..., Unsolicited: _Optional[int] = ..., OpenPositionsProfitLoss: _Optional[float] = ..., DailyProfitLoss: _Optional[float] = ..., InfoText: _Optional[str] = ..., TransactionIdentifier: _Optional[int] = ..., DailyNetLossLimit: _Optional[float] = ..., TrailingAccountValueToLimitPositions: _Optional[float] = ..., DailyNetLossLimitReached: _Optional[int] = ..., IsUnderRequiredMargin: _Optional[int] = ..., ClosePositionsAtEndOfDay: _Optional[int] = ..., TradingIsDisabled: _Optional[int] = ..., Description: _Optional[str] = ..., IsUnderRequiredAccountValue: _Optional[int] = ..., TransactionDateTime: _Optional[int] = ..., MarginRequirementFull: _Optional[float] = ..., MarginRequirementFullPositionsOnly: _Optional[float] = ..., PeakMarginRequirement: _Optional[float] = ..., IntroducingBroker: _Optional[str] = ...) -> None: ...

class AccountBalanceAdjustment(_message.Message):
    __slots__ = ("RequestID", "CreditAmount", "DebitAmount", "Currency", "Reason", "TradeAccount")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    CREDITAMOUNT_FIELD_NUMBER: _ClassVar[int]
    DEBITAMOUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    CreditAmount: float
    DebitAmount: float
    Currency: str
    Reason: str
    TradeAccount: str
    def __init__(self, RequestID: _Optional[int] = ..., CreditAmount: _Optional[float] = ..., DebitAmount: _Optional[float] = ..., Currency: _Optional[str] = ..., Reason: _Optional[str] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class AccountBalanceAdjustmentReject(_message.Message):
    __slots__ = ("RequestID", "RejectText", "TradeAccount")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    TradeAccount: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class AccountBalanceAdjustmentComplete(_message.Message):
    __slots__ = ("RequestID", "TransactionID", "TradeAccount", "NewBalance")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NEWBALANCE_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TransactionID: int
    TradeAccount: str
    NewBalance: float
    def __init__(self, RequestID: _Optional[int] = ..., TransactionID: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., NewBalance: _Optional[float] = ...) -> None: ...

class HistoricalAccountBalancesRequest(_message.Message):
    __slots__ = ("RequestID", "TradeAccount", "StartDateTime")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TradeAccount: str
    StartDateTime: int
    def __init__(self, RequestID: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., StartDateTime: _Optional[int] = ...) -> None: ...

class HistoricalAccountBalancesReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class HistoricalAccountBalanceResponse(_message.Message):
    __slots__ = ("RequestID", "DateTime", "CashBalance", "AccountCurrency", "TradeAccount", "IsFinalResponse", "NoAccountBalances", "InfoText", "TransactionId")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    CASHBALANCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTCURRENCY_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISFINALRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NOACCOUNTBALANCES_FIELD_NUMBER: _ClassVar[int]
    INFOTEXT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    DateTime: float
    CashBalance: float
    AccountCurrency: str
    TradeAccount: str
    IsFinalResponse: int
    NoAccountBalances: int
    InfoText: str
    TransactionId: str
    def __init__(self, RequestID: _Optional[int] = ..., DateTime: _Optional[float] = ..., CashBalance: _Optional[float] = ..., AccountCurrency: _Optional[str] = ..., TradeAccount: _Optional[str] = ..., IsFinalResponse: _Optional[int] = ..., NoAccountBalances: _Optional[int] = ..., InfoText: _Optional[str] = ..., TransactionId: _Optional[str] = ...) -> None: ...

class UserMessage(_message.Message):
    __slots__ = ("UserMessage", "IsPopupMessage")
    USERMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ISPOPUPMESSAGE_FIELD_NUMBER: _ClassVar[int]
    UserMessage: str
    IsPopupMessage: int
    def __init__(self, UserMessage: _Optional[str] = ..., IsPopupMessage: _Optional[int] = ...) -> None: ...

class GeneralLogMessage(_message.Message):
    __slots__ = ("MessageText",)
    MESSAGETEXT_FIELD_NUMBER: _ClassVar[int]
    MessageText: str
    def __init__(self, MessageText: _Optional[str] = ...) -> None: ...

class JournalEntryAdd(_message.Message):
    __slots__ = ("JournalEntry", "DateTime")
    JOURNALENTRY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    JournalEntry: str
    DateTime: int
    def __init__(self, JournalEntry: _Optional[str] = ..., DateTime: _Optional[int] = ...) -> None: ...

class JournalEntriesRequest(_message.Message):
    __slots__ = ("RequestID", "StartDateTime")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    StartDateTime: int
    def __init__(self, RequestID: _Optional[int] = ..., StartDateTime: _Optional[int] = ...) -> None: ...

class JournalEntriesReject(_message.Message):
    __slots__ = ("RequestID", "RejectText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ...) -> None: ...

class JournalEntryResponse(_message.Message):
    __slots__ = ("JournalEntry", "DateTime", "IsFinalResponse")
    JOURNALENTRY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    ISFINALRESPONSE_FIELD_NUMBER: _ClassVar[int]
    JournalEntry: str
    DateTime: int
    IsFinalResponse: int
    def __init__(self, JournalEntry: _Optional[str] = ..., DateTime: _Optional[int] = ..., IsFinalResponse: _Optional[int] = ...) -> None: ...

class AlertMessage(_message.Message):
    __slots__ = ("MessageText", "TradeAccount")
    MESSAGETEXT_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MessageText: str
    TradeAccount: str
    def __init__(self, MessageText: _Optional[str] = ..., TradeAccount: _Optional[str] = ...) -> None: ...

class HistoricalPriceDataRequest(_message.Message):
    __slots__ = ("RequestID", "Symbol", "Exchange", "RecordInterval", "StartDateTime", "EndDateTime", "MaxDaysToReturn", "UseZLibCompression", "RequestDividendAdjustedStockData", "Integer_1")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    RECORDINTERVAL_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    ENDDATETIME_FIELD_NUMBER: _ClassVar[int]
    MAXDAYSTORETURN_FIELD_NUMBER: _ClassVar[int]
    USEZLIBCOMPRESSION_FIELD_NUMBER: _ClassVar[int]
    REQUESTDIVIDENDADJUSTEDSTOCKDATA_FIELD_NUMBER: _ClassVar[int]
    INTEGER_1_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Symbol: str
    Exchange: str
    RecordInterval: HistoricalDataIntervalEnum
    StartDateTime: int
    EndDateTime: int
    MaxDaysToReturn: int
    UseZLibCompression: int
    RequestDividendAdjustedStockData: int
    Integer_1: int
    def __init__(self, RequestID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., RecordInterval: _Optional[_Union[HistoricalDataIntervalEnum, str]] = ..., StartDateTime: _Optional[int] = ..., EndDateTime: _Optional[int] = ..., MaxDaysToReturn: _Optional[int] = ..., UseZLibCompression: _Optional[int] = ..., RequestDividendAdjustedStockData: _Optional[int] = ..., Integer_1: _Optional[int] = ...) -> None: ...

class HistoricalPriceDataResponseHeader(_message.Message):
    __slots__ = ("RequestID", "RecordInterval", "UseZLibCompression", "NoRecordsToReturn", "IntToFloatPriceDivisor")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RECORDINTERVAL_FIELD_NUMBER: _ClassVar[int]
    USEZLIBCOMPRESSION_FIELD_NUMBER: _ClassVar[int]
    NORECORDSTORETURN_FIELD_NUMBER: _ClassVar[int]
    INTTOFLOATPRICEDIVISOR_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RecordInterval: HistoricalDataIntervalEnum
    UseZLibCompression: int
    NoRecordsToReturn: int
    IntToFloatPriceDivisor: float
    def __init__(self, RequestID: _Optional[int] = ..., RecordInterval: _Optional[_Union[HistoricalDataIntervalEnum, str]] = ..., UseZLibCompression: _Optional[int] = ..., NoRecordsToReturn: _Optional[int] = ..., IntToFloatPriceDivisor: _Optional[float] = ...) -> None: ...

class HistoricalPriceDataReject(_message.Message):
    __slots__ = ("RequestID", "RejectText", "RejectReasonCode", "RetryTimeInSeconds")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    REJECTREASONCODE_FIELD_NUMBER: _ClassVar[int]
    RETRYTIMEINSECONDS_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    RejectReasonCode: HistoricalPriceDataRejectReasonCodeEnum
    RetryTimeInSeconds: int
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ..., RejectReasonCode: _Optional[_Union[HistoricalPriceDataRejectReasonCodeEnum, str]] = ..., RetryTimeInSeconds: _Optional[int] = ...) -> None: ...

class HistoricalPriceDataRecordResponse(_message.Message):
    __slots__ = ("RequestID", "StartDateTime", "OpenPrice", "HighPrice", "LowPrice", "LastPrice", "Volume", "NumTrades", "BidVolume", "AskVolume", "IsFinalRecord")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    OPENPRICE_FIELD_NUMBER: _ClassVar[int]
    HIGHPRICE_FIELD_NUMBER: _ClassVar[int]
    LOWPRICE_FIELD_NUMBER: _ClassVar[int]
    LASTPRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    NUMTRADES_FIELD_NUMBER: _ClassVar[int]
    BIDVOLUME_FIELD_NUMBER: _ClassVar[int]
    ASKVOLUME_FIELD_NUMBER: _ClassVar[int]
    ISFINALRECORD_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    StartDateTime: int
    OpenPrice: float
    HighPrice: float
    LowPrice: float
    LastPrice: float
    Volume: float
    NumTrades: int
    BidVolume: float
    AskVolume: float
    IsFinalRecord: int
    def __init__(self, RequestID: _Optional[int] = ..., StartDateTime: _Optional[int] = ..., OpenPrice: _Optional[float] = ..., HighPrice: _Optional[float] = ..., LowPrice: _Optional[float] = ..., LastPrice: _Optional[float] = ..., Volume: _Optional[float] = ..., NumTrades: _Optional[int] = ..., BidVolume: _Optional[float] = ..., AskVolume: _Optional[float] = ..., IsFinalRecord: _Optional[int] = ...) -> None: ...

class HistoricalPriceDataTickRecordResponse(_message.Message):
    __slots__ = ("RequestID", "DateTime", "AtBidOrAsk", "Price", "Volume", "IsFinalRecord")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    ATBIDORASK_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    ISFINALRECORD_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    DateTime: float
    AtBidOrAsk: AtBidOrAskEnum
    Price: float
    Volume: float
    IsFinalRecord: int
    def __init__(self, RequestID: _Optional[int] = ..., DateTime: _Optional[float] = ..., AtBidOrAsk: _Optional[_Union[AtBidOrAskEnum, str]] = ..., Price: _Optional[float] = ..., Volume: _Optional[float] = ..., IsFinalRecord: _Optional[int] = ...) -> None: ...

class HistoricalPriceDataResponseTrailer(_message.Message):
    __slots__ = ("RequestID", "FinalRecordLastDateTime")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    FINALRECORDLASTDATETIME_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    FinalRecordLastDateTime: int
    def __init__(self, RequestID: _Optional[int] = ..., FinalRecordLastDateTime: _Optional[int] = ...) -> None: ...

class HistoricalMarketDepthDataRequest(_message.Message):
    __slots__ = ("RequestID", "Symbol", "Exchange", "StartDateTime", "EndDateTime", "UseZLibCompression", "Integer_1")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    ENDDATETIME_FIELD_NUMBER: _ClassVar[int]
    USEZLIBCOMPRESSION_FIELD_NUMBER: _ClassVar[int]
    INTEGER_1_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    Symbol: str
    Exchange: str
    StartDateTime: int
    EndDateTime: int
    UseZLibCompression: int
    Integer_1: int
    def __init__(self, RequestID: _Optional[int] = ..., Symbol: _Optional[str] = ..., Exchange: _Optional[str] = ..., StartDateTime: _Optional[int] = ..., EndDateTime: _Optional[int] = ..., UseZLibCompression: _Optional[int] = ..., Integer_1: _Optional[int] = ...) -> None: ...

class HistoricalMarketDepthDataResponseHeader(_message.Message):
    __slots__ = ("RequestID", "UseZLibCompression", "NoRecordsToReturn")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    USEZLIBCOMPRESSION_FIELD_NUMBER: _ClassVar[int]
    NORECORDSTORETURN_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    UseZLibCompression: int
    NoRecordsToReturn: int
    def __init__(self, RequestID: _Optional[int] = ..., UseZLibCompression: _Optional[int] = ..., NoRecordsToReturn: _Optional[int] = ...) -> None: ...

class HistoricalMarketDepthDataReject(_message.Message):
    __slots__ = ("RequestID", "RejectText", "RejectReasonCode")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    REJECTTEXT_FIELD_NUMBER: _ClassVar[int]
    REJECTREASONCODE_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    RejectText: str
    RejectReasonCode: HistoricalPriceDataRejectReasonCodeEnum
    def __init__(self, RequestID: _Optional[int] = ..., RejectText: _Optional[str] = ..., RejectReasonCode: _Optional[_Union[HistoricalPriceDataRejectReasonCodeEnum, str]] = ...) -> None: ...

class HistoricalMarketDepthDataRecordResponse(_message.Message):
    __slots__ = ("RequestID", "StartDateTime", "Command", "Flags", "NumOrders", "Price", "Quantity", "IsFinalRecord")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    STARTDATETIME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    NUMORDERS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ISFINALRECORD_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    StartDateTime: int
    Command: int
    Flags: int
    NumOrders: int
    Price: float
    Quantity: int
    IsFinalRecord: int
    def __init__(self, RequestID: _Optional[int] = ..., StartDateTime: _Optional[int] = ..., Command: _Optional[int] = ..., Flags: _Optional[int] = ..., NumOrders: _Optional[int] = ..., Price: _Optional[float] = ..., Quantity: _Optional[int] = ..., IsFinalRecord: _Optional[int] = ...) -> None: ...

class TradeAccountTradingIsDisabledRequest(_message.Message):
    __slots__ = ("RequestID", "TradeAccount", "SetTradingIsDisabled", "SetDisableTradingForParentAccountOnly")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SETTRADINGISDISABLED_FIELD_NUMBER: _ClassVar[int]
    SETDISABLETRADINGFORPARENTACCOUNTONLY_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TradeAccount: str
    SetTradingIsDisabled: TradingIsDisabledEnum
    SetDisableTradingForParentAccountOnly: TradingIsDisabledEnum
    def __init__(self, RequestID: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., SetTradingIsDisabled: _Optional[_Union[TradingIsDisabledEnum, str]] = ..., SetDisableTradingForParentAccountOnly: _Optional[_Union[TradingIsDisabledEnum, str]] = ...) -> None: ...

class TradeAccountTradingIsDisabledResponse(_message.Message):
    __slots__ = ("RequestID", "TradeAccount", "TradingIsDisabled", "DisableTradingForParentAccountOnly", "ErrorText")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRADEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TRADINGISDISABLED_FIELD_NUMBER: _ClassVar[int]
    DISABLETRADINGFORPARENTACCOUNTONLY_FIELD_NUMBER: _ClassVar[int]
    ERRORTEXT_FIELD_NUMBER: _ClassVar[int]
    RequestID: int
    TradeAccount: str
    TradingIsDisabled: TradingIsDisabledEnum
    DisableTradingForParentAccountOnly: TradingIsDisabledEnum
    ErrorText: str
    def __init__(self, RequestID: _Optional[int] = ..., TradeAccount: _Optional[str] = ..., TradingIsDisabled: _Optional[_Union[TradingIsDisabledEnum, str]] = ..., DisableTradingForParentAccountOnly: _Optional[_Union[TradingIsDisabledEnum, str]] = ..., ErrorText: _Optional[str] = ...) -> None: ...
