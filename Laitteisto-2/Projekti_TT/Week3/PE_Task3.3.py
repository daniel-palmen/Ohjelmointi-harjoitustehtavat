import time
from fifo import Fifo
from filefifo import Filefifo
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

def main():
    rot = Encoder(10, 11, 12)
    oled_width = 128
    oled_height = 64
    i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
    
    low = 0
    high = 128
    new_value = 0
    
    oled.fill(0)
    data_max, data_min = min_maxer()
    scaler(data_max, data_min, oled, low, high)
    oled.show()
    
    while True:
        if rot.fifo.has_data():
            value = rot.fifo.get()
            print(value)
            if value == 1:
                low = low + 1
                high = high + 1
                if high <= 1000:
                    new_value = high
                    adder(new_value, oled, data_min, data_max)
                    oled.scroll(-1, 0)
                elif high > 1000:
                    low = 871
                    high = 1000
            else:
                low = low - 1
                high = high - 1
                if low > 0:
                    new_value = low
                    adder_b(new_value, oled, data_min, data_max)
                    oled.scroll(1, 0)
                elif low <= 0:
                    low = 0
                    high = 128
            oled.show()

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
            
def min_maxer(): #reads first 10s seconds and sets max and low
    data_new = 0
    data_max = 0
    data_min = 0
    data_setter = 0
    text_file = Filefifo(10, name = 'week3_data.txt')
    for _ in range(1000):
                if text_file.has_data():
                    data_new = text_file.get()
                    if data_setter == 0:
                        data_max = data_new + 1
                        data_min = data_new
                        data_setter = 1
                    elif data_new > data_max:
                        data_max = data_new
                    elif data_new < data_min:
                        data_min = data_new                   
    return data_max, data_min

def scaler(data_max, data_min, oled, low, high): #scales 10s of data
    placer = 0
    text_file = Filefifo(10, name = 'week3_data.txt')
    for i in range(low, high):
        if text_file.has_data():
            data_new = text_file.get()
            data_scaled = ((data_new - data_min) / (data_max - data_min)) * (62)
            data_scaled = round(data_scaled)
            placer = screener(data_scaled, oled, placer) #screens data to oled
    return

def screener(data_scaled, oled, placer): #screens data to oled
    oled.fill_rect(placer, data_scaled, 2, 2, 1)
    placer = placer + 1
    return placer

def adder(new_value, oled, data_min, data_max):
    placer = 126
    text_file = Filefifo(10, name = 'week3_data.txt')
    for i in range(0, new_value):
        if text_file.has_data():
            data_new = text_file.get()
    data_scaled = ((data_new - data_min) / (data_max - data_min)) * (62)
    data_scaled = round(data_scaled)
    print(new_value)
    print(data_new)
    oled.fill_rect(126, 0, 2, 64, 0)
    placer = screener(data_scaled, oled, placer) #screens data to oled
    return

def adder_b(new_value, oled, data_min, data_max):
    placer = 0
    text_file = Filefifo(10, name = 'week3_data.txt')
    for i in range(0, new_value):
        if text_file.has_data():
            data_new = text_file.get()
    data_scaled = ((data_new - data_min) / (data_max - data_min)) * (62)
    data_scaled = round(data_scaled)
    print(new_value)
    print(data_new)
    oled.fill_rect(0, 0, 2, 64, 0)
    placer = screener(data_scaled, oled, placer) #screens data to oled
    
    return

main()