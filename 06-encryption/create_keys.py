import rsa

public_key, private_key = rsa.newkeys(512)

public_file = open("keys/public.txt", "w")
private_file = open("keys/private.txt", "w")

print(public_key)
print(public_key.save_pkcs1())
print(public_key.save_pkcs1().decode('utf-8'))

public_file.write(public_key.save_pkcs1().decode('utf-8'))
public_file.close()
private_file.write(private_key.save_pkcs1().decode('utf-8'))
private_file.close()


