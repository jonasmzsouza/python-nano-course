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
    action = input("Enter:\n" +
                   "< ON > To ON\n" +
                   "< OFF > To turn OFF: ").upper()
    while action == "ON" or action == "OFF":
        if action == "ON":
            connection.write(b'1')
        else:
            connection.write(b'0')
        action = input("Enter:\n" +
                       "< ON > To ON\n" +
                       "< OFF > To turn OFF: ").upper()
    connection.close()
    print("Connection closed")
else:
    print("No ports available")