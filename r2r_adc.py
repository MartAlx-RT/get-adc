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
