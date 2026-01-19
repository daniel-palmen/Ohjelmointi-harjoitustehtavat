from machine import Pin, ADC
import time

pot = ADC(Pin(27))
led = Pin("LED", Pin.OUT)

conversion_factor = 1/65535

while True:
    analog = pot.read_u16() * conversion_factor
    print(analog)
    time.sleep(analog)
    led.on()
    time.sleep(analog)
    led.off()