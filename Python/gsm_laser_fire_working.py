#!/usr/local/bin/python
import serial
import os, time
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
from gpiozero import LightSensor
import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(0.400)
from time import sleep

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
ldr = LightSensor(4)  # gpio 4
   # GPIO 17

GPIO.setup(27, GPIO.IN)

port.write(b'AT\r')
rcv = port.read(10)
print(rcv)
time.sleep(1)

try:
    while True:
        if ((GPIO.input(27))==False) and ((ldr.value < 0.9)==False):
            buzzer.on()
            print('intrusion and smoke')
            print('laser,smoke sending sms')
            port.write(b"AT+CMGF=1\r")
            print("Text Mode Enabled…")
            time.sleep(3)
            port.write(b'AT+CMGS="9482152447"\r')
            msg = "Laser and smoke Alert!!!"
                      #print("sending message….")
            time.sleep(3)
            port.reset_output_buffer()
            time.sleep(1)
            port.write(str.encode(msg+chr(26)))
            time.sleep(3)
            print("message sent for Intrusion and smoke Alert")
        
        
        elif (GPIO.input(27))==False:
            #buzzer.on()
            print('Fire Detected, sending sms')
            port.write(b"AT+CMGF=1\r")
            print("Text Mode Enabled…")
            time.sleep(3)
            port.write(b'AT+CMGS="9482152447"\r')
            msg = "fire detected"
                  #print("sending message….")
            time.sleep(3)
            port.reset_output_buffer()
            time.sleep(1)
            port.write(str.encode(msg+chr(26)))
            time.sleep(3)
            print("message sent and Intrusion Alert")
            pygame.mixer.music.load("04.wav")
            pygame.mixer.music.play()
            #buzzer.on()
            
        elif (ldr.value < 0.9)==False:
            #buzzer.on()
            print('intrusion')
            print('laser, sending sms')
            port.write(b"AT+CMGF=1\r")
            print("Text Mode Enabled…")
            time.sleep(3)
            port.write(b'AT+CMGS="9482152447"\r')
            msg = "Laser intervention Alert!!!"
                      #print("sending message….")
            time.sleep(3)
            port.reset_output_buffer()
            time.sleep(1)
            port.write(str.encode(msg+chr(26)))
            time.sleep(3)
            pygame.mixer.music.load("03.wav")
            pygame.mixer.music.play()
            print("message sent and Intrusion Alert")
            
            
        
            
        else:
            #buzzer.off()
            print('farmaland secure')
            
        sleep(1)
        
finally:
    GPIO.cleanup()

