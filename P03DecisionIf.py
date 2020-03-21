name=input("Enter the name: ")
age=int(input("Enter the age: "))
priority="NO"
if age>=65:
    priority="YES"
print("Does the patient " + name + " have priority care? " + priority)