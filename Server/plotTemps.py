import requests
import numpy as np
import matplotlib.pyplot as plt
n = 1
tmax = -100
tmin = 100
once = True
old_data3 = None
old_data2 = None
old_data1 = None
while True:
    n += 1
    a = requests.get(r'http://sensor3/temperature')
    data = float(a.text)
    if not old_data3:
        old_data3 = data
    tmax = max(tmax, data)
    tmin = min(tmin, data)
    plt.axis([0, n, tmin, tmax])
    # plt.scatter(n, data)
    plt.plot([n-1, n], [old_data3, data], marker='', color='blue', markerfacecolor='blue', markersize=12, linewidth=2, linestyle='solid', label="sensor3")
    old_data3 = data

    a = requests.get(r'http://sensor2/temperature')
    data = float(a.text)
    if not old_data2:
        old_data2 = data
    tmax = max(tmax, data)
    tmin = min(tmin, data)
    plt.axis([0, n, tmin, tmax])
    # plt.scatter(n, data)
    plt.plot([n-1, n], [old_data2, data], marker='', color='blue', markerfacecolor='blue', markersize=12, linewidth=2, linestyle='dashed', label="sensor2")
    old_data2 = data

    a = requests.get(r'http://sensor1/temperature')
    data = float(a.text)
    if not old_data1:
        old_data1 = data
        plt.legend()
    tmax = max(tmax, data)
    tmin = min(tmin, data)
    plt.axis([0, n, tmin, tmax])
    # plt.scatter(n, data)
    plt.plot([n-1, n], [old_data1, data], marker='', color='blue', markerfacecolor='blue', markersize=12, linewidth=2, linestyle='dotted', label="sensor1")
    old_data1 = data
    if once:
        plt.legend()
        once = False
    plt.pause(2.75)

plt.show()
