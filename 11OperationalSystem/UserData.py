import getpass
from datetime import datetime

print("User...........: ", getpass.getuser())
print("Date...........: ", datetime.now())
print("Day............: ", datetime.now().day)
print("Month..........: ", datetime.now().month)
print("Year...........: ", datetime.now().year)
print("Hour...........: ", datetime.now().hour)
print("Minute.........: ", datetime.now().minute)
print("Second.........: ", datetime.now().second)
print("Micro Second...: ", datetime.now().microsecond)
