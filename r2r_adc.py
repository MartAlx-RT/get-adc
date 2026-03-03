

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
def sequential_counting_adc(self):
        max_value = 2**8 - 1  # 255 для 8-битного ЦАП

        for value in range(max_value + 1):
            self.number_to_dac(value)       # 1. Подаём число на ЦАП
            time.sleep(self.compare_time)   # 2. Ждём, пока компаратор сравнит напряжения
            comparator_output = GPIO.input(self.comp_gpio)  # 3. Считываем состояние компаратора
            
            if self.verbose:
                voltage = value / max_value * self.dynamic_range
                print(f"Код: {value}, Напряжение: {voltage:.3f} В")

            if comparator_output == 0:  # 4. Если напряжение ЦАП превысило входное (логика зависит от схемы!)
                return value

        return max_value    # 5. Если так и не превысили входное напряжение

    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()  # Получаем цифровое значение

        n_bits = len(self.bits_gpio)        # Определяем разрядность по количеству пинов
        max_value = 2**n_bits - 1

        voltage = digital_value / max_value * self.dynamic_range    # Переводим в напряжение

        if self.verbose:
            print(f"Цифровое значение: {digital_value}")
            print(f"Измеренное напряжение: {voltage:.4f} В")

        return voltage

if name == "main":
    try:
        adc = R2R_ADC(3.17)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Измеренное напряжение: {voltage:.4f} В")
            time.sleep(0.1)  # небольшая пауза для удобства вывода

    finally:
        adc.deinit()
