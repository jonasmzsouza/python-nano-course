from socket import *

localhost = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((localhost, port))
output = ""
while output != "X":
    msg = input("Your message: ")
    obj_socket.sendto(msg.encode(), (localhost, port))
    data, origin = obj_socket.recvfrom(65535)
    print("Server response: ", data.decode())
    output = input("Enter <X> to exit: ").upper()
obj_socket.close()
