import serial

connection = ""
for port in range(10):
    try:
        connection = serial.Serial("COM" + str(port), 115200, timeout=0.5)
        print("Connected with the port: ", connection.portstr)
        break
    except serial.SerialException:
        pass
if connection != "":
    connection.close()
    print("Connection closed")
else:
    print("No ports available")



