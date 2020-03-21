inventory = []
answer = "Y"

#ADD ELEMENT TO THE INVENTORY
while answer == "Y":
    hardware=[input("Hardware: "),
              float(input("Price: ")),
              int(input("Serial Number: ")),
              input("Department: ")]
    inventory.append(hardware)
    answer = input("Enter \"Y\" to continue: ").upper()

#DISPLAY INVENTORY DATA
for element in inventory:
    print("\n----------------------------------")
    print("Hardware...: ", element)
    print("----------------------------------")
    print("Description: ", element[0])
    print("Price......: ", element[1])
    print("Serial.....: ", element[2])
    print("Department.: ", element[3])
    print("----------------------------------")

#SEARCH FOR AN ELEMENT IN THE INVENTORY
search=input("\nEnter name of the hardware you want to search: ")
for element in inventory:
    if search==element[0]:
        print("\nPrice......: ", element[1])
        print("Serial.....: ", element[2])

#ANSWER
depreciation=input("\nDo you want to depreciate this hardware by 10%? ").upper()
while depreciation != "YES" and depreciation != "NO":
    print("Answer YES or NO to depreciate")
    depreciation=input("Do you want to depreciate this hardware by 10%? ").upper()

#CHANGE DATA FOR AN ELEMENT IN THE INVENTORY
if depreciation == "YES":
    for element in inventory:
        if search==element[0]:
            print("\nOld price:", element[1])
            element[1] = element[1] * 0.9
            print("New price:", element[1])
else:
    print("The price of the hardware \"" + search + "\" has not been depreciated.")

#DELETE AN ELEMENT IN THE INVENTORY
search=input("\nEnter name of the hardware you want to delete: ")
for element in inventory:
    if search==element[0]:
        inventory.remove(element)

#NEW DISPLAY INVENTORY DATA
for element in inventory:
    print("\n----------------------------------")
    print("Hardware...: ", element)
    print("----------------------------------")
    print("Description: ", element[0])
    print("Price......: ", element[1])
    print("Serial.....: ", element[2])
    print("Department.: ", element[3])
    print("----------------------------------")

