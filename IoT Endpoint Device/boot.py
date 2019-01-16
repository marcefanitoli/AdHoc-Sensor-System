# This file is executed on every boot (including wake-boot from deepsleep)
try:
    import usocket as socket
except:
    import socket

from machine import Pin
import network
import esp
import gc


import webrepl
HOST_NAME = 'SENSOR1'
WIRELESS_ACCESS_POINT = 'Stardust'
PASSWORD = '***REMOVED***'
esp.osdebug(None)
gc.collect()

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.config(dhcp_hostname=HOST_NAME)
nic.connect(WIRELESS_ACCESS_POINT, PASSWORD)

while nic.isconnected() is False:
    pass

print('Connection successful')
print(nic.ifconfig())
webrepl.start()
