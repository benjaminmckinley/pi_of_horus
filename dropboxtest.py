from picamera import PiCamera
import dropbox
from time import sleep
import datetime
import json

# Get Dropbox Credentials from "credentials.json"
with open('credentials.json') as file:
	data = json.load(file)
	TOKEN = data["ACCESS_TOKEN"]

dbx = dropbox.Dropbox(TOKEN)

# Function Definitions #
def upload(dbx, filepath, upload_path):
	with open(filepath, 'rb') as file:
        	data = file.read()
	dbx.files_upload(data, upload_path)

# Format current time into string going to seconds place
def formatTimestamp():
	timestamp = datetime.datetime.now()
	return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def main():
	# Start and Format Camera Settings
	camera = PiCamera() # new camera object
	camera.resolution = (1024, 768)
	camera.start_preview()
	sleep(2) # Camera warm-up time

	for x in range(3) : # limit calls for now
		photo_name = formatTimestamp() + ".jpeg"
		photo_path = "/photos/" + photo_name
		camera.capture(photo_path) # take photo
		upload(dbx, photo_path, "/" + photo_name) # upload file
		sleep(25)

if __name__ == '__main__':
	main()
