import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10, 6))
    plt.xlim(0, 3)
    plt.ylim(0, max_voltage)
    plt.xlabel("time, s")
    plt.ylabel("voltage, V")

    #print(time)
    #print(voltage)

    plt.plot(time, voltage, 'o')
    plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.5)
    plt.minorticks_on()
    plt.grid(visible=True, which='minor', color='#666666', linestyle=':', alpha=0.2)
    #plt.plot(time, voltage)
    plt.show()

def plot_sampling_period_hist(time):
    plt.figure(figsize=(10,6))
    plt.hist(time)
    plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.5)
    plt.minorticks_on()
    plt.grid(visible=True, which='minor', color='#666666', linestyle=':', alpha=0.2)
    plt.show()