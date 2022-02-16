import os
import pathlib
import random
import requests
import schedule
import subprocess
import time

WALLPAPER_FOLDER = 'wallpapers'
SET_WALLPAPER_OSASCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "{}"
end tell
END"""


files = os.listdir(WALLPAPER_FOLDER)

## rebuilds arrays

fileType = '.png'
newFiles = []

for i in range(1, files.__len__()):
	 newFiles.append(str(i) + fileType)

files = newFiles

## start

while True:
	for imagePos in files:
		full_image_path = os.path.join(
		pathlib.Path().absolute(),
		WALLPAPER_FOLDER,
		imagePos
	)
		subprocess.Popen(SET_WALLPAPER_OSASCRIPT.format(full_image_path), shell=True)
		time.sleep(.25)