# 08: Vector time series: SNOTEL data for the Western U.S.

Static spatial analysis is powerful, but things often vary in time...

## Options to represent time in Python 
* https://csit.kutztown.edu/~schwesin/fall20/csc223/lectures/Pandas_Time_Series.html
* Multiple options to represent datetime objects - easy to convert

### Python `datetime`
* Built-in module called `datetime` which contains classes for `datetime` object (and `timedelta` object) - can be confusing
* https://docs.python.org/3/library/datetime.html

### NumPy `datetime64`
* https://numpy.org/doc/stable/reference/arrays.datetime.html

### Pandas `Timestamp`
* https://pandas.pydata.org/docs/user_guide/timeseries.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html
* https://pandas.pydata.org/docs/user_guide/timeseries.html#overview
* `DatetimeIndex`
* `pd.to_datetime()`
    * Accepts "int, float, str, datetime, list, tuple, 1-d array, Series, DataFrame/dict-like"

### xarray
* https://xarray.pydata.org/en/stable/user-guide/time-series.html
