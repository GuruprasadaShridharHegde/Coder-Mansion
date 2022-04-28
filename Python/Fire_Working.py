from gpiozero import Buzzer
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
buzzer = Buzzer(17)

try:
    while True:
        if GPIO.input(27):
            buzzer.off()
            print('No Fire')
        else:
            buzzer.on()
            print('Fire Detected, sending sms')
        sleep(1)
finally:
    GPIO.cleanup()