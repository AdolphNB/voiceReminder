from socket import *
from time import ctime


HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)
counter = 0


tcpSvrSock = socket(AF_INET, SOCK_STREAM)
tcpSvrSock.bind(ADDR)
tcpSvrSock.listen(5)


while True:
    
    print("Waiting for connection...")
    tcpCliSock, addr = tcpSvrSock.accept()
    print("...connected from", addr)
    
    while True:
        
        data = tcpCliSock.recv(BUFSIZ)
        
        if not data:
            break
        
        data = data.decode('utf-8')
        respMsg = "[%s] %s --> %s" % (ctime(), data, "adolph", counter)
        counter += 1
        tcpCliSock.send(bytes(respMsg, 'utf-8'))
        
    tcpCliSock.close()

tcpSvrSock.close()

