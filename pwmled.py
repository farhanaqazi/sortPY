#pwmled.py
#farhan Qazi

# PWM LED Brightness Control program
#Connect an LED to your Raspberry Pi and write a program to 
#gradually #increase brightness, and then gradually decrease 
#brightness. The exact rate #of increase and decrease is not 
#critical but let it take at least one second #to go from 
#maximum to minimum brightness

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
p= GPIO.PWM(18, 50)
p.start(0)
print("Led Now Fades!")
try:
    while True:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100, 0, -1):
            p.ChangeDutyCycle(i)
            time.sleep(0.02)
except KeyboardInterrupt:
	pass
p.stop()

print("End of program!")

GPIO.cleanup() 
