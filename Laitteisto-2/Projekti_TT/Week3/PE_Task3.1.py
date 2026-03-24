import time
from fifo import Fifo
from machine import UART, Pin, I2C, Timer, ADC, PWM
from ssd1306 import SSD1306_I2C

def main():
    rot = Encoder(10, 11, 12)
    led = Led(22)
    led.light.freq(1000)
    fade_step = 1
    switch = 0
    while True:
        led.light.duty_u16(int(led.brightness * 65535 / 255))
        if rot.press() == 0:
            time.sleep(0.5)
            if switch == 0:
                switch = 1
                led.brightness = led.memory
            else:
                switch = 0
                led.memory = led.brightness
                led.brightness = 0
        if rot.fifo.has_data():
            if switch == 1:
                if led.brightness < 0:
                    led.brightness = 0
                elif led.brightness > 50:
                    led.brightness = 50
                elif 0 <= led.brightness <= 50:
                    change = rot.fifo.get()
                    if led.brightness == 0 and change == -1:
                        led.brightness = 0
                    else:
                        led.brightness = led.brightness + (fade_step * change)
                print(led.brightness)
                
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
        elif self.a():
            self.fifo.put(1)

class Led:
    def __init__(self, pin):
        self.light = PWM(pin)
        self.brightness = 0
        self.memory = 0

main()