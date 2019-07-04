# Source: https://youtu.be/H8t4DJ3Tdrg

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
key = file.read() # The key will be type bytes
file.close()

# Open to the file to encrypt
with open('texte-a-chiffrer.txt.encrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

# Write the encrypted file
with open('texte-a-chiffrer.txt.decrypted', 'wb') as f:
    f.write(encrypted)

    
