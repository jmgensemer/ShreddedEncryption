from Crypto import Random
from Crypto.Cipher import AES
import hashlib, binascii
import time

start = time.clock()

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt_text(plaintext, key):
    plaintext = pad(plaintext)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext)

def decrypt_text(cipheredtext, key):
    iv = cipheredtext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(cipheredtext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, fileout_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt_text(plaintext, key)
    with open(fileout_name, 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, fileout_name,key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt_text(ciphertext, key)
    with open(fileout_name, 'wb') as fo:
        fo.write(dec)

def getKey():
    password = bytes(memoryview(time.ctime().encode()))
    dk = hashlib.pbkdf2_hmac('sha256', password, b'salt', 100000)
    return dk

key = getKey()
print("Encrypting")
encrypt_file('fire.mp3', 'Encrypted.enc', key)
print("Decrypting")
decrypt_file('Encrypted.enc', 'newfire.mp3', key)
print(time.clock() - start)