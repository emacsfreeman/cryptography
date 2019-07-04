# Source: https://youtu.be/H8t4DJ3Tdrg

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('key.key', 'wb')
file.write(key) # The key is type bytes
file.close()
