import serial
import json
import time
from datetime import datetime

connection = ""
for port in range(10):
    try:
        connection = serial.Serial("COM" + str(port), 115200)
        print("Connected with the port: ", connection.portstr)
        break
    except serial.SerialException:
        pass
if connection != "":
    dictionary = {}
    count = 0
    while count < 10:
        answer = connection.readline()
        dictionary[str(datetime.now())] = [answer.decode('utf-8')[0:3]]
        print(answer.decode('utf-8')[0:3])
        count += 1
    with open('Temperature.json', "w") as file:
        json.dump(dictionary, file)
    connection.close()
    print("Connection closed")
else:
    print("No ports available")
