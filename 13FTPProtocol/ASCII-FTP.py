import os
from ftplib import *


def writeLine(data):
    fl.write(data)
    fl.write(os.linesep)


activeFTP = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
file = 'README-TWO.txt'
ftp.set_pasv(activeFTP)
with open(file, 'w') as fl:
    ftp.retrlines('RETR README', writeLine)
ftp.quit()
