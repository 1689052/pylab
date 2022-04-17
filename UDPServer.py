#!/usr/bin/python3

import socket

host =""
port = 12276
buff_size = 128
sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)

while True:
    print("wating for rerquest...")

    message, client_address = sock.recvfrom(buff_size)
    print("echo request from {} port : {}".format(client_address[0], client_address[1]))
    message.decode()

    try:
        message = int(message)
        if message % 2 == 0:
            print("입력된 정수는 짝수 입니다: {}\n".format(message))
        elif message % 2 != 0:
            print("입력된 정수는 홀수 입니다: {}\n".format(message))
    except ValueError:
        print("정수가 아닙니다.")

sock.close()
