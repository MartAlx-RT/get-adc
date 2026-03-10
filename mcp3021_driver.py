import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"received: {data}, highest byte: {upper_data_byte:x}, lower byte: {lower_data_byte:x}, number: {number}")
        return number

    def get_voltage(self):
        return self.dynamic_range * (self.get_number() / 2**10)


if __name__ == "__main__":
    try:
        mcp = MCP3021(5.210)    # dynamic range

        while True:
            voltage = mcp.get_voltage()
            print(f"input voltage: {voltage:.4f} В")
            time.sleep(1)  # pause

    finally:
        mcp.deinit()
