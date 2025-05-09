from machine import Pin, PWM
import time


def scan_process():
    servo = PWM(Pin(13))  # GPIO13 control the servo 
    servo.freq(50)  # Standard servo frequency (50Hz)
    i = 3100
    servo.duty_u16(i)
    #scan left
    while(i < 4500):
        servo.duty_u16(i)
        print("i=", i)
        i += 400
        time.sleep(0.5)
    #scan right
    while(i > 1500):
        servo.duty_u16(i)
        print("i=", i)
        i -= 400
        time.sleep(0.5) 

scan_process()

