from socket import *

localhost = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((localhost, port))
obj_socket.listen(2)
print("Waiting for the client...")
while True:
    con, client = obj_socket.accept()
    print("Connected with: ", client)
    while True:
        msg_received = str(con.recv(1024))
        print("Message Received: ", str(msg_received)[2:-1])
        msg_sent = bytes(input("Your answer: "), 'utf-8')
        con.send(msg_sent)
        break
    con.close()
