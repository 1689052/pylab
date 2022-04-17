#!/usr/bin/python3

import socket

host = '203.250.133.88'
port = 12276
buff_size = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to {} port {}".format(server_address[0], server_address[1]))
sock.connect(server_address)

message = input("파일 이름을 입력하세요 : ")
message = bytes(message, encoding='utf-8')


try:
    sock.sendall(message)
    data = sock.recv(buff_size)
    data = data.decode()

    if len(data) > 1:
        print("Received from server : \n{}".format(data))
        accessMode = 'w'
        filename = message
        myFile = open(filename, accessMode)
        myFile.write(data)
        print("클라이언트가 정상적으로 서버로 부터 받은 파일을 로컬에 저장 하였습니다.")
    else:
        print("파일을 찾을 수 없습니다.")

except Exception as e:
    print("Exception : {}".format(str(e)))

sock.close()