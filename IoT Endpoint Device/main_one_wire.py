

def web_page(data):
  html = str(data)
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
import time
import onewire, ds18x20
import machine
pin0 = machine.Pin(0, machine.Pin.OUT, machine.Pin.PULL_UP)
pin0.value(1)
pin2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
ds = ds18x20.DS18X20(onewire.OneWire(pin2))
roms = ds.scan()
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  temperature = request.find('/temperature')
  if temperature == 6:
    ds.convert_temp()
    time.sleep_ms(750)
    data=[]
    for rom in roms:
      data += [str(ds.read_temp(rom))]
    data = ",".join(data)
    response = web_page(data)
  else:
    conn.send('HTTP/1.1 404 OK')
    response = request
  response_headers = []
  response_headers += ["Content-Type: text/html; encoding=utf8"]
  response_headers += ["Content-Length: "+str(len(response))]
  response_headers += ["Connection: close"]
  response_headers_raw = "\n".join(response_headers)
  conn.send('HTTP/1.1 200 OK')
  conn.send(response_headers_raw)
  conn.send('\n')
  conn.send('\n')
  print(response)
  print(str(len(response)))
  conn.send(response)
  conn.close()
