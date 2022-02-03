# Open Data for Projects

This is a dynamic list of data sources that might be useful for projects. It is by no means exhaustive or complete, but includes many catalogs that contain hundreds of independent data products, many hosted in the cloud with code/tutorials for easy access.

If you find others that should be included here, please open a PR to add or send me a note.

## Public data catalogs in the cloud
* https://registry.opendata.aws/
* https://cloud.google.com/storage/docs/public-datasets
* https://developers.google.com/earth-engine/datasets

## Google Earth Engine
* https://earthengine.google.com/
* https://developers.google.com/earth-engine/datasets (different than Google Cloud public datasets)
* https://github.com/giswqs/geemap - interactive GEE analysis and visualization in a Jupyter notebook using Python API (a nice alternative to the standard javascript IDE)

## Lidar
* USGS 3DEP LidarExplorer: https://prd-tnm.s3.amazonaws.com/LidarExplorer/index.html#/
  * Possible to select a rectangular area, then process on the fly for download
  * Can also use website interface to prepare a PDAL pipeline (https://pdal.io/) that can be run on the hub for on-demand data processing.
* OpenTopography: https://opentopography.org/
  * Lidar and Global DEM with on-demand processing and API
* WA DNR Lidar portal: https://lidarportal.dnr.wa.gov/
  * Note that you can select and download subsets of these data products. But all products hosted by WA DNR use WA state plane coordinate systems with horizontal and vertical units of feet, so extra steps to integrate with other datasets using standard units of meters.

## Sample high-resolution imagery
* Planet PlanetScope (~3 m GSD, 4 bands).  They have edu and research program that allows you to sign up for an account that enables access their Explorer interface and API, with a limited quota to download sample imagery: https://www.planet.com/markets/education-and-research/
* NAIP for 1-m tiled orthoimages, RGB and in some cases NIR.  Here's info about WA: https://geo.wa.gov/datasets/785aa8e8876c4b8b9ed54e9816fb02c4
* Maxar/DigitalGlobe releases some data to the public: 
  * https://www.maxar.com/open-data/
  * https://www.maxar.com/product-samples
* Spacenet hosts competitions using sample data for various locations around the world: https://registry.opendata.aws/spacenet/

## Rivers
* Global River Widths from Landsat (GRWL) Database: https://zenodo.org/record/1297434
* River Surface Reflectance Database (RiverSR): https://zenodo.org/record/4304567#.X86aQGhKiUk

## Seattle Geospatial Data
* https://data-seattlecitygis.opendata.arcgis.com/
* https://www.seattle.gov/utilities/services/gis/frequently-requested-data

## Washington State Geospatial Data
* https://geo.wa.gov/
* https://www.wsdot.wa.gov/mapsdata/geodatacatalog/
* https://ecology.wa.gov/Research-Data/Data-resources/Geographic-Information-Systems-GIS

## Federal Geospatial Data
* https://catalog.data.gov/dataset?metadata_type=geospatial
* https://www.nps.gov/subjects/gisandmapping/tools-and-data.htm
