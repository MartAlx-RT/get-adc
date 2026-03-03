import RPi.GPIO as GPIO

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def dec2bin(value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        while...
    
    def get_sc_voltage(self):
        return 
    
    def set_voltage(self, voltage):
        if(not(0.0 <= voltage <= self.dynamic_range)):
            print(f"Voltage is out of range (0.0 ... {self.dynamic_range:.2f} V)")
            print("Set zero.")
            self.set_number(0)
        else: self.set_number(int(voltage / self.dynamic_range * 255))

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.295)
               
        while True:
            try:
                voltage = float(input("Input voltage (V): "))
                dac.set_voltage(voltage)
        
            except ValueError:
                print("This is NAN, try again\n")
        
    finally:
        dac.deinit()