# 07: Reprojection, Clipping, Sampling, Zonal Stats 

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

This week, we are going to revisit rasters. We will cover common operations and strategies, including reprojection, clipping, sampling strategies, zonal statistics, and creating rasters from unstructured point data.

## Reading and Tutorials
Please take some time to review the following material (especially if you have limited GIS experience), and come with questions on topics that are unclear, so we can discuss together.  There is some overlap in content, but different presentation of the essential material, so hopefully one or more will work for you:

### Raster clipping
* https://autogis-site.readthedocs.io/en/latest/notebooks/Raster/clipping-raster.html
* https://rasterio.readthedocs.io/en/latest/topics/masking-by-shapefile.html

### Raster Reprojection
* https://gdal.org/programs/gdalwarp.html 

### Raster resampling/interpolation 
* https://rasterio.readthedocs.io/en/latest/topics/resampling.html#resampling-methods
* https://support.esri.com/en/technical-article/000008915

### Points to raster 
* https://www.earthdatascience.org/courses/use-data-open-source-python/data-stories/what-is-lidar-data/lidar-points-to-pixels-raster/

### Sampling a raster at points
* https://github.com/uw-cryo/raster_sampling

### Sampling a raster for polygons: zonal statistics
* https://pythonhosted.org/rasterstats/
* https://autogis-site.readthedocs.io/en/latest/notebooks/Raster/zonal-statistics.html
* https://pysal.org/scipy2019-intermediate-gds/deterministic/gds2-rasters.html