from filefifo import Filefifo
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

def main():
    fifo = Filefifo(10, name = 'sinewave_250Hz_02.txt') #250Hz
    i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
    button = Pin(8, Pin.IN, Pin.PULL_UP)
    oled_width = 128
    oled_height = 64
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
    oled.fill(0)
    oled.text('Task 2.2', 0, 0, 1)
    oled.text('press SW1', 0, 8, 1)
    oled.show()
    
    while True:
        if button() == 0:
            time.sleep(0.1)
            oled.fill(0)
            data_max, data_min = min_maxer(fifo) #set min and max for scaling
            scaler(fifo, data_max, data_min, oled) #scales and calls screener func
    return

def min_maxer(fifo): #reads first 2 seconds and sets max and low
    data_new = 0
    data_max = 0
    data_min = 0
    data_setter = 0
    for _ in range(250*2):
                if fifo.has_data():
                    data_new = fifo.get()
                    if data_setter == 0:
                        data_max = data_new
                        data_min = data_new
                        data_setter = 1
                    elif data_new > data_max:
                        data_max = data_new
                    elif data_new < data_min:
                        data_min = data_new
    return data_max, data_min

def scaler(fifo, data_max, data_min, oled): #scales 10s of data
    for _ in range(250*10):
        if fifo.has_data():
            data_new = fifo.get()
            data_scaled = ((data_new - data_min) / (data_max - data_min)) * (100)
            data_scaled = round(data_scaled)
            screener(data_scaled, oled) #screens data to oled
    return

def screener(data_scaled, oled): #screens data to oled
    length = round(((data_scaled - 0) / (128 - 0)) * (128))
    oled.scroll(0,-8)
    oled.fill_rect(0, 56, 128, 8, 0)
    oled.text(str(data_scaled),0,56,1)
    oled.fill_rect(24,56, length, 8, 1)
    oled.show()
    print(f'{data_scaled}')
    
    return

main()