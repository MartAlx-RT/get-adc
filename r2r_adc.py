import RPi.GPIO as GPIO
import time

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
    
    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, self.dec2bin(number))

    def sequential_counting_adc(self):
        max_value = 2**8 - 1  # 8bit

        for value in range(max_value + 1):
            self.number_to_dac(value)       
            time.sleep(self.compare_time)   
            comparator_output = GPIO.input(self.comp_gpio)  
                
            if self.verbose:
                voltage = value / max_value * self.dynamic_range
                print(f"Код: {value}, Напряжение: {voltage:.3f} В")

            if comparator_output == 1: # shiiit!
                return value

        return max_value

    def get_sar_voltage(self):
        result = 0
        curent_bit = 7

        while(curent_bit >= 0):
            cmp = GPIO.input(self.comp_gpio)

            if(cmp > 0):
                result -= (1 << curent_bit)
            else:
                result += (1 << curent_bit)
            if result >= 256:
                result = 255
            if result < 0:
                result = 0

            curent_bit -= 1

            self.number_to_dac(result)
            time.sleep(self.compare_time)

        return result * self.dynamic_range/255


    def get_sc_voltage(self):
            digital_value = self.sequential_counting_adc() 

            n_bits = len(self.bits_gpio)
            max_value = 2**n_bits - 1

            voltage = digital_value / max_value * self.dynamic_range 

            if self.verbose:
                print(f"Цифровое значение: {digital_value}")
                print(f"Измеренное напряжение: {voltage:.4f} В")

            return voltage

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.292)

        while True:
            #voltage = adc.get_sc_voltage()
            voltage = adc.get_sar_voltage()
            print(f"Измеренное напряжение: {voltage:.4f} В")
            time.sleep(0.1)  # pause

    finally:
        adc.deinit()
