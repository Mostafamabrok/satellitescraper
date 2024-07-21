import os
import glob
import shutil
from satellitescraper import map_api, sanity_check, stitch_whole_tile


def map_fetch(min_lat_deg ,max_lat_deg, min_lon_deg, max_lon_deg, zoom, verbose = False, threads_= 8, container_dir = "myOutputFolder"):

    download_obj = map_api(min_lat_deg = min_lat_deg,
                      max_lat_deg = max_lat_deg,
                      min_lon_deg = min_lon_deg,
                      max_lon_deg = max_lon_deg,
                      zoom = zoom,
                      verbose = False,
                      threads_ = threads_, 
                      container_dir = container_dir)

# If you don't have Chrome and can't take advantage of the auto access key fetch, set
# a.ac_key = ACCESS_KEY_STRING
# here

# If you just need the image tiles without the road place info, set this to false.
    download_obj.download(getMasks = False)

# create the object of class satellitescraper api
    sanity_obj = map_api(min_lat_deg = min_lat_deg,
                      max_lat_deg = max_lat_deg,
                      min_lon_deg = min_lon_deg,
                      max_lon_deg = max_lon_deg,
                      zoom = zoom,
                      verbose = False,
                      threads_ = threads_, 
                      container_dir = container_dir)

    sanity_check(min_lat_deg = min_lat_deg,
                max_lat_deg = max_lat_deg,
                min_lon_deg = min_lon_deg,
                max_lon_deg = max_lon_deg,
                zoom = zoom,
                verbose = False,
                threads_ = threads_, 
                container_dir = container_dir)

    print("Cleaning up... hold on")

    sqlite_temp_files = glob.glob('*.sqlite*')



# update_stitcher_db(container_dir)
# get_bbox_lat_lon()
    stitch_whole_tile(save_name="QATAR", folder_name=container_dir)


    
    for item in sqlite_temp_files:
        os.remove(item)



## Try to remove tree; if failed show an error using try...except on screen
    try:
        chromdriver_folders = glob.glob('[0-9]*')
        for item in chromdriver_folders:
            shutil.rmtree(item)
            
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
