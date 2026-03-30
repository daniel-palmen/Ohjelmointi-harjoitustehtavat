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
            print(f'Threshold: {threshold}')
            oled.text(f'Threshold:{threshold}', 0, 0, 1)
            frequency = round(freq_finder(fifo, threshold), 2)
            print(f'Frequency:{frequency}Hz')
            oled.text(f'Frequency:{frequency}Hz', 0, 8, 1)
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

def freq_finder(fifo, threshold):
    frequency = 0
    counter_av = 0
    start = 0 #finds the first ever upwards crossing of threshold
    sample_count = 0
    current_location = 0 #0 under the threshold 1 over threshold
    for i in range(250*10):
        if fifo.has_data():
            data_new = fifo.get()
            
    
    
    #sampling rate of 250 / average count of samples between upwards crossings
    frequnecy = 250 / (counter_av)
    return frequency

main()