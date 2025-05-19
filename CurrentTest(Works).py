import asyncio
import time
from machine import Pin
#This one actually works because im mint.


# Sensor pins
trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)



# Movement placeholders
def stop():
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
    for pin in motors.values():
        pin.value(0)

def move_forward():
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
        
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)
    motors["M2_IN1"].value(0)
    motors["M2_IN2"].value(1)
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(0)
    motors["M4_IN2"].value(1)

# Distance check (non-async is fine)
def get_distance():
    trigger.low()
    time.sleep_us(2)
    trigger.high()
    time.sleep_us(10)
    trigger.low()

    while echo.value() == 0:
        start = time.ticks_us()
    while echo.value() == 1:
        end = time.ticks_us()

    duration = time.ticks_diff(end, start)
    distance = duration / 58.0
    return distance

# Main logic based on your flowchart
async def main():
    while True:
        distance = get_distance()
        print("Distance:", distance, "cm")

        if distance < 30:
            stop()
            print("Object detected. Waiting 5 seconds.")
            await asyncio.sleep(5)
        else:
            move_forward()

        await asyncio.sleep(0.1)  # Tiny delay to avoid spamming CPU

# Run it
asyncio.run(main())
