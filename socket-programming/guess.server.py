import socket
import random 

s = socket.socket()
s.bind(('127.0.0.1', 9999))
s.listen()
addr, s_listening = s.accept()

num = random.randrange(1, 100)
count = 0 

addr.sendall(b'GUESS\n')
while count <= 3:
    data = b''
    while b'\n' not in data:
        data += addr.recv(1024)
    received = data[:data.find(b'\n')]
    received = int(received.decode())
    if received < num:
        addr.sendall(b'LOW\n')
        addr.sendall(b'GUESS\n') 
    elif received > num:
        addr.sendall(b'HIGH\n')
        addr.sendall(b'GUESS\n')
    else:
        addr.sendall(b'WIN\n')
        break
    count += 1
else:
    addr.sendall(b'GAMEOVER\n')

addr.close()
s.close() 
