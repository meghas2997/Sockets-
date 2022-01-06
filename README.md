# Sockets-
Sokets with Python 3
Sockets are used to send messages through a network. The network can be send be from a local network to the computer or it can be ecternally connected with other networks. There are certain socket APIs used with python sockets and openCV to send and image from the server to the client. We have used the TCP and UDP sockets to send an image from the local host to the client local host. 

## TCP Sockets
Transmission control Protocol is one of the main protocol. TCP is connection oriented and the client and the server need to be cnnected before the data is to be sent.TCP is more reliable and has in order delivery with error checking. To create a socket object, socket.SOCK.STREAM is specified as TCP socket type. The data is sent from the host to to the client via IP network in form of bytes. 

## UDP Sockets 
User Datagram Protocol is also a member of internet protocol suite. UDP uses a simple connectionless communication model with a minimum of protocol mechanisms. There is no guarantee of reliability, order and error checking in case of UDP. 

## OpenCV
For image reading and sending into data packets OpenCV library is used in this code. The image is rad with cv.imread and then numpy library is used to convert the image packets into arrays and send the data into bytes. cv.imshow is used in the client side to show the image recieved. 
