# pi_of_horus
 Application for controlling a Raspberry Pi camera and managing a collection of video files hosted on Google Drive.

## Details:

- This project was built to be run on a Raspberry Pi Zero W. While I do not know how well the project would run on another version of the Pi, as long as you have a WiFi dongle or WiFi enabled device it should work fine, especially on more powerful machines like the 3 or 4.

- The camera used in this build is an [Arducam for Raspberry Pi Zero Camera Module Wide Angle 160°, 1/4 Inch 5MP OV5647 Spy Camera with Flex Cable for Pi Zero and Pi Compute Module](https://www.amazon.com/dp/B07TB3CHZ3/ref=cm_sw_em_r_mt_dp_U_n3WtEb5S1FW74). Check out [Arducam's website](https://www.arducam.com/) for detailed guides on the types of cameras offered for the Pi. The wide (160°) angle made sense for the shape of the room I was trying to cover. The most important spec of the camera for me was the *total shutter* instead of a *rolling shutter*.
 - [Shutter Explanation Gif](https://www.arducam.com/wp-content/uploads/2019/11/Rolling-Shutter-and-total-shutter.gif)

- For the scale of the project, storing a small cache of short video files through Google Drive made the most sense for ease of setup and accessibility.

## Required Installations:

- pydrive

''pip install pydrive''

-  picamera

''pip install picamera''


## Hardware:

- Raspberry Pi Zero W
- USB to micro usb cable
- Power supply
- 3D printed case
  - If you would like to use the same case shown here (or improve upon it) you can check out the model I 3D printed at my local Makerspace.
