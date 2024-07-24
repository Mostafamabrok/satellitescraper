import os
import glob
import shutil
from satellitescraper.map_fetch import *

min_lat_deg = 34.677511
max_lat_deg = 34.705105
min_lon_deg = 135.18681
max_lon_deg = 135.213118
zoom = 19

map_fetch(min_lat_deg ,max_lat_deg, min_lon_deg, max_lon_deg, zoom, verbose = False, threads_= 8, container_dir = "myOutputFolder")
