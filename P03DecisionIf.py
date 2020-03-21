name=input("Enter the name: ")
age=int(input("Enter the age: "))
if age >= 65:
    print("The patient " + name + " has priority care.")
else:
    print("The patient " + name + " hasn't priority care.")