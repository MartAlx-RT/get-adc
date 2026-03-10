import time
import mcp3021_driver
import adc_plot

mcp = MCP3021(3.292)    # dynamic range
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
            voltage.append(mcp.get_voltage())
            time_v.append(t)
            #print(f"Измеренное напряжение: {voltage:.4f} В")
            #time.sleep(0.1)  # pause
            t = time.time()-start_time
        
        adc_plot.plot_voltage_vs_time(time_v, voltage, 3.5)
        adc_plot.plot_sampling_period_hist(ts)

    finally:
        mcp.deinit()
