import os
from ftplib import *

ftp_active = False
ftp = FTP(input("Enter the FTP you want to connect to: "))
print(ftp.getwelcome())
user = input("\nEnter user: ")
password = input("Enter password: ")
ftp.login(user, password)
print("\nSuccessful connection. Current working directory: ", ftp.pwd())
menu = "1"
while menu == "1" or menu == "2" or menu == "3":
    menu = input("\nChoose the option you want:\n" +
                 "<1> - To list files\n" +
                 "<2> - To define a directory\n" +
                 "<3> - To download a file: ")
    if menu == "1":
        print("\n")
        print(ftp.dir())
    elif menu == "2":
        ftp.cwd(input("\nEnter the directory you want to sign in: "))
        print("Current directory is: ", ftp.pwd())
    elif menu == "3":
        type = input("\nType <B> for binary file or any other button for ASCII file: ").upper()
        if type == "B":
            with open(input("Enter the name of the target file: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Source file: "), arq.write)
        else:
            with open(input("Enter the name of the target file: "), 'w') as arq:
                def writeLine(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Source file: "), writeLine)
        print("File successfully downloaded!")
ftp.quit()
