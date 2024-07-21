# Satellite Scraper
Easy to use python package for scraping high-resolution satellite images from apple maps.🌎

## Examples:
Qatar Desert

![image](https://github.com/user-attachments/assets/1a170708-7e1b-4d9b-9e32-ca933f5368e3)

Michigan Forest:

![image](https://github.com/user-attachments/assets/babadade-fe91-4a98-a63d-ed24cdc6bca7)

## Features
  - Provides super high resolution satellite images of a specified area!
  - No need for any api key.

## How it Works:
  - Takes a free API key from sattelites.pro
  - Uses API key to download an array of high-res tiles from apple maps.
  - Stiches the array togehter to produce one high resolution image.

## Install:
  - ```pip install satellitescraper``` (Will require you to have chrome or a chromium based browser installed.)

## Usage:

  After installing the package, you can import it as so:
  ```
  from satellitescraper.map_fetch import *

  min_lat_deg = 25.1 
  max_lat_deg = 25.12
  min_lon_deg = 51.2
  max_lon_deg = 51.22
  zoom = 19

  map_fetch(min_lat_deg ,max_lat_deg, min_lon_deg, max_lon_deg, zoom, verbose = False, threads_= 8, container_dir = "myOutputFolder")
  ```
  To get the coordinate variables:
  - Take two points on earth you would like to make into a rectangle
  - Record the latitude and longitude of both of those points
  - Put the smallest longitude and latitude in respective variabeles
  - Put the largest longitude and latitude in respective variables
  - Choose zoom (affects resolution of tiles).

  For more detailed usage guide, checkout the documentation.
