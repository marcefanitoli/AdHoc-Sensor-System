
# This file is executed on every boot (including wake-boot from deepsleep)
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.config(dhcp_hostname='ESP8266_SENSOR2')
nic.connect('Stardust','***REMOVED***')

while nic.isconnected() == False:
  pass

print('Connection successful')
print(nic.ifconfig())