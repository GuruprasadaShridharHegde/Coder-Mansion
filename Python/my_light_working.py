#!/usr/local/bin/python
from gpiozero import LightSensor, Buzzer
from time import sleep

ldr = LightSensor(4)  # alter if using a different pin
buzzer = Buzzer(17)

while True:
    sleep(0.1)
    if ldr.value < 0.9==0:
        buzzer.off()
        print('Farmland Secure')
    else:
        buzzer.on()
        print('Intrusion Alert')



