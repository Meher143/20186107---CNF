import socket

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.connect((host, port))

	message = input("MARK-ATTANDENCE" + rollnumbers)
	while message != 'q':
		s.send(str.encode(message))
		data = s.recv(1024)
		data = data.decode()
		print("Received from server;" +str(data))
		tokens = str(data).split(" ")
		if tokens[0] = "SECRET QUESTION"
		print("")
		s.close()

if __name__ == '__main__':
	Main()