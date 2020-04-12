from socket import *

localhost = "127.0.0.1"
port = 43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((localhost, port))
    msg = bytes(input("Your answer: "), 'utf-8')
    obj_socket.send(msg)
    answer = obj_socket.recv(1024)
    print("Message Received: : ", str(answer)[2:-1])
    if str(msg)[2:-1].upper() == "FIM":
        break
obj_socket.close()
