import cv2 as cv
import socket
import pickle
import struct
import numpy as np
import time


def split(arr, size): #defining a split function to split the length and size of the array
    test1 = []
    k, m = divmod(len(arr), size)
    for i in range(size):
        arr_div = arr[i*k + min(i, m):(i+1)*k + min(i+1,m)]
        test1.append(arr_div)
    return test1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_NET depicts IPv4 and Sock_STREAM depicts TCP(Transmission control protocol- address type)
##creates a socket object
IP = "localhost"
PORT = 9909
server = ('localhost', PORT)

s.connect(server) #connect the server to the client with the IP address and port number 

img = cv.imread('group 2.jpeg') #reads the image 

h, w, c = img.shape #array shape of the image with height, width and color channel
# print('height: ', h)
# print('width: ', w)
# print('channel: ', c)
msg = [] #creation of a empty array
for i in range (h): #for loop in range of number of height packets
    msg= img[i][:][:] #h number of packets are send with w*c elements
    msg_1 = msg.tobytes() #the array is converted into bytes
    time.sleep(0.001)
    s.send(msg_1) 
