from filefifo import Filefifo
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

def main():
    fifo = Filefifo(10, name = 'sinewave_250Hz_03.txt') #250Hz
    i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
    button = Pin(8, Pin.IN, Pin.PULL_UP)
    oled_width = 128
    oled_height = 64
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
    oled.fill(0)
    oled.text('Task 2.3', 0, 0, 1)
    oled.text('press SW1', 0, 8, 1)
    oled.show()
    while True:
        if button() == 0:
            time.sleep(0.1)
            oled.fill(0)
            threshold = thresholder(fifo)
            print(f'threshold: {threshold}')
            oled.text(f'threshold:{threshold}', 0, 0, 1)
            frequency = round(freq_finder(fifo, threshold), 3)
            print(f'frequency:{frequency}s')
            oled.text(f'frequency:{frequency}s', 0, 8, 1)
            oled.show()
    return

def thresholder(fifo): #reads first 2 seconds and sets threshold
    data_new = 0
    data_max = 0
    data_min = 0
    data_setter = 0
    for i in range(250*2):
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
    threshold = int((data_max + data_min)/2)
    return threshold

def freq_finder(fifo, threshold): #fix this shit
    counter = 0
    first = 0
    frequency = 0
    times = 0
    going_up = 0
    for i in range(250*10):
        if fifo.has_data():
            data_new = fifo.get()
            if data_new < threshold:
                going_up = 1
            if going_up == 1 and data_new > threshold:
                if first == 0:
                    first = 1

    '''
    for i in range(250*10):
            if fifo.has_data():
                data_new = fifo.get()
                if first == 1:
                    counter = counter + 1
                if data_new < threshold:
                    going_up = 1
                    if first == 1:
                        first = 0
                elif going_up == 1 and data_new > threshold:
                    going_up = 0
                    if first == 1:
                        times = times + 1
                    else:
                        first = 1
    frequency = (counter / times) / 250
    '''
    return frequency

main()