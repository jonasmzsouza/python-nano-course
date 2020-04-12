import getpass

user = input("Enter user: ").upper()
password = getpass.getpass("Enter password: ")

if user == "PYTHON" and password == "P383838":
    print("User logged in")
else:
    print("Acess denied")