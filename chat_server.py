import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 6789))
listen_socket.listen()

chat_socket, addr = listen_socket.accept()
data = ''
while data != 'quit':
    data = input('INPUT SERVER: ').encode()
    chat_socket.sendall(data + b'\n')
    data = data.decode()
    if data != 'quit': 
        print('WAITING FOR CLIENT...')
        data = b''
        while b'\n' not in data:
            data += chat_socket.recv(1024)
        print('CLIENT WROTE: ' + data.decode())
print("STOPPED") 
chat_socket.close()
listen_socket.close() 
