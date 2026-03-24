import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

right = Pin(9, Pin.IN, Pin.PULL_UP)
left = Pin(7, Pin.IN, Pin.PULL_UP)
button_reset = Pin(8, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
pos_y = 30
pos_x = 0
size_x = 4
size_y = 12
hit_dir_y = 1

b_pos_y = 34
b_pos_x = 4
b_size = 4
direction_x = 1
direction_y = hit_dir_y

enemy_pos_x = 124

delay = 0.05
oled.fill(0)
oled.fill_rect(pos_x, pos_y, size_x, size_y, 1)
oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 1)
oled.fill_rect(enemy_pos_x, b_pos_y-6, size_x, size_y, 1)

oled.show()

while True:
    
    if right() == 0:
        oled.fill_rect(pos_x, pos_y, size_x, size_y, 0)
        hit_dir_y = 0
        if pos_y <= 52:
            pos_y = pos_y + 3
        oled.fill_rect(pos_x, pos_y, size_x, size_y, 1)
        oled.show()

    if left() == 0:
        oled.fill_rect(pos_x, pos_y, size_x, size_y, 0)
        hit_dir_y = 1
        if pos_y >= -2:
            pos_y = pos_y -3
        oled.fill(0)
        oled.fill_rect(pos_x, pos_y, size_x, size_y, 1)
        oled.show()

    if direction_x == 1:
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 0)
        b_pos_x = b_pos_x + 1
        if b_pos_x >= 120:
            direction_x = 0
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 1)
        oled.show()
        
    if direction_x == 0:
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 0)
        b_pos_x = b_pos_x - 1
        if b_pos_x <= 4 and pos_y <= b_pos_y <= pos_y + size_y:
            direction_x = 1
            direction_y = hit_dir_y
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 1)
        oled.show()
    
    if direction_y == 1:
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 0)
        oled.fill_rect(enemy_pos_x, b_pos_y-6, size_x, size_y, 0)
        b_pos_y = b_pos_y - 1
        if b_pos_y <= 0:
            direction_y = 0
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 1)
        oled.fill_rect(enemy_pos_x, b_pos_y-6, size_x, size_y, 1)
        oled.show()
        
    if direction_y == 0:
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 0)
        oled.fill_rect(enemy_pos_x, b_pos_y-6, size_x, size_y, 0)
        b_pos_y = b_pos_y + 1
        if b_pos_y >= 60:
            direction_y = 1
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 1)
        oled.fill_rect(enemy_pos_x, b_pos_y-6, size_x, size_y, 1)
        oled.show()
    if b_pos_x <=3:
        oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 0)
        oled.text('You loose', 30, 20, 1)
        oled.show()
        while True:
            if button_reset() == 0:
                time.sleep(delay)
                pos_y = 30
                pos_x = 0      
                b_pos_y = 34
                b_pos_x = 4
                hit_dir_y = 1
                direction_x = 1
                direction_y = hit_dir_y
                enemy_pos_x = 124
                oled.fill(0)
                oled.fill_rect(pos_x, pos_y, size_x, size_y, 1)
                oled.fill_rect(b_pos_x, b_pos_y, b_size, b_size, 1)
                oled.fill_rect(enemy_pos_x, b_pos_y-6, size_x, size_y, 1)
                oled.show()
                break
    