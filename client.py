import socket
import os
s=socket.socket()
#id="client1"
while 1:
    port=3000
    s.settimeout(1)
    s.connect(('127.0.0.1',port))
    p=int(s.recv(1024).decode())
    s.close()
    s=socket.socket()
    s.settimeout(1)
    if os.system('netstat -aon | find /i "listening" | findstr "3001" |  find /c /v ""') >=1 :
        s.connect(('127.0.0.1',p))
        break 
    break       
    print('hello')     

print(s.recv(1024).decode())
s.close()