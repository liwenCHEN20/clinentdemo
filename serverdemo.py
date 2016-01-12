#!/usr/bin/env python 

# Copy right (c) Liwen Chen

import socket, os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(("0.0.0.0",12344))

serverSocket.listen(5)

while True:
    
    (clientSocket,address) = serverSocket.accept()
    
    print str(address)
    
    childPid = os.fork()
    if (childPid != 0):
        #we must be still in the socket connection accepting process
        continue
    #we must in a client talking process
    
    
    remoteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    remoteSocket. connect(("www.google.ca",80))
    
    
    done = True
    while done:
        
        clientSocket.setblocking(0)
        try:
            part = clientSocket.recv(2048)
        except IOError, exception:
            if exception.errno == 11:
                part = None
            else:
                raise
        if part:
            remoteSocket.sendall(part)
            
            
        remoteSocket.setblocking(0)
        try:
            part = remoteSocket.recv(2048)
        except IOError, exception:
            if exception.errno == 11:
                part = None
            else:
                raise
        if part:
            clientSocket.sendall(part)