""" Common useful classes and functions for inclusion elsewhere """

import datetime as dt
from dateutil.parser import parse as parse_date
import threading
import time as t
from tqdm import tqdm
from typing import Union


class Progress(tqdm):
    """ Progress bar based on `tqdm` with different defaults"""

    def __init__(self, *args, unit_scale=True, miniters=1, mininterval=0.5, **kwargs):
        """ Original __init__ with different defaults
        Returns:
            Decorated iterator
        """
        super().__init__(*args, unit_scale=unit_scale, miniters=miniters, mininterval=mininterval, **kwargs)


class InterruptibleThread(threading.Thread):
    """ Thread that could be signalled to stop
    Attributes:
        event(threading.Event): Event class used for controlled sleeping
        running (bool): flag controlling if the main thread loop must be running
    """

    def __init__(self):
        super().__init__()
        self.event = threading.Event()
        self.running = True

    def run(self):
        """ This is an example run function that could be interrupted in the middle of waiting """
        while self.running:
            # Do something here
            self.event.wait(10)

    def stop(self):
        """ Break the loop within run() by setting self.running to False, thus stopping the thread """
        self.running = False
        self.event.set()  # Awake the thread from sleep to stop immediately


def now():
    """
    Returns:
        int: Current timestamp
    """
    return int(t.time())


def dt_tstamp(dt_obj):
    """
    Args:
        dt_obj (dt.datetime): datetime.datetime object
    Returns:
        int: timestamp
    """
    return int(dt_obj.strftime('%s'))


def str_to_tstamp(time_value):
    """ Convert date string to timestamp
    Args:
        time_value (Union[str, int]): date string in any format supported by dateutils.parser.parse
    Returns:
        int: timestamp
    """
    if type(time_value) is int:
        # If we got int - consider it being timestamp already
        return time_value
    else:
        return dt_tstamp(parse_date(time_value))

