import socket 

def Main():
	host = '127.0.0.1'
	port = 5000
	list = ["20158501, 20158502, 20158503, 20158504, 20158505, 20158506, 20158507, 20158508, 20158509, 20158510"]
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	c, addr = s.accept()
	print("connection from:" + str(addr))
	while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print("from connected user:" + str(data))
        data = data.split(" ")
        res = int(data[2]) * (dict[data[1]+"To"+data[4]])
        res = round(res, 1)


        print("sending: "+str(res))
        c.send(str(res).encode())
    c.close()
if __name__ == '__main__':
    Main()
