#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPin1 = 19 #Green
ledPin2 = 20 #Blue 
ledPin3 = 21 #White 

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)

with open('led-pwm.txt', 'r') as f:
data = json.load(f)

pwm1 = GPIO.PWM(ledPin1, 100) # PWM object on our pin at 100 Hz
pwm2 = GPIO.PWM(ledPin2, 100)
pwm3 = GPIO.PWM(ledPin3, 100)
pwm1.start(0) # start with LED off
pwm2.start(0)
pwm3.start(0)

while True:
  with open("led-pwm.txt", 'r') as f:
    if data['LED Green']
    dutyCycle = float(f.read()) # read duty cycle value from file
  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
