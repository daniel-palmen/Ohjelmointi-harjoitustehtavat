from fifo import Fifo
from machine import ADC, Pin
from piotimer import Piotimer
from led import Led
import micropython

class isr_adc:
    def __init__(self, adc_pin_nr, led_pin_nr):
        self.av = ADC(adc_pin_nr)
        self.led = Led(led_pin_nr)
        self.fifo = Fifo(500)
        self.factor = 0.85
        self.led.off()
        self.ppi = 0 #yksi väli
        self.MS_IN_MINUTE = 60000
    def handler(self, tid):
        self.fifo.put(self.av.read_u16())
    def calculate_threshold(self):
        min_val = min(self.fifo.data)
        max_val = max(self.fifo.data)
        h = max_val-min_val
        threshold = min_val + self.factor * h
        return int(threshold)
    def calculate_hr(self):
        ppi_ms = self.ppi * 4
        hr = int(self.MS_IN_MINUTE / ppi_ms)
        return hr
    
class Encoder:
    def __init__(self, rot_a, rot_b, rot_press):
        self.a = Pin(rot_a, mode = Pin.IN)
        self.b = Pin(rot_b, mode = Pin.IN)
        self.press = Pin(rot_press, Pin.IN, Pin.PULL_UP)
        self.fifo = Fifo(30, typecode = 'i')
        self.a.irq(handler = self.handler, trigger = Pin.IRQ_RISING, hard = True)
        
    def handler(self, pin):
        if self.b():
            self.fifo.put(-1)
        else:
            self.fifo.put(1)


micropython.alloc_emergency_exception_buf(200)
adc_pin_nr = 27
led_pin_nr = 22
sample_rate = 250
fifo_counter = 0
passed_th = False
first_peak_found = False
prev_value = 0
peak_found = False
rot = Encoder(10, 11, 12)

ia = isr_adc(adc_pin_nr, led_pin_nr)
tmr = Piotimer(mode = Piotimer.PERIODIC, freq = sample_rate, callback = ia.handler)

#init threshold
#while fifo_counter < sample_rate * 2:
#    if not ia.fifo.empty():
#        value = ia.fifo.get()
#        fifo_counter += 1

th = ia.calculate_threshold()
#fifo_counter = 0

while True:
    if not ia.fifo.empty():
        value = ia.fifo.get()
        #print(value, th)
        fifo_counter += 1
        ia.ppi += 1
        if fifo_counter >= sample_rate:
            th = ia.calculate_threshold()
            fifo_counter = 0
        
        if value > th: #yli rajan
            if passed_th == False: #ensimmäinen ylitys
                ia.led.on()
                passed_th = True
            if not peak_found:
                if prev_value >= value:
                    hr = ia.calculate_hr()
                    if hr < 240 and hr > 30:
                        print(hr)
                    peak_found = True
                    ia.ppi = 0
                
        else: #alle rajan
            if passed_th == True:
                ia.led.off()
                passed_th = False
                peak_found = False

        prev_value = value
        if not rot.fifo.empty():
            ia.factor = ia.factor - rot.fifo.get() * 0.01
            print(f'factor changed to {ia.factor}')

#lisää liukuva keskiarvo ja rajat hr muutokselle ja ehkä hr muutoksen raja