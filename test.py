import os
import glob
import shutil
from satellitescraper.map_fetch import *

min_lat_deg = 25.1
max_lat_deg = 25.12
min_lon_deg = 51.2
max_lon_deg = 51.22
zoom = 19

map_fetch(min_lat_deg ,max_lat_deg, min_lon_deg, max_lon_deg, zoom, verbose = False, threads_= 8, container_dir = "myOutputFolder")