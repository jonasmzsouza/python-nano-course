import json
import os


def callMenu():
    choice = int(input("Enter: \n" +
                       "<1> To register asset\n" +
                       "<2> To view stored assets: "))
    return choice


def readFile(file):
    if os.path.exists(file):
        with open(file, "r") as file_json:
            dictionary = json.load(file_json)
    else:
        dictionary = {}
    return dictionary


def writeFile(dictionary, file):
    with open(file, "w") as file_json:
        json.dump(dictionary, file_json)


def register(dictionary, file):
    answer = "Y"
    while answer == "Y":
        dictionary[input("Enter the patrimonial number: ")] = (input("\nEnter the date of the last update: "),
                                                               input("Enter the description: "),
                                                               input("Enter the department: "))
        answer = input("Enter <Y> to continue.").upper()
        writeFile(dictionary, file)
    return "JSON generated!"


def display(file):
    dictionary = readFile(file)
    for key, data in dictionary.items():
        print(".............................................")
        print("Date............: ", data[0])
        print("Description.....: ", data[1])
        print("Department......: ", data[2])
        print(".............................................")
