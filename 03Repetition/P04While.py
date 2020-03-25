name=input("Enter the name: ")
age=int(input("Enter the age: "))
gender=input("Enter the gender of the patient: ").upper()

while gender != "MAN" and gender != "WOMAN":
    print("Answer MAN or WOMAN to gender")
    gender = input("Enter the gender of the patient: ").upper()

contagiousDisease=input("Suspected contagious disease? ").upper()

while contagiousDisease != "YES" and contagiousDisease != "NO":
    print("Answer YES or NO to contagious disease")
    contagiousDisease = input("Suspected contagious disease? ").upper()

if gender == "WOMAN" and age > 10:
    pregnancy=input("Is the patient pregnant? ").upper()
else:
    pregnancy="NO"

while pregnancy != "YES" and pregnancy != "NO":
    print("Answer YES or NO to patient pregnant")
    pregnancy=input("Is the patient pregnant? ").upper()

if contagiousDisease == "YES":
    print("Refer the patient " + name + " to the yellow room")
elif contagiousDisease == "NO" and age >= 65:
    print("Refer the patient " + name + " to the white room - WITH priority.")
elif contagiousDisease == "NO" and pregnancy == "YES" :
    print("Refer the patient " + name + " to the white room - WITH priority.")
else:
    print("Refer the patient " + name + " to the white room - WITHOUT priority.")