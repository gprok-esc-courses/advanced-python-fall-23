import re 

alphanum_re = re.compile(r'[^a-zA-Z0-9]')

txt = input("Give some text, only alphanumeric characters allowed: ")

s = alphanum_re.search(txt)

if not s:
    print(txt)
else:
    print("Invalid char found")