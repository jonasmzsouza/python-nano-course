import socket

answer = "Y"
while answer == "Y":
    url = input("Enter a url: ")
    ip = socket.gethostbyname(url)
    print("The IP of the URL provided is: ", ip)
    answer = input("Enter <Y> to continue: ").upper()
