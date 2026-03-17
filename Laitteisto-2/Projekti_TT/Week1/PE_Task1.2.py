import time
import machine
import ssd1306

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)
oled.text('test',0,0,1)
oled.scroll(1)
oled.text('test 2',0,0,1)