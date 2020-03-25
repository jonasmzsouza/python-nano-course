# ADD ELEMENT TO THE INVENTORY
def fillInventory(list):
    answer = "Y"
    while answer == "Y":
        hardware = [input("\nHardware: "),
                    float(input("Price: ")),
                    int(input("Serial Number: ")),
                    input("Department: ")]
        list.append(hardware)
        answer = input("\nEnter \"Y\" to continue: ").upper()

# DISPLAY INVENTORY DATA
def diplayInventory(list):
    for element in list:
        print("\n----------------------------------")
        print("Hardware...: ", element)
        print("----------------------------------")
        print("Description: ", element[0])
        print("Price......: ", element[1])
        print("Serial.....: ", element[2])
        print("Department.: ", element[3])
        print("----------------------------------")

#SEARCH FOR AN ELEMENT IN THE INVENTORY
def searchElement(list):
    search=input("\nEnter name of the hardware you want to search: ")
    for element in list:
        if search==element[0]:
            print("\n----------------------------------")
            print("\nPrice......: ", element[1])
            print("Serial.....: ", element[2])
            print("----------------------------------")

#CHANGE DATA FOR AN ELEMENT IN THE INVENTORY
def changeElement(list, perc):
    search = input("Enter name of the hardware you want to change the price: ")
    #ANSWER
    depreciation=input("Do you want to depreciate this hardware \"" + search + "\"? ").upper()
    while depreciation != "YES" and depreciation != "NO":
        print("Answer YES or NO to depreciate")
        depreciation=input("Do you want to depreciate this hardware? ").upper()

    if depreciation == "YES":
        for element in list:
            if search==element[0]:
                print("\n----------------------------------")
                print("Old price:", element[1])
                element[1] = element[1] * (1-perc/100)
                print("New price:", element[1])
                print("----------------------------------")
    else:
        print("The price of the hardware \"" + search + "\" has not been depreciated.")

#DELETE AN ELEMENT IN THE INVENTORY
def deleteElement(list):
    search=input("\nEnter name of the hardware you want to delete: ")
    for element in list:
        if search==element[0]:
            list.remove(element)
    return "Element deleted"

#SUMMARY OF VALUES
def summaryValues(list):
    values=[]
    for element in list:
        values.append(element[1])
    if len(values)>0:
        print("\n----------------------------------")
        print("Most expensive hadware value: ", max(values) )
        print("Cheaper hardware value: ", min(values))
        print("Total values: ", sum(values))
        print("----------------------------------")