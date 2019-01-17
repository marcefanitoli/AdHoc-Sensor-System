from sensor_plot import sensor_plot

sensor = sensor_plot.plot(.1)
sensor.add_sensor("Sensor 1", r'http://sensor1/temperature', "red")
sensor.add_sensor("Sensor 2", r'http://sensor2/temperature', "green")
sensor.add_sensor("Sensor 3", r'http://sensor3/temperature', "blue")
sensor.run_forever()
