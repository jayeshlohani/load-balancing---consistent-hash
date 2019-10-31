import socket
import random
s=socket.socket()
#port1=random.randrange(2000,2050)
#port=port1
port=3001
s.bind(('',port))
while True:
    s.listen(5)
    c,addr=s.accept()
    print("got connection from "+str(addr)) 
    c.send("connected - server1".encode())
c.close()
s.close()
