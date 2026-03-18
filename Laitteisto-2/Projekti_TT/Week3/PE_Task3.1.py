import time
from fifo import Fifo
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

def main():           
    rot = Encoder(10, 11, 12)
    switch = 0
    while True:
        if rot.press() == 0:
            time.sleep(0.5)
            if switch == 0:
                switch = 1
            else:
                switch = 0
        if rot.fifo.has_data():
            if switch == 1:
                print(rot.fifo.get())
            else:
                rot.fifo.get()

class Encoder:
    def __init__(self, rot_a, rot_b, rot_press):
        self.a = Pin(rot_a, mode = Pin.IN)
        self.b = Pin(rot_b, mode = Pin.IN)
        self.press = Pin(rot_press, Pin.IN, Pin.PULL_UP)
        self.fifo = Fifo(30, typecode = 'i')
        self.a.irq(handler = self.handler, trigger = Pin.IRQ_RISING, hard = True)
        
    def handler(self, pin):
        if self.b():
            self.fifo.put(-1)
        else:
            self.fifo.put(1)

main()