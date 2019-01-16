
import socketserver
import t_h_sensors
import t_sensors


server = socketserver.server()

SENSOR_TYPE = 'dht11'  # dht11 or ds18x20
if SENSOR_TYPE == 'dht11':
    sensor = t_h_sensors.dht11(data_pin=2, power_pin=0)
    server.set_pre_measure_function(sensor.pre_measure)
    server.add_target('temperature', sensor.temperature)
    server.add_target('humidity', sensor.humidity)
elif SENSOR_TYPE == 'ds18x20':
    sensor = t_sensors.dallas_one_wire(data_pin=2)
    server.set_pre_measure_function(sensor.pre_measure)
    server.add_target('temperature', sensor.temperature)

server.run_forever()
