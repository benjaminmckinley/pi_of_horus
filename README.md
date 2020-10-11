# pi_of_horus

 Application for controlling a Raspberry Pi camera and managing a collection of timelapse image files hosted on Dropbox.

 Designed to collect timelapse images from a small garden. The script itself just connects to wifi, takes a photo, and uploads the image to Dropbox. The magic timing is handled by Crontab. A guide to configuring that tool is [here](https://www.codementor.io/@gergelykovcs/how-to-run-and-schedule-python-scripts-on-raspberry-pi-n2clhe3kp).

## Details:

- This project was built to be run on a Raspberry Pi Zero W. While I do not know how well the project would run on another version of the Pi, as long as you have a WiFi dongle or WiFi enabled device it should work fine, especially on more powerful machines like the 3 or 4.

- The camera used in this build is an [Arducam for Raspberry Pi Zero Camera Module Wide Angle 160°, 1/4 Inch 5MP OV5647 Spy Camera with Flex Cable for Pi Zero and Pi Compute Module](https://www.amazon.com/dp/B07TB3CHZ3/ref=cm_sw_em_r_mt_dp_U_n3WtEb5S1FW74). Check out [Arducam's website](https://www.arducam.com/) for detailed guides on the types of cameras offered for the Pi. The wide (160°) angle made sense for the shape of the room I was trying to cover. The most important spec of the camera for me was the *total shutter* instead of a *rolling shutter*.

 ![Shutter Explanation Gif](https://www.arducam.com/wp-content/uploads/2019/11/Rolling-Shutter-and-total-shutter.gif)

 **Image from [Arducam Camera Guide](https://www.arducam.com/choose-camera-modules-raspberry-pi-jetson-nano-guide/)**

- For the scale of the project, storing a small cache of short video files through Dropbox made the most sense for ease of setup and accessibility.

## Required Installations:

-  picamera
`pip install picamera`

- dropbox
`pip install dropbox`

## Hardware:

- Raspberry Pi Zero W
- USB to micro usb cable
- USB power supply
- Pi Zero Camera (listed in detail above)
- 3D printed case
  - If you would like to use the same case shown here (or improve upon it) you can check out the model I 3D printed at my local Makerspace.

## Credentials:
- Credentials for the Dropbox API must be available and stored in a "credentials.json" file in the format of the blank file included in the repository.

## Troubleshooting:
- I had some initial issues configuring Crontab tool because of issues with relative paths, you may have to adjust your settings depending on directory structure
- Crontab does not relay output anywhere the user can see inless you pipe it into a log file
