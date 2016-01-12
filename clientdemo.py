#!/usr/bin/env python 

# Copy right (c) Liwen Chen

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


clientSocket. connect(("www.google.ca",80))

request = "GET / HTTP/1.0\n\n"

clientSocket.sendall(request)

done = True

while done:
    part = clientSocket.recv(2048)
    if part:
        print part
    else:
        done = False