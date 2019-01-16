import onewire
import machine
import ds18x20
import time


class ds18x20_setup:
    def __init__(self, data_pin=None, ground_pin=None, power_pin=None):
        if data_pin is not None:
            data_pin = machine.Pin(data_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        if ground_pin is not None:
            ground_pin = machine.Pin(ground_pin, machine.Pin.OUT, machine.Pin.PULL_UP)
            ground_pin.value(0)
        if power_pin is not None:
            power_pin = machine.Pin(power_pin, machine.Pin.OUT, machine.Pin.PULL_UP)
            power_pin.value(1)
        self.data = ds18x20.DS18X20(onewire.OneWire(data_pin))
        self.devices = self.data.scan()

    # These functions use functions from ds18x20
    def temperature(self):
        time.sleep_ms(750)
        data = []
        for rom in self.devices:
            data += [str(self.data.read_temp(rom))]
        data = ",".join(data)
        return self.data

    def pre_measure(self):
        return self.data.convert_temp()
