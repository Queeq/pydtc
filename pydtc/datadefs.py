""" Defines common data structures and complex types """

from datetime import datetime
from typing import TypeVar, List, Generator, Tuple


class MktDataEntry:
    """ Market data structure
    Attributes:
        time (datetime): datetime object for time
        o (float): open price
        h (float): high price
        l (float): low price
        c (float): close price
        vol (float): volume
        tcount (int): number of trades
        bidv (float): bid volume
        askv (float): ask volume
    """
    def __init__(self, time, o, h, l, c, vol, tcount, bidv, askv):
        """
        Args:
            time (datetime): datetime object for time
            o (float): open price
            h (float): high price
            l (float): low price
            c (float): close price
            vol (float): volume
            tcount (int): number of trades
            bidv (float): bid volume
            askv (float): ask volume
        """
        self.time = time
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.vol = vol
        self.tcount = tcount
        self.bidv = bidv
        self.askv = askv


# Market data types
MktData = TypeVar("MktData", Generator[MktDataEntry, None, None], List[MktDataEntry], Tuple[MktDataEntry])
