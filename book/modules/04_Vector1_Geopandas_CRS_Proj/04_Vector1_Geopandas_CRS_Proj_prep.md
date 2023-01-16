# Introduction

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean  

This week, please finish the Lab03 exercises, then follow the [student weekly workflow](../../resources/students/student_weekly_workflow.md) to submit on Github (make sure to switch to `%matplotlib inline` and rerun to embed figures!), then submit the url on the Canvas assignment page before the deadline.

Also, please review information about the course [Final Project](../../resources/project/README.md):  
* Start thinking about potential project ideas you might want to explore
* Come prepared on Friday to share an idea or two during breakouts with other students (no commitment expected, just brainstorm)

## Overview
This week, we are going to cover several fundamental geospatial data concepts, including coordinate reference systems (CRS), projections/transformations, and basic vector geometry definitions (points, lines, polygons). We will also begin using the GeoPandas package (https://geopandas.readthedocs.io/en/latest/) for further analysis of the ICESat point dataset.

>“GeoPandas is an open source project to make working with geospatial data in python easier. GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types. Geometric operations are performed by shapely. Geopandas further depends on fiona for file access and descartes and matplotlib for plotting.”

We will revisit vector data and cover more advanced processing, analysis and visualization in a few weeks.

## Reading and Tutorials
Please take some time before lab on Friday to review some of the following material (especially important if you have limited GIS experience), and come with questions on topics that are unclear, so we can discuss together. There is some overlap in content, but they offer different presentations of essential material, so hopefully one or more will work for you, and some repetition will help solidify.

* [Data Carpentry Introduction to Geospatial Concepts](https://datacarpentry.org/organization-geospatial/):
    * Section 2: Introduction to Vector Data (~10 min)
    * Section 3: Coordinate Reference Systems (~15 min)
* [Vector Geohackweek tutorial](https://geohackweek.github.io/vector/): first 4 sections (~30-45 min)
    * Introduction
    * Geospatial Concepts
    * Encodings, Formats and Libraries
    * GeoPandas Introduction
    * *Note: If you prefer an instructor explaining, here is a recording of this tutorial by Emilio Mayorga:* https://www.youtube.com/watch?v=t3PMTnhl1eY&feature=youtu.be
* [Earth Lab Intermediate Earth Data Science Textbook](https://www.earthdatascience.org/courses/use-data-open-source-python/intro-vector-data-python/spatial-data-vector-shapefiles/intro-to-coordinate-reference-systems-python/)
    * Section 2, Chapter 2: all sections (~30-60 min)
        * Can review on website or download data for interactive exploration
        * Lesson 1. GIS in Python: Introduction to Vector Format Spatial Data - Points, Lines and Polygons
        * Lesson 2. GIS in Python: Intro to Coordinate Reference Systems in Python
        * Lesson 3. Geographic vs projected coordinate reference systems - GIS in Python
        * Lesson 4. Understand EPSG, WKT and Other CRS Definition Styles

## Other Resources

### Official documentation:
* GeoPandas: http://geopandas.org/index.html
* Shapely: https://shapely.readthedocs.io/en/stable/manual.html

### Other good resources:
* https://automating-gis-processes.github.io/site/lessons/L1/Intro-Python-GIS.html
* https://automating-gis-processes.github.io/site/lessons/L2/overview.html
* https://github.com/Automating-GIS-processes/CSC/blob/master/source/notebooks/L1/geometric-objects.ipynb
* http://darribas.org/gds15/content/labs/lab_03.html
* https://geohackweek.github.io/visualization/03-cartopy/
* https://www.w3.org/2015/spatial/wiki/Coordinate_Reference_Systems
* https://github.com/geopandas/geopandas/tree/master/examples
