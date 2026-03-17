import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

button_down = Pin(9, Pin.IN, Pin.PULL_UP)
button_up = Pin(7, Pin.IN, Pin.PULL_UP)
button_reset = Pin(8, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
pos_y = 30
pos_x = 0
size = 4
delay = 0.05
oled.fill(0)
oled.fill_rect(pos_x, pos_y, size, size, 1)
oled.show()

while True:
    if pos_x >= 124:
        pos_x = 0
    if button_up() == 0:
        time.sleep(delay)
        pos_x = pos_x + 1
        if pos_y > 0:
            pos_y = pos_y - 1
        oled.fill_rect(pos_x, pos_y, size, size, 1)
        oled.show()
        
    if button_down() == 0:
        time.sleep(delay)
        pos_x = pos_x + 1
        if pos_y < 60:
            pos_y = pos_y + 1
        oled.fill_rect(pos_x, pos_y, size, size, 1)
        oled.show()
    
    if button_reset() == 0:
        time.sleep(delay)
        pos_x = 0
        pos_y = 30
        oled.fill(0)
        oled.show()
        time.sleep(delay*4)
        oled.fill_rect(pos_x, pos_y, size, size, 1)
        oled.show()
        
    if button_up() == 1 and button_down() == 1:
        time.sleep(delay)
        pos_x = pos_x + 1
        oled.fill_rect(pos_x, pos_y, size, size, 1)
        oled.show()