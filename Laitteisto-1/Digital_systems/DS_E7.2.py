from machine import pin
import time

class alarmsyst:
    def __init__(self, delay):
        self.delay = delay
        self.button = Pin(7, Pin.IN, Pin.PULL_UP)
        self.alarm = Pin(9, Pin.IN, Pin.PULL_UP)
        self.lamp = Pin(22, Pin.OUT)
        self.siren = Pin(20, Pin.OUT)
        self.state = self.off
    
    def off(self):
        self.lamp.off()
        self.siren.off()
        time.sleep(self.delay)
        if self.alarm() == 0:
            self.state = self.on
    
    def on(self):
        self.lamp.on()
        self.siren.on()
        time.sleep(self.delay)
        if self.button() == 0:
            if self.alarm() == 1:
                self.state = self.off
            else:
                self.state = self.on_A1
        if self.button() == 1:
            if self.alarm() == 0:
                self.state = self.on_B
                
    def on_A1(self):
        self.siren.off()
        self.lamp.on()
        time.sleep(self.delay)
        if self.alarm() == 0:
            self.state = self.on_A1
        else:
            self.state = self.off
    
    def on_A2(self):
        self.siren.off()
        self.lamp.off()
        time.sleep(self.delay)
        self.state = self.on_A1
    
    def on_B(self):
        self.siren.off()
        self.lamp.on()
        time.sleep(self.delay)
        if self.button() == 0:
            self.state = self.off