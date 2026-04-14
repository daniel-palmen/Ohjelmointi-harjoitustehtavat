from filefifo import Filefifo

def main():
    rate = 250
    fifo = Filefifo(10, name='hr_capture03_250Hz.txt')
    wanted = 200
    results = 0
    sample_counter = 0
    last_peak_sample = -1000
    min_interval = int(0.3 * rate)
    THRESHOLD = 34000
    bpm = 0
    sum_bpm = 0
    data_B = fifo.get()
    data_A = fifo.get()

    while results < wanted:
        data_new = fifo.get()
        sample_counter += 1
        is_peak = (
            data_A > data_B and
            data_A > data_new and
            data_A > THRESHOLD and
            (sample_counter - last_peak_sample) > min_interval
        )
        if is_peak:
            if last_peak_sample > 0:
                interval = sample_counter - last_peak_sample
                sum_bpm = sum_bpm + ((rate / interval) * 60)
                results += 1
                if results % 10 == 0:
                    bpm = sum_bpm/10
                    print(f'Heart rate: {bpm:.0f} bpm')
                    sum_bpm = 0
            last_peak_sample = sample_counter
        data_B = data_A
        data_A = data_new

main()