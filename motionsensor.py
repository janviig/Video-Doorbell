import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define trigger pin
motionSensor = 17
GPIO.setup(motionSensor, GPIO.IN)

#variables from present and past 
present = 0
past = 0

try:
	print("waiting")
	while GPIO.input(motionSensor) == 1:
		present = 0

	while True:
		present = GPIO.input(motionSensor)

		#if motion is detected
		if present == 1 and past == 0:
			print("someone is at the door - motion detected ")
			#trigger to send webhook to ifttt
			trigger = requests.post('https://maker.ifttt.com/trigger/motion_detected/with/key/bmXpeKYBaYpMnyFMcQftDY', params={"value1":"none","value2":"none","value3":"none"})
			past = 1
			#waiting 10 seconds before looping again - for arguments sake, real life it would be 120 seconds
			print("Waiting 10 seconds")
			time.sleep(10)

		elif present == 0 and past == 1:
			print("ready")
			past = 0

except KeyboardInterrupt:
	GPIO.cleanup()
