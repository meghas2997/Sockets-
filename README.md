# Sockets-
Sockets with Python 3


Sockets are used to send messages through a network. The network can be send be from a local network to the computer or it can be ecternally connected with other networks. There are certain socket APIs used with python sockets and openCV to send and image from the server to the client. We have used the TCP and UDP sockets to send an image from the local host to the client local host. 

## TCP Sockets
Transmission control Protocol is one of the main protocol. TCP is connection oriented and the client and the server need to be cnnected before the data is to be sent.TCP is more reliable and has in order delivery with error checking. To create a socket object, socket.SOCK.STREAM is specified as TCP socket type. The data is sent from the host to to the client via IP network in form of bytes. 

## UDP Sockets 
User Datagram Protocol is also a member of internet protocol suite. UDP uses a simple connectionless communication model with a minimum of protocol mechanisms. There is no guarantee of reliability, order and error checking in case of UDP. 

## OpenCV
For image reading and sending into data packets OpenCV library is used in this code. The image is rad with cv.imread and then numpy library is used to convert the image packets into arrays and send the data into bytes. cv.imshow is used in the client side to show the image recieved. 


### connection from server sent 
![server](https://user-images.githubusercontent.com/92062404/148404998-8e31b747-dd3e-49bc-ba39-25d2369f9e00.PNG)

### sniffing thourgh Wireshark
Wireshark is used to see the data packets sent from the server to the client. it tells how many bytes and the form of packets sent which makes it easier to figure out if the right data is sent in the right amount. 
![wireshark](https://user-images.githubusercontent.com/92062404/148408374-533dae62-f0a7-4008-857f-1e19e91e94e6.PNG)


### data from server to client recieved 
![client](https://user-images.githubusercontent.com/92062404/148405027-ce99e683-001d-4677-921d-0d94bf8bbf0d.PNG)
