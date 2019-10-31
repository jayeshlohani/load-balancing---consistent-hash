import socket
s=socket.socket()
port=3000
#id="client2"
s.connect(('127.0.0.1',port))
port=int(s.recv(1024).decode())
s.close()
s=socket.socket()
s.connect(('127.0.0.1',port))
print(s.recv(1024).decode())
s.close()