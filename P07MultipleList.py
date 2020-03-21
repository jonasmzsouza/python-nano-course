hardwares = []
prices = []
serials = []
departments = []
answer = "Y"
while answer == "Y":
    hardwares.append(input("Hardware: "))
    prices.append(float(input("Price: ")))
    serials.append(int(input("Serial Number: ")))
    departments.append(input("Department: "))
    answer = input("Enter \"Y\" to continue: ").upper()

for index in range(0,len(hardwares)):
    print("\n----------------------------------")
    print("Hardware...: ", (index+1))
    print("----------------------------------")
    print("Description: ", hardwares[index])
    print("Price......: ", prices[index])
    print("Serial.....: ", serials[index])
    print("Department.: ", departments[index])
    print("----------------------------------")

search=input("\nEnter name of the hardware you want to search: ")
for index in range(0,len(hardwares)):
    if search==hardwares[index]:
        print("\nPrice......: ", prices[index])
        print("Serial.....: ", serials[index])

depreciation=input("\nDo you want to depreciate this hardware by 10%?").upper()
while depreciation != "YES" and depreciation != "NO":
    print("Answer YES or NO to depreciate")
    depreciation=input("Do you want to depreciate this hardware by 10%?").upper()

if depreciation == "YES":
    for index in range(0,len(hardwares)):
        if search==hardwares[index]:
            print("\nOld price:", prices[index])
            prices[index] = prices[index] * 0.9
            print("New price:", prices[index])
else:
    print("The price of the hardware \"" + search + "\" has not been depreciated.")

