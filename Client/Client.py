import socket
import threading

ip_port = ('127.0.0.1', 2333)
mySocket = socket.socket()
mySocket.connect(ip_port)


def listenServer(mySocket):
    while True:
        data = mySocket.recv(1024)
        print("the message is %s" % data)


while True:
    data = mySocket.recv(1024)
    print("Received message:%s" % str(data))
    inp = input('please input:')
    mySocket.sendall(inp.encode('utf-8'))
    if inp == 'over':
        break
mySocket.close()
