import socket
import hashlib
##initial setup
s = socket.socket()#create socket 
port = 55555
ip=input("enter the ip: ")
s.connect((ip, port))
##user input collection
name = input("What is your username: ")
pwd= input("What is your password: ")
##encode and send
bytpwd=pwd.encode() #encode pwd data into byte
data = name + ',' + hashlib.sha224(bytpwd).hexdigest() #store name and store password hash
data = data.encode() #encode new string into byte form, and store it to data variable
s.sendall(data)#send encoded data
##overrite stored values to ensure they do not remain in memory
data=""
pwd=""
bytpwd=""
#

print (s.recv(1024).decode())#print recieved data
s.close()