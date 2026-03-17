from filefifo import Filefifo
import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
fifo = Filefifo(10, name = 'sinewave_250Hz_01.txt')
button = Pin(8, Pin.IN, Pin.PULL_UP)
true = True
dataA = 0
dataB = 0
slope2 = 0
time = 0
cum_time = 0
first = 0
three = 0
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text('Task 2.1', 0, 0, 1)
oled.text('press SW1', 0, 8, 1)
oled.show()

while true:
    if button() == 0:
        for _ in range(1000):
            if fifo.has_data():
                dataB = dataA
                dataA = fifo.get()
                time = time + 1
                if dataA > 10000:
                    slope1 = dataA - dataB
                    if slope2 >= 0 and slope1 <= 0 and time >= 10:
                        if first == 0:
                            first = 1
                            print(dataA)
                        else:
                            print(f'samples: {time}')
                            time = time/250
                            cum_time = cum_time + time
                            print(f'time: {time}s')
                            print(dataA)
                            three = three + 1
                        time = 0
                    slope2 = slope1
            if three >= 3:
                frequency = 1/(cum_time/3)
                print(f'\nFrequency: {frequency}Hz')
                true = False
                break
