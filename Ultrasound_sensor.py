from machine import Pin
import time

#This program uses us or microseconds for more precise timings
trig = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
buzzer = Pin(2, Pin.OUT)

def get_distance():
    #send trigger signal
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    
    while echo.value() == 0:
        start = time.ticks_us()
    
    while echo.value() == 1:
        end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    distance = (duration * 0.0343) / 2
    #0.0343 is defined by speed of sound through air in cm/microsecond
    return distance

while True:
    distance = get_distance()
    if(distance <= 40):
        buzzer.value(1)
        time.sleep(0.0045)
        buzzer.value(0)
    else:
        print("Distance: ", distance, " cm")
    time.sleep(0.01)
    
        
        

