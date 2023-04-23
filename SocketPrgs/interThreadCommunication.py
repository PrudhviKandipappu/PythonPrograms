
import socket
from threading import*
import time

message = str()
serverObject = socket.socket()
host = "192.168.169.247"
port = 5000
serverObject.bind((host, port))
serverObject.listen(3)

def serverScoket(conn):#, condition
	# client.start()
	global message
	while True:
		try:
			conn.send(message.encode())
		except Exception as e:
			print(e)
		# try:
		# 	condition.notify()
		# except Exception as e:
		# 	print(str(e))
		message = conn.recv(1024)
		if not message:
			break
		# condition.wait()
		message = message.decode()
	conn.close()

# conditionObject = Condition()
while True:
	conn, address = serverObject.accept()
	client = Thread(target = serverScoket, args = conn)
	client.start()
	# serverScoket(conn)# , conditionObject
serverObject.close()


