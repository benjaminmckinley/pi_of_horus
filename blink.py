# Script is responsible for taking a single capture, connecting the raspi to wifi, and uploading the photo #
# Automatically turns off camera/wifi for power conservation #
from picamera import PiCamera
import dropbox
from time import sleep
import datetime
import json
import os

ABS_PATH = "/home/horus/pi_of_horus/" # path to directory so that all paths are absolute
DROPBOX_UPLOAD_PATH = "/"
PHOTO_DIR = "photos/"

# Get Dropbox Credentials from "credentials.json"
with open(ABS_PATH + 'credentials.json') as file:
        data = json.load(file)
        TOKEN = data["ACCESS_TOKEN"]

dbx = dropbox.Dropbox(TOKEN)

# Function Definitions #
def upload(dbx, filepath, upload_path):
        with open(filepath, 'rb') as file:
                data = file.read()
        dbx.files_upload(data, upload_path)

def wifi_on():
    cmd = 'ifconfig wlan0 up'
    os.system(cmd)
    print("WiFi connection on [o]")

def wifi_off():
    cmd = 'ifconfig wlan0 down'
    os.system(cmd)
    print("WiFi connection off [-]")

# Check if there are unuploaded photos and return photo name if exists or false if none
def upload_pic_cache():
    for file in os.listdir(ABS_PATH + PHOTO_DIR):
        if file.endswith(".jpeg"):
            try: # using try-except because do not want to delete file if we cannot upload
                photo_path = ABS_PATH + PHOTO_DIR + file
                upload(dbx, photo_path, DROPBOX_UPLOAD_PATH + file) # upload file
                os.remove(photo_path) # remove file after upload
            except:
                print("Error uploading to Dropbox -- cancelling processing")

# Format current time into string going to seconds place
def formatTimestamp():
        timestamp = datetime.datetime.now()
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def main():

        wifi_on()

    # Start and Format Camera Settings
        camera = PiCamera() # new camera object
        camera.resolution = (1024, 768)
        camera.start_preview()
        sleep(2) # Camera warm-up time

    # Take and Upload Photo
        photo_name = formatTimestamp() + ".jpeg"
        photo_path = ABS_PATH + PHOTO_DIR + photo_name
        camera.capture(photo_path) # take photo

    # Try and upload all files in "photos" folder, remove as uploaded successfully
        upload_pic_cache()

        wifi_off()


if __name__ == '__main__':
        main()
