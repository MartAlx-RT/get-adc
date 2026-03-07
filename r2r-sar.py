import time
import r2r_adc
import adc_plot

adc = r2r_adc.R2R_ADC(3.292, 0.0001)
voltage = []
time_v = []
ts = []
duration = 3.0

start_time = 0
t = 0

if __name__ == "__main__":
    try:
        start_time = time.time()
        t = 0

        while (t < duration):
            ts.append(t)
            voltage.append(adc.get_sar_voltage())
            time_v.append(t)
            t = time.time()-start_time
        
        adc_plot.plot_voltage_vs_time(time_v, voltage, 3.5)
        adc_plot.plot_sampling_period_hist(ts)

    finally:
        adc.deinit()
