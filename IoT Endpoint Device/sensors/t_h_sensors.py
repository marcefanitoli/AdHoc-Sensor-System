import dht
import machine


class dht11(dht.DHT11):
    def __init__(self, data_pin=None, ground_pin=None, power_pin=None):
        if data_pin:
            data_pin = machine.Pin(data_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        if ground_pin:
            ground_pin = machine.Pin(ground_pin, machine.Pin.OUT, machine.Pin.PULL_DOWN)
            ground_pin.value(0)
        if power_pin:
            power_pin = machine.Pin(power_pin, machine.Pin.OUT, machine.Pin.PULL_UP)
            power_pin.value(1)
        dht.DHT11.__init__(self, data_pin)

    def pre_measure(self):
        return self.measure()
