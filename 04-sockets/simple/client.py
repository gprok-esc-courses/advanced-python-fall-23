from socket import socket, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5001))

msg = input("Type your name: ")
msg_bytes = str.encode(msg)

client_socket.send(msg_bytes)

msg_bytes = client_socket.recv(1024)
msg = msg_bytes.decode('utf-8')

print(msg)