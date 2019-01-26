import socket


def sendMsg():
    print('send.....')
    mySocket = socket.socket()
    mySocket.connect(('127.0.0.1', 2333))
    while True:
        # data = mSocket.recv(1024)
        # print("Received message:%s" % str(data))
        inp = input('please input:')
        mySocket.sendall(inp.encode('utf-8'))
        print("msg has been sent")
        if inp == 'over':
            break
            mySocket.close()


if __name__ == '__main__':
    sendMsg()
