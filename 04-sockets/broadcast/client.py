from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def receive(sock):
    while True:
        msg_bytes = sock.recv(1024)
        msg = msg_bytes.decode('utf-8')
        print(msg)


client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5002))

msg = input("Type your name: ")
msg_bytes = str.encode(msg)

client_socket.send(msg_bytes)

msg_bytes = client_socket.recv(1024)
msg = msg_bytes.decode('utf-8')

print(msg)

th = Thread(target=receive, args=(client_socket,))
th.start()

while True:
    msg = input("Type msg: ")
    msg_bytes = str.encode(msg)
    client_socket.send(msg_bytes)

