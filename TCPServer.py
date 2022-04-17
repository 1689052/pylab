#!/usr/bin/python3

import socket

host = ""
port = 12276
buff_size = 128
c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
c_sock.bind(server_address)

c_sock.listen(5)

while True:
    print("waiting for requests...")
    data_c_sock, address = c_sock.accept()
    print("echo request from {} port {}".format(data_c_sock, address))
    message = data_c_sock.recv(buff_size)
    print(message.decode())

    if message :
        server_respone =" HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n<HTML><BODY><H1> Hello, World! </H1></BODY></HTML>"
        data_c_sock.sendall(server_respone.encode())
        print("++++++++")
data_hsock.close()