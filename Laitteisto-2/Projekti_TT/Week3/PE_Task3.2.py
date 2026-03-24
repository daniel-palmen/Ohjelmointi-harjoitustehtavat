import time
from fifo import Fifo
from machine import UART, Pin, I2C, Timer, ADC, PWM
from ssd1306 import SSD1306_I2C

def main():       
    rot = Encoder(10, 11, 12)
    led1 = Led(22)
    led2 = Led(21)
    led3 = Led(20)
    led1.light.freq(1000)
    led2.light.freq(1000)
    led3.light.freq(1000)
    oled_width = 128
    oled_height = 64
    i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
    chooser = 0

    oled.fill(0)
    oled.text(f'LED1 - {led1.state}', 8, 0, 1)
    oled.text(f'LED2 - {led2.state}', 8, 8, 1)
    oled.text(f'LED3 - {led3.state}', 8, 16, 1)
    oled.text('[', 0, chooser * 8, 1)
    oled.text(']', 88, chooser * 8, 1)
    oled.show()

    
    while True:
        led1.light.duty_u16(int(led1.brightness * 65535 / 255))
        led2.light.duty_u16(int(led2.brightness * 65535 / 255))
        led3.light.duty_u16(int(led3.brightness * 65535 / 255))

        if rot.fifo.has_data():
            oled.text('[', 0, chooser * 8, 0)
            oled.text(']', 88, chooser * 8, 0)
            info = rot.fifo.get()
            print(info)#testi
            if info == 1:
                if chooser < 2:
                    chooser = chooser + 1
                else:
                    chooser = 2
            elif info == 2:
                if chooser > 0:
                    chooser = chooser - 1
                else:
                    chooser = 0
            elif info == 3:
                time.sleep(0.25)
                if chooser == 0:
                    if led1.brightness == 10:
                        led1.off()
                    else:
                        led1.on()
                    oled.fill_rect(8,0,80,8,0)
                    oled.text(f'LED1 - {led1.state}', 8, 0, 1)
                if chooser == 1:
                    if led2.brightness == 10:
                        led2.off()
                    else:
                        led2.on()
                    oled.fill_rect(8,8,80,8,0)
                    oled.text(f'LED2 - {led2.state}', 8, 8, 1)
                if chooser == 2:
                    if led3.brightness == 10:
                        led3.off()
                    else:
                        led3.on()
                    oled.fill_rect(8,16,80,8,0)
                    oled.text(f'LED3 - {led3.state}', 8, 16, 1)
            oled.text('[', 0, chooser * 8, 1)
            oled.text(']', 88, chooser * 8, 1)
            oled.show()

class Encoder:
    def __init__(self, rot_a, rot_b, rot_press):
        self.a = Pin(rot_a, mode = Pin.IN)
        self.b = Pin(rot_b, mode = Pin.IN)
        self.press = Pin(rot_press, mode = Pin.IN, pull = Pin.PULL_UP)
        self.fifo = Fifo(30)
        self.a.irq(handler = self.handler, trigger = Pin.IRQ_RISING, hard = True)
        self.press.irq(handler = self.handler_press, trigger = Pin.IRQ_FALLING, hard = True)

    def handler(self, pin):
        if self.b():
            self.fifo.put(2)
        elif self.a():
            self.fifo.put(1)

    def handler_press(self, pin):
        if self.press():
            self.fifo.put(3)

class Led:
    def __init__(self, pin):
        self.light = PWM(pin)
        self.brightness = 0
        self.state = 'OFF'
    def on(self):
        self.brightness = 10
        self.state = 'ON'
    def off(self):
        self.brightness = 0
        self.state = 'OFF'
main()