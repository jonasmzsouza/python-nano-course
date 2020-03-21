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
    print("Description: ",hardwares[index])
    print("Price......: ", prices[index])
    print("Serial.....: ", serials[index])
    print("Department.: ", departments[index])
    print("----------------------------------")