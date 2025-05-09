from machine import Pin, PWM
import time



# Define motor pins as dictionary
motors = {
    "M1_IN1": Pin(19, Pin.OUT),#Motor 1 incorrectly installed so pin numbers switched
    "M1_IN2": Pin(18, Pin.OUT),
    "M2_IN1": Pin(20, Pin.OUT),
    "M2_IN2": Pin(21, Pin.OUT),
    "M3_IN1": Pin(6, Pin.OUT),
    "M3_IN2": Pin(7, Pin.OUT),
    "M4_IN1": Pin(8, Pin.OUT),
    "M4_IN2": Pin(9, Pin.OUT)
}


#-----Scanning------
def scan_process():
    servo = PWM(Pin(13))  # GPIO13 control the servo 
    servo.freq(50)  # Standard servo frequency (50Hz)
    
    i=3000
    while(i < 4900):
        servo.duty_u16(i)
        print("i=", i)
        i += 25
        time.sleep(0.05)
    
    '''
    while(i > 2100):
        servo.duty_u16(i)
        print("i=", i)
        i-=50
        time.sleep(0.1)
'''



#----Movement-------
def stop():
    for pin in motors.values():
        pin.value(0)


def move_backward(duration):
    #To move forward set IN1=1 and IN2=0 for all motors

    motors["M1_IN1"].value(1)
    motors["M1_IN2"].value(0)
    motors["M2_IN1"].value(1)
    motors["M2_IN2"].value(0)
    motors["M3_IN1"].value(1)
    motors["M3_IN2"].value(0)
    motors["M4_IN1"].value(1)
    motors["M4_IN2"].value(0)
    time.sleep(duration)
    stop()


def move_forward(duration):
    # To move backward set IN1=0 and IN2=1 for all motors
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)
    motors["M2_IN1"].value(0)
    motors["M2_IN2"].value(1)
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(0)
    motors["M4_IN2"].value(1)
    time.sleep(duration)
    stop()


def turn_left(duration):
    # Turn left by setting right motors forward and left motors back
    
    # Left motors backward
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)  
    motors["M2_IN1"].value(1)
    motors["M2_IN2"].value(0)
    # Right motors forward
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(1)
    motors["M4_IN2"].value(0)
    
    time.sleep(duration)
    stop()


def turn_right(duration):
    #Turn right by setting left motors forward and right motors back
    
    #Left motor forward
    motors["M1_IN1"].value(1)
    motors["M1_IN2"].value(0)
    motors["M2_IN1"].value(0)
    motors["M2_IN2"].value(1)
    #Right motors backward
    motors["M3_IN1"].value(1)
    motors["M3_IN2"].value(0)
    motors["M4_IN1"].value(0)
    motors["M4_IN2"].value(1)
    
    time.sleep(duration)
    stop()


# Run the test
move_backward(2)
time.sleep(3)
scan_process()
time.sleep(3)
move_forward(2)
time.sleep(1)



