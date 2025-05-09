from Machine import Pin, PWM
import time
import _thread
from Ultrasound_sensor import get_distance
from servo_scan import scan_process

# ========== Motor Setup ==========
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

def move_forward():
    motors["M1_IN1"].value(0)
    motors["M1_IN2"].value(1)
    motors["M2_IN1"].value(0)
    motors["M2_IN2"].value(1)
    motors["M3_IN1"].value(0)
    motors["M3_IN2"].value(1)
    motors["M4_IN1"].value(0)
    motors["M4_IN2"].value(1)

def stop():
    for pin in motors.values():
        pin.value(0)

# ========== Thread 1: Move Forward ==========
def drive_loop():
    while True:
        move_forward()
        time.sleep(0.05)

# ========== Thread 2: Sweep Servo ==========
def scan_loop():
    scan_servo()  # Calls your existing sweep function

# ========== Thread 3: Monitor Distance ==========
def safety_loop():
    while True:
        dist = get_distance()
        print("Distance:", dist)
        if dist < 30:
            print("Obstacle detected. Stopping car.")
            stop()
            break
        time.sleep(0.1)

# ========== Run Threads ==========
_thread.start_new_thread(drive_loop, ())
_thread.start_new_thread(scan_loop, ())
_thread.start_new_thread(safety_loop, ())

# Keep main thread alive
while True:
    time.sleep(1)
