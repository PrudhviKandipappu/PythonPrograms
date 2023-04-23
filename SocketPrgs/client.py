# Client Program

import tkinter as tk
import threading
import socket

host = "192.168.1.48"
port = 4123

window = tk.Tk()
window.title("Chat Box")

clientObject = socket.socket()
clientObject.connect((host, port))

messageCounter = 0

def loadMessage(message):
	global messageCounter
	if messageCounter != 0:
		listBox.insert(messageCounter - 1, message)
	messageCounter += 1

def getMessageFromChartBox():
	message = entryBox.get()
	loadMessage(f"Me : {message}")
	sendMessageToServer(message)
	if message == "bye":
		exit()
	entryBox.insert(0, str())

def receiveMessageFromServer():
	while True:
		try:
			data = clientObject.recv(1024)
			message = data.decode()
			loadMessage(message)
		except Exception:
			pass

def sendMessageToServer(data):
	data = data.encode()
	clientObject.send(data)

def serverInteraction():
	threading._start_new_thread(receiveMessageFromServer, ())

listBox = tk.Listbox(window, width = "40", height = "20")
listBox.pack()
entryBox = tk.Entry(window, width = "40", name = "entryBox")
entryBox.pack(side = tk.LEFT)
button = tk.Button(window, text = "Send", command = getMessageFromChartBox)
button.pack(side = tk.RIGHT)

threading._start_new_thread(serverInteraction, ())

window.mainloop()
clientObject.close()
