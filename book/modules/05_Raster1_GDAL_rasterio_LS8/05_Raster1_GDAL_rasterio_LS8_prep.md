# 05: Raster Fundamentals: GDAL, rasterio, Landsat-8

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

## Overview
This week, we are going to cover raster basics.  We will introduce and use `gdal` and `rasterio` to process, analyze and visualize Landsat-8 satellite images over Washington state.

## Reading and Tutorials
Please review the following material (especially if you have limited GIS or remote sensing experience), and come to lecture/lab with questions on topics that are unclear, so we can discuss together.  There is some overlap in content, but different presentation of the essential material, so hopefully one or more will work for you:

### Raster fundamentals
* ESRI Documentation (~15-30 min)
    * https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/what-is-raster-data.htm
    * https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/cell-size-of-raster-data.htm
    * https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/raster-bands.htm
* Data Carpentry Introduction to Raster Data (~15 min)
    * https://datacarpentry.org/organization-geospatial/01-intro-raster-data/index.html

### Landsat and multispectral imagery background
* Intro and history: https://en.wikipedia.org/wiki/Landsat_program
* Landsat-8 Overview: https://landsat.gsfc.nasa.gov/landsat-8/landsat-8-overview
* EarthLab Section 5: https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/. Required chapters (can skim on web, not required to try interactive):
    * Chapter 7: Introduction to Multispectral Remote Sensing Data in Python
    * Chapter 9: Work with Landsat Remote Sensing Data in Python
    * Chapter 11: Calculate Vegetation Indices in Python

### Rasterio
* Quickstart: https://rasterio.readthedocs.io/en/latest/quickstart.html
* Automating GIS Processes
    * [Reading raster files with Rasterio](https://autogis-site.readthedocs.io/en/latest/notebooks/Raster/reading-raster.html)
    * [Visualizing raster layers](https://autogis-site.readthedocs.io/en/latest/notebooks/Raster/plotting-raster.html)
    * [Masking / clipping raster](https://autogis-site.readthedocs.io/en/latest/notebooks/Raster/clipping-raster.html)
    * [Raster map algebra](https://autogis-site.readthedocs.io/en/latest/notebooks/Raster/raster-map-algebra.html)

### GDAL
* Quickstart: https://live.osgeo.org/en/quickstart/gdal_quickstart.html
    * Only the GDAL sections (not OGR) 
* Part 4 of Rob Simmons' "A Gentle Introduction to GDAL": https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-4-working-with-satellite-data-d3835b5e2971
* Optional:
    * https://github.com/dwtkns/gdal-cheat-sheet#raster-operations
    * https://developers.planet.com/planetschool/getting-started-with-gdal/
    * Parts 1 and 2 of Rob Simmons' "A Gentle Introduction to GDAL":
        * https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-1-a3253eb96082
        * https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-2-map-projections-gdalwarp-e05173bd710a

### Other resources (optional)
* GeoHackWeek: https://geohackweek.github.io/raster/
* EarthLab Section 3: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-raster-data-python/fundamentals-raster-data/
    * Note: The EarthLab material recently migrated from `rasterio` to `rioxarray` for raster processing in PYthon. We will start with `rasterio`, then come back to `xarray` and `rioxarray` later in the quarter.
