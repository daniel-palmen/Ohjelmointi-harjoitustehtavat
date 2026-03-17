import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

sw_0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw_2 = Pin(7, Pin.IN, Pin.PULL_UP)
sw_1 = Pin(8, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
pos_x = 20 #player
pos_y = 50
size = 10
jump = 18
going_up = 0
delay = 0.1
obs_x = 128 #obstacle
obs_y = 50
oled = SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)
oled.fill_rect(0, 61, 128, 2, 1) #floor
oled.fill_rect(pos_x, pos_y, size, size, 1) #player
oled.show()

while True:
    if sw_2() == 0 and pos_y == 50: #Jump button
        going_up = 1
    if going_up == 1:
        if pos_y <= 50 - jump:
            going_up = 0
        else:
            oled.fill_rect(pos_x, pos_y, size, size, 0)
            pos_y = pos_y - 1
            oled.fill_rect(pos_x, pos_y, size, size, 1)
            oled.show()
    if going_up == 0 and pos_y <50:
            oled.fill_rect(pos_x, pos_y, size, size, 0)
            pos_y = pos_y + 1
            oled.fill_rect(pos_x, pos_y, size, size, 1)
            oled.show()
    oled.fill_rect(obs_x, obs_y, size, size, 0)
    obs_x = obs_x-1
    oled.fill_rect(obs_x, obs_y, size, size, 1) #obstacle
    oled.show()
    if obs_x < -10:
        obs_x = 128
    if pos_y <= obs_y <= pos_y +10 and pos_x <= obs_x <= pos_x +5:
        oled.fill(0)
        oled.text('you loose', 10, 10, 1)
        oled.show()
    if sw_1() == 0:
        going_up = 0
        obs_x = 128 #obstacle
        obs_y = 50
        oled.fill(0)
        oled.fill_rect(0, 61, 128, 2, 1) #floor
        oled.fill_rect(pos_x, pos_y, size, size, 1) #player
        oled.show()