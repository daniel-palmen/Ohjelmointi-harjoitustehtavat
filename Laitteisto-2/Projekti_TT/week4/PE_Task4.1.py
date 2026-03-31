from filefifo import Filefifo

def main():
    rate = 250
    fifo = Filefifo(10, name = 'hr_capture03_250Hz.txt')
    wanted = 20
    first = 0
    start_count = 0
    sum_count = 0
    nro_results = 0
    if fifo.has_data():
        data_A = fifo.get()
        data_B = fifo.get()
    
    while nro_results < wanted:
        
        for i in range(rate):
            if fifo.has_data():
                data_new = fifo.get()
                if start_count == 1:
                    sum_count += 1
                if data_new < data_A and data_B < data_A:
                    if first == 0:
                        start_count = 1
                        first = 1
                    if first == 1:
                        print(f'data_B{data_B} data_A{data_A} data_B{data_B} sum_count{sum_count}')
                        
                        print(f'heartrate{heartrate}')
                        nro_results += 1
                        first = 0
                        sum_count = 0
                data_B = data_A
                data_A = data_new
                    
main()