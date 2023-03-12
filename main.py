#!/bin/python3

#SOCKETS - connects 2 nodes together (ports/ip addresses)

import socket 

Host = '127.0.0.1' #Loopback address
Port = 7777

s = socket.stocket(socket.AF_INET, socket.SOCK_STREAM) #af_int is IPv4, socket_stream is a port

s.connect((Host, Port))

#netcat(nc) - connect ports or establish a listening port

#Thank You TCM Security