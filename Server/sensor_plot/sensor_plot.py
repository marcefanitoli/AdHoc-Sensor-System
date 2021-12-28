import time
import numpy as np
import matplotlib.pyplot as plt
import requests


class plot:
    def __init__(self, delay):
        self.sensor_list = []
        self.delay = delay
        self.tmax = -100
        self.tmin = 100
        self.n = 0

    def add_sensor(self, name, address, color, constant_offset):
        self.sensor_list += [{"name": name, "address": address, "last_data": None, "color": color, "constant_offset": constant_offset}]

    def __get_request__(self, item):
        requests.ReadTimeout = 1.9
        requests.Timeout = 1.6
        requests.ConnectTimeout = 1.4
        data = requests.get(item["address"], timeout=1.8)
        return float(data.text) + item["constant_offset"]

    def __update_plots__(self, item, data):
        if item["last_data"] is None:
            item["last_data"] = data
        self.tmax = max(self.tmax, data)
        self.tmin = min(self.tmin, data)
        plt.axis([0, self.n, self.tmin, self.tmax])
        plt.plot([self.n-1, self.n], [item["last_data"], data], marker='', markersize=12, color=item["color"], linewidth=2, linestyle='dotted', label=item["name"])
        # color='blue', markerfacecolor='blue',
        item["last_data"] = data

    def __update_logs__(self, n, item, data):
        with open("log.csv", "a") as fp:
            fp.write(str(n) +"," + item["name"] + "," + str(data) + "\n")

    def __run_once__(self):
        plt.legend()

    def run_forever(self):
        once = False
        while True:
            self.n += 1
            for item in self.sensor_list:
                try:
                    data = self.__get_request__(item)
                    self.__update_plots__(item, data)
                    self.__update_logs__(self.n, item, data)
                except requests.exceptions.ReadTimeout:
                    print("read timed out for: " + item["name"])
                except requests.ConnectionError:
                    print("ConnectionError timed out for: " + item["name"])
            plt.pause(self.delay)
            if not once:
                self.__run_once__()
                once = True
        plt.show()
