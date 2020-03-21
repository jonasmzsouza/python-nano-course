name=input("Enter the name: ")
age=int(input("Enter the age: "))
contagiousDisease=input("Suspected contagious disease? ").upper()
if age >= 65:
    print("The patient " + name + " has priority service.")
elif contagiousDisease == "YES":
    print("The patient " + name + " must be taken to the reserved waiting room.")
else:
    print("The patient " + name + " hasn't priority service.")