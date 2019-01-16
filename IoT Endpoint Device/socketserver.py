import socket


class server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)
        self.path_data = {}

    def set_pre_measure_function(self, pre_measure_function):
        self.pre_measure_function = pre_measure_function

    def add_target(self, path_endpoint, path_function):
        self.path_data[path_endpoint] = path_function

    def run_forever(self):
        while True:
            self.conn, self.addr = self.s.accept()
            print('Got a connection from %s' % str(self.addr))
            self.request = self.conn.recv(1024)
            self.request = str(self.request)
            print('Content = %s' % self.request)
            success = False
            for path in self.path_data:
                if self.request.find('/' + path) == 6:
                    success = True
                    self.pre_measure_function()
                    return self.path_data[path]()
            if not success:
                self.conn.send('HTTP/1.1 404 OK')
                response = self.request

            response_headers = []
            response_headers += ["Content-Type: text/html; encoding=utf8"]
            response_headers += ["Content-Length: "+str(len(response))]
            response_headers += ["Connection: close"]
            response_headers_raw = "\n".join(response_headers)
            self.conn.send('HTTP/1.1 200 OK')
            self.conn.send(response_headers_raw)
            self.conn.send('\n')
            self.conn.send('\n')
            print(self.response)
            print(str(len(self.response)))
            self.conn.send(response)
            self.conn.close()
