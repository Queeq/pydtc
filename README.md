# Data and Trading Communications (DTC) Protocol

This is a very basic realization of [DTC protocol](http://dtcprotocol.org) in Python

## Limitations

* Only client mode is supported.
* Only historical data download is supported for now.
* Supported encoding is limited to Google Protobuf.
* Partial data download is possible by specifying start date. Date range or end date is not supported.
* Tested only on Linux with local Sierra Chart DTC server.


## Installation and usage

You can install directly from Github:

```
pip install git+https://github.com/Queeq/pydtc
```

Import `dtc_download` function to your project and use returned `pydtc.datadefs.MktDataEntry` objects directly or together with `vars()` to convert it to dictionary.

Here's an example on how to save data into Pandas DataFrame:

```python
import pandas as pd
from pydtc import dtc_download

data = dtc_download("BTC-BSTMP", start_date="01.01.2018")

# Beware that the first yielded object is a header that contains
# information about exchange, symbol and record interval
# as reported by a DTC server

header = next(data)
print(header)

df = pd.DataFrame(vars(entry) for entry in data)
print(df)
```

`dtc_download()` accepts the following arguments:

    symbol (str): symbol, the only mandatory option
    exchange (str): exchange (default "Bitcoin")
    start_date (Union[str, int]): date in any format
        (default "01.01.1970)
    server (tuple[str, int]): IP and port of the DTC server
        (default ("127.0.0.1", 11101))
    debug (bool): toggle very verbose logging (all messages will be shown)
        (default False)

For debug messages to show up it may be necessary to enable debug logging in the calling script, for example:
```python
logging.basicConfig(format='{asctime} {name} {threadName} {levelname}: {message}', style='{', level=logging.DEBUG)
```
