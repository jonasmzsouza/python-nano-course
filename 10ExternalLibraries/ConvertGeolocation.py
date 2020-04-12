from pygeocoder import Geocoder
from function import *
import sys

EntryFileName = "data_entry.json"
OutputFileName = "data_output.json"
search = readFile(EntryFileName)
option = callMenu()

while option != "":
    if option == 1:
        print(register(search, EntryFileName))

        list = search["address"]
        address = list[0] + "," + list[1] + " " + list[2] + " " + list[3] + " " + list[4]
        output = {"Coordinates": Geocoder('Place_your_API_key_here').geocode(address).coordinates}
        writeFile(output, OutputFileName)

    elif option == 2:
        display(EntryFileName)
        option = callMenu()

    elif option == 3:
        sys.exit()

    else:
        option = callMenu()


