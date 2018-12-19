import socket
def Main():
    host='127.0.0.1'
    port=8080
    server=(host,port)
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(server)
    message=input("->")
    while message!='q':
        s.sendall(message.encode())
        data,addr=s.recvfrom(1024)
        data=data.decode()
        print("Received from server:"+str(data))
        message=input("->")
    s.close()
if __name__=='__main__':
    Main()
