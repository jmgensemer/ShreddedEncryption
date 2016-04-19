from Crypto import Random
from Crypto.Cipher import AES
import hashlib, binascii
import time
import os

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

def encrypt_file(file_name, key):
    fileout_name = file_name + '.enc'
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt_text(plaintext, key)
    with open(fileout_name, 'wb') as fo:
        fo.write(enc)
    os.system('rm ' + file_name)
    os.system('mv ' + fileout_name + ' ' + file_name)

def decrypt_file(file_name,key):
    fileout_name = file_name + '.dec'
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt_text(ciphertext, key)
    with open(fileout_name, 'wb') as fo:
        fo.write(dec)
    os.system('rm ' + file_name)
    os.system('mv ' + fileout_name + ' ' + file_name)

def getKey():
    password = bytes(memoryview(time.ctime().encode()))
    dk = hashlib.pbkdf2_hmac('sha256', password, b'salt', 100000)
    return dk

#key = getKey()
key = b'\xd4h\x9a\xa9c\xc5\xb4\xc4\x00) \xb3?\xa6u\xff\xb7Y\xbe\xbd\x7fN7:\x95\x1bB`\x1bB~\r'
print("Encrypting")
encrypt_file('fire.mp3', key)
print("Decrypting")
decrypt_file('fire.mp3', key)
print(time.clock() - start)