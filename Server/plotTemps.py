from sensor_plot import sensor_plot

sensor = sensor_plot.plot(5)
sensor.add_sensor("Sensor 1", r'http://192.168.43.171/temperature', "red", -0.394211111)
#sensor.add_sensor("Sensor 1 H", r'http://192.168.43.171/humidity', "green")
sensor.add_sensor("Sensor 2", r'http://192.168.43.18/temperature', "blue", -10.331711111)
sensor.add_sensor("Sensor 3", r'http://192.168.43.92/temperature', "green", -9.706711111)
sensor.run_forever()
