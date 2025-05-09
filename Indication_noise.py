from machine import Pin
import time

#Buzzer works on GPIO2
buzzer = Pin(2, Pin.OUT)  

while True:
    buzzer.value(1)  # Noise on
    time.sleep(0.25)
    buzzer.value(0)  # Noise off
    
