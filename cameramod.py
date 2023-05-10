from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#def camera module, resolution, frame
cammod = PiCamera()
cammod.resolution = (640, 480)
cammod.framerate = 24
rawCapture = PiRGBArray(cammod, size=(640, 480))

# allow the camera to warmup
time.sleep(2)

for frame in cammod.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    #heading of the footage pop up
    cv2.imshow("video doorbell footage", image)
    keyboardButton = cv2.waitKey(1) & 0xFF

    #clear
    rawCapture.truncate(0)