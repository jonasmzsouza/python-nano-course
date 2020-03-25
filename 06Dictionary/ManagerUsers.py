from function import *
users={}
option=ask()
while option == "I" or option == "S" or option == "D" or option == "L":
    if option == "I":
        insert(users)
    if option == "S":
        search(users,input("Which login do you want to search for? ").upper())
    if option == "D":
        delete(users,input("What login do you want to delete? ").upper())
    if option == "L":
        list(users)
    option = ask()
