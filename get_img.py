import requests
import os
import ctypes
import subprocess

# API key for NASA
api_key = 'YOUR_API_KEY'

# URL for NASA Image of the Day API
url = 'https://api.nasa.gov/planetary/apod'

# Parameters for the API request
params = {
    'api_key': api_key,
    'hd': True  # Download high-definition image if available
}







# Send the API request and get the response
response = requests.get(url, params=params)

# Get the URL of the image from the API response
image_url = response.json()['hdurl']

# Get the filename of the image from the URL
filename = os.path.basename(image_url)

# Download the image from the URL and save it to the current directory
with open(filename, 'wb') as f:
    response = requests.get(image_url)
    f.write(response.content)

# Path to the downloaded image
image_path = os.path.abspath(filename)

# Set the wallpaper
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

subprocess.call('TASKKILL /F /PID ' + str(os.getpid()), shell=True)


