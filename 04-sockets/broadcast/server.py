from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def client_thread(conn, name):
    while True:
        msg_bytes = conn.recv(1024)
        msg = msg_bytes.decode('utf-8')
        print(msg)
        new_msg = name + ": " + msg
        new_msg_bytes = str.encode(new_msg)
        for client in clients:
            client[0].send(new_msg_bytes)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5002))

clients = []

server_socket.listen()
print("Server started on port 5002")

while True:
    conn, addr = server_socket.accept()
    print("Connection from ", addr)
    clients.append((conn, addr))
    msg_bytes = conn.recv(1024)
    name = msg_bytes.decode('utf-8')
    print(name)
    msg = "Hello " + name
    msg_bytes = str.encode(msg)
    conn.send(msg_bytes)
    # Start a new thread for the connection
    th = Thread(target=client_thread, args=(conn, name))
    th.start()