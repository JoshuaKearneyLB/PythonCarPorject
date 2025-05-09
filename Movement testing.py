from machine import Pin
import time

# Define motor pins as dictionary
motors = {
    "M1_IN1": Pin(19, Pin.OUT),
    "M1_IN2": Pin(18, Pin.OUT),
    "M2_IN1": Pin(20, Pin.OUT),
    "M2_IN2": Pin(21, Pin.OUT),
    "M3_IN1": Pin(6, Pin.OUT),
    "M3_IN2": Pin(7, Pin.OUT),
    "M4_IN1": Pin(8, Pin.OUT),
    "M4_IN2": Pin(9, Pin.OUT)
}


def stop():
    for pin in motors.values():
        pin.value(0)


def move_backword(duration):
    #To move backword set IN1=1 and IN2=0 for all motors

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
    # To move forward set IN1=0 and IN2=1 for all motors
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
    motors["M1_IN1"].value(1)
    motors["M1_IN2"].value(0)  
    motors["M2_IN1"].value(1)
    motors["M2_IN2"].value(0)
    # Right motors forward
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(0)
    motors["M4_IN2"].value(1)
    
    time.sleep(duration)
    stop()


def turn_right(duration):
    #Turn right by setting left motors forward and right motors back
    
    #Left motors forward
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)
    motors["M2_IN1"].value(0)
    motors["M2_IN2"].value(1)
    #Right motors backward
    motors["M3_IN1"].value(1)
    motors["M3_IN2"].value(0)
    motors["M4_IN1"].value(1)
    motors["M4_IN2"].value(0)
    
    time.sleep(duration)
    stop()
    
##Strafing using mecano wheels
def strafe_left(duration):
    #Strafe Right by setting right wheels inward and left wheels outward
    
    #Left motors forward
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
    
def strafe_right(duration):
    #Strafe Right by setting right wheels inward and left wheels outward
    
    #Left motors forward
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)
    motors["M2_IN1"].value(1)
    motors["M2_IN2"].value(0)
    #Right motors backward
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(1)
    motors["M4_IN2"].value(0)
    
    time.sleep(duration)
    stop()


# Run the test

strafe_right(0.3)
strafe_left(0.6)
