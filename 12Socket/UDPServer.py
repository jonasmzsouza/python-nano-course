from socket import *

localhost = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((localhost, port))
print("Server ready...")
while True:
    data, origin = obj_socket.recvfrom(65535)
    print("Origin..........: ", origin)
    print("Received data: ", data.decode())
    answer = input("Enter the answer: ")
    obj_socket.sendto(answer.encode(), origin)
obj_socket.close()
