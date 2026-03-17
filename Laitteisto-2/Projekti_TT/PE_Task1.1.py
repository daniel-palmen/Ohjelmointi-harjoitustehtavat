import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

button_R = Pin(9, Pin.IN, Pin.PULL_UP)
button_L = Pin(7, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
position = 52
delay = 0.05
oled.fill(0)
oled.text('<=>', position, 54, 1)
oled.show()

while True:
    if button_R() == 0:
        time.sleep(delay)
        if position < 105:
            position = position + 1
        oled.fill(0)
        oled.text('<=>', position, 54, 1)
        oled.show()
        
    if button_L() == 0:
        time.sleep(delay)
        if position >= 0:
            position = position - 1
        oled.fill(0)
        oled.text('<=>', position, 54, 1)
        oled.show()