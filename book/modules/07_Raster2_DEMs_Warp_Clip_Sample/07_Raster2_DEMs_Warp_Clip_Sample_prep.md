# 07: Raster 2 - Reprojection, Clipping, Sampling, Zonal Stats 

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

## Overview
This week, we are going to revisit rasters. We will cover common operations and strategies, including reprojection, clipping, sampling, zonal statistics, and creating rasters from unstructured point data.

## Reading and Tutorials
Please take some time to review the following material (especially if you have limited GIS experience), and come with questions on topics that are unclear, so we can discuss together.  There is some overlap in content, but different presentation of the essential material, so hopefully one or more will work for you:

### rioxarray
We will dive into `xarray` in a few weeks, but we will introduce some raster processing and analysis concepts using `rioxarray` this week. It will be useful to have a general understanding of these two packages from the high-level "quick overview" docs:
* https://docs.xarray.dev/en/stable/getting-started-guide/why-xarray.html
* https://corteva.github.io/rioxarray/stable/getting_started/getting_started.html

### Raster Reprojection
* GDAL: https://gdal.org/programs/gdalwarp.html 
* rasterio: https://rasterio.readthedocs.io/en/latest/topics/reproject.html
* rioxarray: https://corteva.github.io/rioxarray/stable/examples/reproject.html (much closer to the geopandas `to_crs()` method)
  * reproject_match: https://corteva.github.io/rioxarray/stable/examples/reproject_match.html (very useful for comparing two rasters)

### Raster clipping/masking
* Using rasterio:
  * https://autogis-site.readthedocs.io/en/2021/notebooks/Raster/clipping-raster.html
  * https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html
* Using rioxarray:
  * https://corteva.github.io/rioxarray/stable/examples/clip_geom.html

### Raster resampling/interpolation 
* https://rasterio.readthedocs.io/en/latest/topics/resampling.html#resampling-methods
* https://support.esri.com/en/technical-article/000008915

### Sampling a raster over polygon areas: zonal statistics
* https://pythonhosted.org/rasterstats/
* https://autogis-site.readthedocs.io/en/2021/notebooks/Raster/zonal-statistics.html
* https://pysal.org/scipy2019-intermediate-gds/deterministic/gds2-rasters.html#zonal-statistics

### Sampling a raster at points
* https://github.com/uw-cryo/raster_sampling

### Gridding points to raster 
* https://www.earthdatascience.org/courses/use-data-open-source-python/data-stories/what-is-lidar-data/lidar-points-to-pixels-raster/
* We will revisit point interpolation and gridding in Lab08

### Useful examples of basic raster processing
* https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/raster-data-processing/
  * Nice examples of raster reprojection, clipping, subtraction and export
