import serial

connection = ""
for port in range(10):
    try:
        connection = serial.Serial("COM" + str(port), 115200)
        print("Connected with the port: ", connection.portstr)
        break
    except serial.SerialException:
        pass
if connection != "":
    while True:
        answer = connection.read()
        if answer == b'1':
            print("LED ON")
        else:
            print("LED OFF")
    connection.close()
    print("Connection closed")
else:
    print("No ports available")
