name=input("Enter the name: ")
age=int(input("Enter the age: "))
contagiousDisease=input("Suspected contagious disease? ").upper()
if age >= 65 and contagiousDisease == "YES":
    print("Refer the patient " + name + " to the yellow room - With priority")
if age < 65 and contagiousDisease == "YES":
    print("Refer the patient " + name + " to the yellow room - Without priority")
if age >= 65 and contagiousDisease == "NO":
    print("Refer the patient " + name + " to the white room - With priority")
if age < 65 and contagiousDisease == "NO":
    print("Refer the patient " + name + " to the white room - Without priority")
else:
    print("Answer YES or NO to contagious disease")