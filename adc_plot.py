import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    manager = plt.get_current_fig_manager()
    manager.resize(1280, 960)
    plt.plot(time, voltage, 'o')
    plt.plot(time, voltage)
    plt.show()
