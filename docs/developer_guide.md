# Developer Guide

Here we explain the internal mechanisms of the code to help future developers.

## Code Structure

## Basic rundown:

- Importing is done by ``` from satellitescraper.map_fetch import * ``` 
- (Note: map_fetch is the simplified, unified version of all the BASE functions, when anything needs to be downloaded, you call map_fetch.)
- ```map_fetch(min_lat_deg ,max_lat_deg, min_lon_deg, max_lon_deg, zoom, verbose = False, threads_= 8, container_dir = "myOutputFolder")```
- This function downloads all tiles within the minmum and maximum latitude and longitude goven to it. It also supports multi threading.
- If any feature is to be added involving downloaded tiles, map_fetch is to be used to download them, NOTHING ELSE.
- map_fetch works by callingj different functions in satellitescraper.py, sanity_checker, and tile stitcher.
- satellitescraper downloads the images, sanitychecker verifies them, and tile sticher assembles them into one big image.
- Thats Basically it!
- To Learn more about the code, go to individual files and read the comments at the top!
