import PCF8591 as ADC
from pynput.mouse import Button, Controller
import time

mouse = Controller()

def setup():
    ADC.setup(0x48)                    # Setup PCF8591
    global state

def angle(x, y):
    if x - 125 < 15 and x - 125 > -15 and y - 125 < 15 and y - 125 > -15:
        return "home"
    if y == 125:
        y = 127     # there are a little error with my device.
    x -= 127
    y -= 127

    return [x/64,y/64]
setup()
while True:
    a = angle(ADC.read(0), ADC.read(1))
    if a!="home":
        mouse.move(a[0], a[1])