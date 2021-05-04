import socket

my_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

my_socket.connect((address, port))
print(my_socket.recv(1024))
my_socket.sendall(b'Hello from client\n')
my_socket.close() 
