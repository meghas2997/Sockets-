import cv2 as cv
import socket
import pickle
import struct
import numpy as np

IP = "192.168.0.117"
PORT = 9909
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creats a socket object with IPv4 and TCP protocol
server = ('localhost', PORT)
s.bind(server) #the IP address of the local host and the port number is binded 
s.listen(1) #listen enables the socket to accept the message
c, address = s.accept() #accepts wait for the incoming connection and connects with a socket and address
arr_full = []
while 1:
    msg = c.recv(65000) #msg is recieved from the server for the given number of bytes 
    #print(len(msg))
    if not msg: break
    arr =  np.frombuffer(msg, dtype= 'uint8') #array is converted back from bytes into datatype
    arr1 = np.array(arr) #packets are converted to string of arrays
    arr2 = np.reshape(arr1, newshape= (500,3)) #the string of arrays are reshaped into one packet and appended
    arr_full.append(arr2)
    
arr3 = np.array(arr_full) #the appended array is converted to an image of array in the form of (height,width,channel)
print(arr3.shape)
cv.imshow('hello',arr3) #the image is displayed 

cv.waitKey(0)

c.close()
s.close()