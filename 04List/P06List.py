inventory = []
answer = "Y"
while answer == "Y":
    inventory.append(input("Hardware: "))
    inventory.append(float(input("Price: ")))
    inventory.append(int(input("Serial Number: ")))
    inventory.append(input("Department: "))
    answer = input("Enter \"Y\" to continue: ").upper()

for element in inventory:
    print(element)
