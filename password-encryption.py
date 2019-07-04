# Source: https://youtu.be/H8t4DJ3Tdrg

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "passwords" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes

salt = b'\x9d\xa0\x1a\xee\x14B(T6\x86\xe3|y\xbe\xa1\x00'
kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
print(key)
