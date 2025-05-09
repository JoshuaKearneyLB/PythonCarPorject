import uasyncio as asyncio
from machine import Pin, PWM
import time

# Setup pins
#servo = PWM(Pin(13))
#servo.freq(50)
trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)

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

# Function to control servo

async def scan():
    while True:
        for angle in range(30, 120, 10):
            duty = int(500 + (angle / 180) * 2000)
            servo.duty_u16(int(duty * 65535 / 20000))
            await asyncio.sleep(0.1)
        await asyncio.sleep(0.5)

# Function to move forward
async def move_forward():
    # To move forward set IN1=0 and IN2=1 for all motors
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)
    motors["M2_IN1"].value(0)
    motors["M2_IN2"].value(1)
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(0)
    motors["M4_IN2"].value(1)
    while True:
        await asyncio.sleep(1)

# Function to check distance
async def check_distance():
    while True:
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

        print("Distance:", distance, "cm")
        if (distance < 30):
            stop()
            
        await asyncio.sleep(0.01)

# Main event loop
async def main():
    await asyncio.gather(
        move_forward(),
        check_distance()
    )

asyncio.run(main())
