# Socket client program

import socket
import threading

host = "192.168.1.40"
port = 4123

clientObject = socket.socket()
clientObject.connect((host, port))

def recieveMessage():
	while True:
		serverMessage = clientObject.recv(1024).decode()
		print(serverMessage)

def sendMessage(message):
	message = message.encode()
	clientObject.send(message)

name = (input("Enter Your Name: ")).encode()
clientObject.send(name)

while True:
	threading._start_new_thread(recieveMessage, ())
	message = input("")
	if message.lower().strip() == "bye":
		break
	threading._start_new_thread(sendMessage, (message, ))
clientObject.close()