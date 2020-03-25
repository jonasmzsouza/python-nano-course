users={}
answer="Y"
emails=[]
while answer=="Y":
    emails.append(input("Enter an e-mail: ").lower())
    answer=input("Enter <Y> to continue: ").upper()

tuple = list(enumerate(emails))
for key in range(0,len(tuple)):
    print("\nEmail: ", tuple[key][1])
    users[tuple[key]]=[input("Enter the name: "), input("Enter the level: ")]

for key,data in users.items():
    print("\n----------------------------------")
    print("User....: ", key[0])
    print("Email...: ", key[1])
    print("Name....: ", data[0])
    print("Level...: ", data[1])
    print("----------------------------------")