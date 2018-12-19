import socket;
def Main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connects.connect((host, port))
		message = input("--> ")
		print(message)
		while message != 'q':
			s.send(message.encode())
			data = s.recv(1024).decode()
			print("Received from Server: " + str(data))
			message = input("--> ")
		s.close()
if __name__ == '__main__':
	Main()