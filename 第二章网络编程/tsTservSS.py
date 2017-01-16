from socketserver import TCPServer, StreamRequestHandler
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(StreamRequestHandler):

    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCPServer(ADDR, MyRequestHandler)
print('waiting fro connection...')
tcpServ.serve_forever
