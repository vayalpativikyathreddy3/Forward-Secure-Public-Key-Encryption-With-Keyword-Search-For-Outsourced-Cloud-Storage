
# import base64
# def peks_encrypt(keyword):
#     return base64.b64encode(keyword.encode()).decode()

# def peks_decrypt(encrypted_keyword):
#     return base64.b64decode(encrypted_keyword.encode()).decode()

# d='shivaeds'
# print(d)
# x=peks_encrypt(d)
# print(x)
# y=peks_decrypt(x)
# print(y)
# z=peks_encrypt(d)
# print(z)
# import hashlib

# def hash_string(input_string):
#     # Create a new sha256 hash object
#     sha_signature = hashlib.sha256()
    
#     # Update the hash object with the bytes of the input string
#     sha_signature.update(input_string.encode('utf-8'))
    
#     # Return the hexadecimal representation of the digest
#     return sha_signature.hexdigest()


# x='data'
# print(hash_string(x))
# y='data'
# print(hash_string(y))

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
from django.http import HttpResponse

def abe_encrypt(file):
    # Generate a random key for AES encryption
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)   # Initialization Vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt file content
    file_content = file.read()
    encrypted_content = encryptor.update(file_content) + encryptor.finalize()
    
    # Encode encrypted content and key for storage
    return (base64.b64encode(encrypted_content).decode(), base64.b64encode(key).decode(), base64.b64encode(iv).decode())

def abe_decrypt(encrypted_file, key, iv):
    encrypted_content = base64.b64decode(encrypted_file)
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_content = decryptor.update(encrypted_content) + decryptor.finalize()
    return decrypted_content
filepath= 'static/Files/file.txt'
file_path = filepath.encode('utf-8').decode()
print('---------')
print(file_path)
encrypted_file, key, iv = abe_encrypt(file_path)
print(encrypted_file)
print(key)
print(iv)
dec=abe_decrypt(encrypted_file, key, iv)
print(dec)