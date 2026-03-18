import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

sw_0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw_2 = Pin(7, Pin.IN, Pin.PULL_UP)
sw_1 = Pin(8, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
lost = 0
pos_x = 20 #player
pos_y = 50
size = 10
jump = 15
going_up = 0
delay = 0.1
obs_x = 128 #obstacle
obs_y = 50
obs_y2 = 0
obs_height = 15
obs_width = 6
oled = SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)
"""oled.fill_rect(0, 61, 128, 2, 1) #floor"""
oled.fill_rect(pos_x, pos_y, size, size, 1) #player
oled.show()

while True:
    if sw_2() == 0: #Jump button
        going_up = 1
        pos_lock = pos_y
    if going_up == 1:
        if pos_y <= pos_lock - jump:
            going_up = 0
        else:
            oled.fill_rect(pos_x, pos_y, size, size, 0)
            pos_y = pos_y - 3
            oled.fill_rect(pos_x, pos_y, size, size, 1)
            oled.show()
    if going_up == 0 and pos_y <50:
            oled.fill_rect(pos_x, pos_y, size, size, 0)
            pos_y = pos_y + 3
            oled.fill_rect(pos_x, pos_y, size, size, 1)
            oled.show()
    oled.fill_rect(obs_x, obs_y, obs_width, obs_height, 0)
    oled.fill_rect(obs_x, obs_y2, obs_width, obs_height, 0)
    obs_x = obs_x-1
    oled.fill_rect(obs_x, obs_y, obs_width, obs_height, 1) #lower obstacle
    oled.fill_rect(obs_x, obs_y2, obs_width, obs_height, 1) #upper obstacle
    oled.show()
    if obs_x < -10:
        obs_x = 128
    if pos_y <= obs_y <= pos_y +10 or pos_y -6 <= obs_y2 <= pos_y:
        if pos_x <= obs_x <= pos_x +5:
            oled.fill(0)
            oled.text('you loose', 10, 10, 1)
            oled.show()
            lost = 1
            while lost == 1:
                if sw_1() == 0:
                    time.sleep(0.1)
                    lost = 0
    if sw_1() == 0:
        going_up = 0
        obs_x = 128 #obstacle
        obs_y = 50
        obs_y2 = 0
        oled.fill(0)
        oled.fill_rect(pos_x, pos_y, size, size, 1) #player
        oled.show()