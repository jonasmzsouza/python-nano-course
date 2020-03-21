name=input("Enter the name: ")
age=int(input("Enter the age: "))
contagiousDisease=input("Suspected contagious disease? ").upper()
if age >= 65:
    print("Patient with priority")
    if contagiousDisease == "YES":
        print("Refer the patient " + name + " to the yellow room")
    elif contagiousDisease == "NO":
        print("Refer the patient " + name + " to the white room")
    else:
        print("Answer YES or NO to contagious disease")
else:
    print("Patient without priority")
    if contagiousDisease == "YES":
        print("Refer the patient " + name + " to the yellow room")
    elif contagiousDisease == "NO":
        print("Refer the patient " + name + " to the white room")
    else:
        print("Answer YES or NO to contagious disease")