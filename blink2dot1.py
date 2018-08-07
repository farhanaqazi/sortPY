#      LED to blink when a push button is NOT pressed. 
####    However, the LED should stay on continually when the push button IS pressed.


import RPi.GPIO as GPIO
import time
#setup GPIO
GPIO.setmode(GPIO.BCM)

ledPin = 23
butPin = 17

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Here we go! Press CTRL+C to exit")
try:

while True:
	#if button not pressed do something
	if GPIO.input(butPin):
		GPIO.output(ledPin,GPIO.HIGH)

	else:
		GPIO.output(ledPin,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(ledPin,GPIO.LOW)
		time.sleep(0.5)

except KeyboardInterrupt: 
	pwm.stop()
	GPIO.cleanup()

