def callMenu():
    choice = int(input("Enter:\n" +
                       "<1> To register asset\n" +
                       "<2> To persist in file\n" +
                       "<3> To view stored assets: "))
    return choice


def register(dictionary):
    answer = "Y"
    while answer == "Y":
        dictionary[input("Enter the patrimonial number: ")] = [
            input("\nEnter the date of the last update: "),
            input("Enter the description: "),
            input("Enter the department: ")]
        answer = input("Enter <Y> to continue.").upper()


def persist(dictionary):
    with open("./files/inventory.csv", "a") as inv:
        for key, value in dictionary.items():
            inv.write(key + ";" + value[0] + ";" +
                      value[1] + ";" + value[2] + "\n")
    return "Persisted successfully!"


def display():
    with open("./files/inventory.csv", "r") as inv:
        lines = inv.readlines()
    return lines
