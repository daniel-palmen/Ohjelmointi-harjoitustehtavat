from filefifo import Filefifo
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

def main():
    fifo = Filefifo(10, name = 'sinewave_250Hz_03.txt') #250Hz
    threshold = thresholder(fifo)
    print(threshold)
    frequency = freq_finder(fifo, threshold)
    print(frequency)
    return

def thresholder(fifo): #reads first 2 seconds and sets threshold
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
    threshold = int((data_max + data_min)/2)
    print(data_max,data_min)
    return threshold

def freq_finder(fifo, threshold):
    counter = 0
    first = 0
    frequency = 0
    times = 0
    for _ in range(250*2):
            if fifo.has_data():
                data_new = fifo.get()
                if first = 1:
                    counter = counter + 1
                if data_new < threshold:
                    going up = 1
                elif going up == 1 and data_new > theshold:
                    if first = 1:
                    times = times + 1
                    else:
                        first = 1
    
    return frequency

main()