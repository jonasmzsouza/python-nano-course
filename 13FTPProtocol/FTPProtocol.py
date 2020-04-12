from ftplib import *

activeFTP = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
user = input("Enter user: ")
password = input("Enter password: ")
ftp.login(user, password)
print("Current work directory: ", ftp.pwd())
ftp.cwd('pub')
print("Current directory: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()
