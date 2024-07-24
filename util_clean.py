import os
import shutil
import glob

temp_sqlite_files = glob.glob("*.sqlite")

print("Cleaning space for development...")

shutil.rmtree("myOutputFolder")

print("Output folder deleted.")

for file in temp_sqlite_files:
	os.remove(file)

print("Temporary sqlite files removed.")

for file in os.listdir():
	if '.png' in file:
		os.remove(file)

print("Downloaded images deleted.")

print("\nAll Done.")
