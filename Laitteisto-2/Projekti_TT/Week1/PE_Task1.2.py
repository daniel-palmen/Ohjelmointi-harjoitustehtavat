import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
row = 0

oled.fill(0)

while True:
    user_input = input()
    oled.text(user_input,0,row,1)
    oled.show()
    row = row + 8
    if row >= 64:
        oled.scroll(0,-8)
        row = 56
        oled.fill_rect(0, 56, 128, 8, 0)