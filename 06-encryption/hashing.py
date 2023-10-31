import hashlib

hashed_value = "7110eda4d09e062aa5e4a390b0a572ac0d2c0220"

password = input("Give your password: ")

password_bytes = password.encode('utf-8')
password_hash = hashlib.sha1(password_bytes)

if password_hash.hexdigest() == hashed_value:
    print("Enter the system")
else:
    print("Wrong credentials")
