# 08: Vector spatiotemporal analysis - trajectories, SNOTEL met stations, correlation

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

## Overview
Static spatial analysis is powerful, but most interesting processes vary in time, with varying spatial and temporal correlation.

This week we will explore the time dimension for vector data. We will use Pandas/GeoPandas to explore analysis approaches for 4D trajectories (x,y,z,t) and time series from spatially distributed networks of meteorological stations. We will also explore some simple spatial interpolation approaches to convert vector data to raster data. If there is time, we will briefly touch on geostatistics and some options for more advanced spatiotemporal analysis.

## Working with temporal data in Python 
* https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
* https://csit.kutztown.edu/~schwesin/fall20/csc223/lectures/Pandas_Time_Series.html

### Pandas resources
* https://pandas.pydata.org/docs/user_guide/timeseries.html
* https://pandas.pydata.org/docs/user_guide/timeseries.html#overview

### xarray
* https://xarray.pydata.org/en/stable/user-guide/time-series.html

## Spatial interpolation
* 1D vs. 2D interpolation
* https://docs.scipy.org/doc/scipy/tutorial/interpolate.html  

## Correlation

### Independent time series correlation
* https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

### Spatial autocorrelation
* Variograms and kriging
* https://geostat-framework.readthedocs.io/projects/gstools/en/stable/
* http://darribas.org/gds15/content/labs/lab_06.html 
* http://darribas.org/gds_scipy16/ipynb_md/04_esda.html