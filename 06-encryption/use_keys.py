import rsa

public_file = open("keys/public.txt", "r")
public_text = public_file.read()
public_key = rsa.PublicKey.load_pkcs1(public_text, "PEM")

private_key = open("keys/private.txt", "r")
private_text = private_key.read()
private_key = rsa.PrivateKey.load_pkcs1(private_text, "PEM")

message = input("Type message: ")

# encrypt message and print it
message_bytes = message.encode('utf-8')
message_encrypted = rsa.encrypt(message_bytes, public_key)

print(message_encrypted)

# decrypt message and print it
original_bytes = rsa.decrypt(message_encrypted, private_key)
original = original_bytes.decode('utf-8')

print(original)
