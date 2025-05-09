import machine
import neopixel
import time

num_leds = 8  
led_pin = 16

# Must create neopixel object 
leds = neopixel.NeoPixel(machine.Pin(led_pin), num_leds)


def set_color(r, g, b):
    for i in range(num_leds):
        leds[i] = (r, g, b)  
    leds.write()  

#Turn off
def clear_leds():
    set_color(0, 0, 0)  

def neo_test():
    for i in range(15):
        for i in range(num_leds):
            leds[i] = (255, 0, 0)
            leds.write()
        time.sleep(0.5)
        
        for i in range(num_leds):
            leds[i] = (0, 0 , 255)
            leds.write()
        time.sleep(0.5)
        
    for i in range(num_leds):
            leds[i] = (0, 0 , 0)
            leds.write()
            
        
        

