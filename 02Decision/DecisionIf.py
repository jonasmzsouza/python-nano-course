name=input("Enter the name: ")
age=int(input("Enter the age: "))
gender=input("Enter the gender of the patient: ").upper()
contagiousDisease=input("Suspected contagious disease? ").upper()

if gender == "WOMAN" and age > 10:
    pregnancy=input("Is the patient pregnant? ").upper()
else:
    pregnancy="NO"

if contagiousDisease == "YES":
    print("Refer the patient " + name + " to the yellow room")
elif contagiousDisease == "NO" and age >= 65:
    print("Refer the patient " + name + " to the white room - WITH priority.")
elif contagiousDisease == "NO" and pregnancy == "YES" :
    print("Refer the patient " + name + " to the white room - WITH priority.")
elif contagiousDisease == "NO" and age < 65:
    print("Refer the patient " + name + " to the white room - WITHOUT priority.")
else:
    print("Answer YES or NO to contagious disease")




