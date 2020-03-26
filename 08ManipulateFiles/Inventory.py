from InventoryFunction import *

inventory = {}
option = callMenu()
while option>0 and option<4:
    if option == 1:
        register(inventory)
    if option == 2:
        persist(inventory)
    if option == 3:
        result = display()
        for line in result:
            list=line.split(";")
            print("Date............: ", list[1])
            print("Description.....: ", list[2])
            print("Department......: ", list[3])
    option = callMenu()
