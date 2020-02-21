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

def formatTimestamp():
    timestamp = datetime.datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def main():
    for x in range(2) : # just 5 calls over 2 minutes
        photo_name = formatTimestamp()



        upload(dbx, "zebra.jpeg", "/" + photo_name + ".jpeg")
        sleep(30)


if __name__ == '__main__':
    main()
