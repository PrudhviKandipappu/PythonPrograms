# Server program

import socket
import threading

threadCount = 0
host = "192.168.1.40"
port = 4123
serverObject = socket.socket()

try:
	serverObject.bind((host, port))
except Exception as e:
	print(e)
serverObject.listen()

listOfThreads = []

def multiThreadedClient(client):
	global listOfThreads
	while True:
		responce = client.recv(1024).decode()
		print(responce)
		if not responce:
			break

		for record in listOfThreads:
			if record[1] == client:
				name = str(record[0])

		for record in listOfThreads:
			if record[1] != client:
				message = f"{name} : {responce}"
				message = message.encode()
				record[1].send(message)
	client.close()

while True:
	client, address = serverObject.accept()
	clientName = f"({address[0]} - {address[1]})"
	print("Connected to: " + address[0] + ": " + str(address[1]))
	listOfThreads.append([clientName, client])
	threading._start_new_thread(multiThreadedClient, (client, ))
	threadCount += 1
	print("Thread Number: " + str(threadCount))
serverObject.close()