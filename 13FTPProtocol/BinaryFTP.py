from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('/pub/linux/logos/pictures')
with open('father_of_linux.jpg', 'wb') as file:
    ftp.retrbinary('RETR linus-father-of-linux.jpg', file.write)
ftp.quit()
