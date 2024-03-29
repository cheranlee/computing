import socket

chat_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

chat_socket.connect((address, port))
data = '' 
while data != 'quit':
    print('WAITING FOR SERVER...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    print('SERVER WROTE: ' + data.decode())
    data = data.strip().decode()
    if data != 'quit': 
        data = input('INPUT CLIENT: ').encode()
        chat_socket.sendall(data + b'\n')

chat_socket.close() 
