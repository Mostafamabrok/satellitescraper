# User Guide

Here, we cover all the information needed to effectively use satellitescrpaer.

## Installation 

### Prerequisites
- Python 3.7+
- Pip
- Chromium based browser on $PATH

### Instalation Using Pip

```
pip install satellitescraper
```

## Usage:

### Basic Usage
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