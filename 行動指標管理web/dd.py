files = []
import ftplib
import resp
try:
    files = ftp.nlst()
except (ftplib.error_perm, resp):
    if str(resp) == "550 No files found":
        print ("No files in this directory")
    else:
        raise

for f in files:
    print (f)