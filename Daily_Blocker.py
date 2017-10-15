# This script will block distracting websites for specific working hours .....
# Working Hours are from 9am to 2pm
import time
from datetime import datetime as dt

# Basically we redirect the url of websites to local host.
redirect="127.0.0.1"
websites = ["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]
# path of host file in Linux.
file_path = "/etc/hosts"

while True:
    # if time is in my working hours , write some lines in hosts file .
    print(dt.now())
    
    file = open(file_path, 'r+')
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        content = file.read()
        for website in websites:
            if website in content:
                continue
            else:
                file.write(redirect+"    "+website+"\n")
    else :
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
                file.truncate()
    time.sleep(5)



