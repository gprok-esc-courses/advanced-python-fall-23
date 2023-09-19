import re

email = input("Give email: ")

email_re = re.compile(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]{2,3}$')

s = email_re.search(email)

if not s:
    print("Invalid email")
else:
    print(email)