from filefifo import Filefifo

def main():
    heart_rate = 0
    row = 0
    fifo = Filefifo(10, name = 'hr_capture03_250Hz.txt')
    row = file_reader(fifo, row)
    print(f'this is rows: {row}')

def file_reader(fifo, row): #read 10 sec of data
    data_new = 0
    data_max = 0
    data_min = 0
    data_setter = 0
    counter = 0
    times = 0
    going_up = 0
    frequency = 0
    for i in range(250*10):
        if fifo.has_data():
            data_new = fifo.get()
            if row < 250:
                threshold, data_min, data_max, data_setter = thresholder(data_new, data_min, data_max, data_setter) #calculates threshold
            elif row > 250:
                threshold, data_min, data_max, data_setter = thresholder(data_new, data_min, data_max, data_setter) #calculates threshold
                heart_rate = heart_rater(data_new, threshold, going_up, times, counter)
            if frequency != 0 and row % 250 == 0:
                print(f'this is freq: {frequency}')
        row = row + 1
    print('test1')
    return row

def thresholder(data_new, data_min, data_max, data_setter):
    if data_setter == 0:
        data_max = data_new
        data_min = data_new
        data_setter = 1
    elif data_new > data_max:
        data_max = data_new
    elif data_new < data_min:
        data_min = data_new
    threshold = int((data_max + data_min)/2)
    return threshold, data_min, data_max, data_setter

def heart_rater(data_new, threshold, going_up, times, counter):
    if data_new < threshold:
        going_up = 1
        times = 1
    elif data_new > threshold:
        going_up = 0
    
        
    return heart_rate

main()