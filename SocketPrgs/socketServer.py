# Server socket program

import socket

host = "192.168.169.247"
port = 4123

serverObject = socket.socket()
serverObject.bind((host, port))

serverObject.listen(3)
conn, address = serverObject.accept()

print("Connection from: " + str(address))

while True:
	clientMessage = conn.recv(1024)
	clientMessage = clientMessage.decode()

	if not clientMessage:
		break
	print("From client: " + clientMessage)

	message = input("-> ")
	message = message.encode()
	conn.send(message)
conn.close()