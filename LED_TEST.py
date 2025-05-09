##Test Script for led
##Ensures car is connected and accepting python files

from machine import Pin
import time

led = Pin("LED", Pin.OUT)
# Choose any motor control pin

while True:
    led.value(1)
    time.sleep(0.25)
    led.value(0)
    time.sleep(0.25)