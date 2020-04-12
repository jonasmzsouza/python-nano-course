import json
import os


def callMenu():
    entry = input("Enter:\n" +
                  "<1> To search for a new address: \n" +
                  "<2> To view information from the input file: \n" +
                  "<3> To end: ")
    if entry == "":
        choice = 0
    else:
        choice = int(entry)
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
    dictionary["address"] = [input("\nEnter the street number: "),
                             input("Enter the street name: "),
                             input("Enter the city: "),
                             input("Enter the state: "),
                             input("Enter the country: ")]
    writeFile(dictionary, file)
    return "JSON generated!"


def display(file):
    dictionary = readFile(file)
    for key, data in dictionary.items():
        print("\nStreet number.....: ", data[0])
        print("Street name.......: ", data[1])
        print("City..............: ", data[2])
        print("State.............: ", data[3])
        print("Country...........: ", data[4], "\n")
