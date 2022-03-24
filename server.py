from encodings import utf_8
import random
import socket
from xml.etree.ElementTree import tostring
#host info constants
HOST = socket.gethostbyname(socket.gethostname())
PORT = 55555  
print(HOST+":"+PORT)

#validation code, this could be expanded to search an entire database rather than use hardcoded values
def validate(datatoval):
    if b"denis" in datatoval:# check username
        if b"d63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01" not in datatoval: #look for hash value of password in recieved string
            return False #output true or false
        else: 
            return True


#main server function
def Recieve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.bind((HOST, PORT)) 
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True: # this loop continues recieving data, until there is no more data to recieve
                data = conn.recv(1024)
                if not data:
                    break# stop loop when out of data
                if validate(data): # call validate function, and if data is valid, generate and send OTP
                    random_code =random.randint(10000,99999) # random 5 digit number
                    conn.sendall(bytes(f"Password verified, your OTP is: {random_code}","utf_8")) #combine OTP with verification message and send in byte form
                    
                else:
                    conn.sendall(b"Incorrect username/password")#inform user of wrong pass
while(1):#main loop to handle multiple connections in a row
    try:#simple exception handling
        print("running")
        Recieve() #call main function
    except:
        print("Something went wrong.")#exception message on server terminal