from machine import Pin
import time

class Lampsyst:
    def __init__(self, delay):
        self.delay = delay
        self.lamp = Pin(20, Pin.OUT)
        self.button = Pin(7, Pin.IN, Pin.PULL_UP)
        self.state = self.off
    
    def off(self):
        self.lamp.off()
        time.sleep(self.delay)
        if self.button() == 0:
            self.state = self.onw
            
    def onw(self):
        self.lamp.on()
        time.sleep(self.delay)
        if self.button() == 1:
            self.state = self.on
            
    def on(self):
        self.lamp.on()
        time.sleep(self.delay)
        if self.button() == 0:
            self.state = self.offn
            
    def offn(self):
        self.lamp.off()
        time.sleep(self.delay)
        if self.button() == 1:
            self.state = self.off
            
asm = Lampsyst(0.05)
while True:
    asm.state()