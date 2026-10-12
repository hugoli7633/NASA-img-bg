import requests
import os
import ctypes
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote

# Directory to save the downloaded images (absolute path)
# A drive other than C: is recommended, e.g. r'D:\NASA_APOD'. Do NOT use the Startup folder
save_dir = os.path.join(os.path.expanduser('~'), 'Pictures', 'NASA_APOD')

# RSS feed of NASA Astronomy Picture of the Day
# (api.nasa.gov/planetary/apod now returns the NASA logo instead of the picture, so use the feed)
url = 'https://science.nasa.gov/feed/apod-basic/'

# Send the request and get the response
response = requests.get(url, timeout=30)
response.raise_for_status()
root = ET.fromstring(response.content)

# The feed lists recent APODs, newest first. Some days are videos, so take the newest image
image_url = None
for item in root.iter('item'):
    hdurl = item.findtext('{https://science.nasa.gov/apod/}hdurl')
    if hdurl and urlparse(hdurl).path.lower().endswith(('.jpg', '.jpeg', '.png')):
        # hdurl points to a resized copy, use the original file instead
        image_url = hdurl.split('?')[0].replace('/dynamicimage/assets/science/', '/content/dam/science/')
        break

if image_url is None:
    raise SystemExit('No APOD image found in the feed')

# Get the filename of the image from the URL
os.makedirs(save_dir, exist_ok=True)
filename = os.path.join(save_dir, unquote(os.path.basename(urlparse(image_url).path)))

# Download the image from the URL and save it to save_dir
response = requests.get(image_url, timeout=120)
response.raise_for_status()
with open(filename, 'wb') as f:
    f.write(response.content)

# Path to the downloaded image
image_path = os.path.abspath(filename)

# Set the wallpaper
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
