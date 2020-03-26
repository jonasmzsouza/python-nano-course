from function import *

inventory = readFile("inventory_json.json")
option = callMenu()

while 0 < option < 3:
    if option == 1:
        print(register(inventory, "inventory_json.json"))
    elif option == 2:
        display("inventory_json.json")
    option = callMenu()

