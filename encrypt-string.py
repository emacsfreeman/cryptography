from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()

# Encode the message
message = "my deep dark secret"
encoded = message.encode()

# Encrypt the message
f = Fernet(key)
encrypted = f.encrypt(encoded)

# Get the key again (for the demonstration)
file = open('key.key', 'rb')
key2 = file.read() # The key will be type bytes
file.close()

# Decrypt the encrypted message
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)

# Decode the message
original_message = decrypted.decode()
print(original_message)
