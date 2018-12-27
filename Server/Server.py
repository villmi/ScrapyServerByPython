import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall('I am the server'.encode('utf-8'))
        flag = True
        while flag:
            data = conn.recv(1024)
            if data == 'over':
                flag = False
            else:
                print("the message is %s" % data)


if __name__ == '__main__':
    print("Server is running..")
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 2333), MyServer)
    server.serve_forever()





