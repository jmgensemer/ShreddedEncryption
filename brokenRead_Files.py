import codecs
import random
import string
import os
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import time



"""Generates a 10 character long string
    Args:
        size: Always 10
        char: Ascii values allowed in name
    Returns:
        random string, size of 10
"""
def filename_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

"""Generates a list of random Filenames
    Args:
        nameamounts: How many random names need to be generated
    Returns:
        list of random names
"""
def filenames(nameamounts):
    x = []
    for i in range(nameamounts):
        x.append(filename_generator())
    return x

def change_filename(filename):
    return ''.join((filename[1], filename[0], filename[9], filename[4], filename[3], filename[8], filename[7], filename[6], filename[5], filename[2]))


"""Fragments File passed
    Args:
        readFile: File that will be Fragmented
    Returns:
        Name of the first piece
"""
def splitFiles(readFile,key):
    encrypt_file(readFile, key)
    readf = open(readFile,"rb")
    filesize = os.path.getsize(readFile)
    pieceSize = findSizeofPieces(filesize)
    splitNumber = (int)(filesize/pieceSize) + 1
    lastPiece = filesize % pieceSize
    fnames = filenames(splitNumber)
    j = 0
    for i in range(splitNumber):
        if (i == splitNumber - 1):
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "w")
            piece.write(change_filename("haltcode00"))
            piece.close()
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "ab")
            piece.seek(10)
            piece.write(readf.read(lastPiece))
        else:
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "w")
            piece.write(change_filename(fnames[i + 1]))
            piece.close()
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "ab")
            piece.seek(10)
            piece.write(readf.read(pieceSize))
        piece.close()
    readf.close()
    os.remove(readFile)
    return change_filename(fnames[0])

"""Generates the size of each File Piece
    Args:
        fileSize: Size of the file you are splitting
    Returns:
        Size of for each individual piece
"""
def findSizeofPieces(fileSize):
    x = 0
    if (fileSize <= 100):
        x = 5
    elif (fileSize <= 1000):
        x = 25
    elif (fileSize <= 10000):
        x = 500
    elif (fileSize <= 100000):
        x = 5000
    elif (fileSize <= 1000000):
        x = 50000
    elif (fileSize <= 50000000):
        x = 500000
    elif (fileSize <= 100000000):
        x = 5000000
    elif (fileSize <= 1000000000):
        x = 50000000
    else:
        x = 500000000
    return x

"""Combinds File Pieces to recreate Original File
    Args:
        file_tuple: A tuple that contains (Path/Filename, First Split Piece)
"""
def piece_Files(file_tuple,key):
    wholefile = open(file_tuple[0], "wb")
    name = change_filename(file_tuple[1])
    while(name != "haltcode00"):
        open_piece = codecs.open("/Applications/Shredded Encryption/"+name,"r", encoding="utf-8")
        nextname = open_piece.read(len(name))
        open_piece.close()
        open_piece = open("/Applications/Shredded Encryption/"+name, "rb")
        open_piece.seek(len(name))
        size = os.path.getsize("/Applications/Shredded Encryption/" + name) - len(name)
        wholefile.write(open_piece.read(size))
        os.remove("/Applications/Shredded Encryption/" + name)
        name = change_filename(nextname)
    wholefile.close()
    decrypt_file(file_tuple[0], key)

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
        os.remove(file_name)
        os.rename(fileout_name,file_name)

def decrypt_file(file_name,key):
    fileout_name = file_name + '.dec'
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt_text(ciphertext, key)
    with open(fileout_name, 'wb') as fo:
        fo.write(dec)
    os.remove(file_name)
    os.rename(fileout_name, file_name)

def getKey():
    password = bytes(memoryview(time.ctime().encode()))
    dk = hashlib.pbkdf2_hmac('sha256', password, b'salt', 100000)
    return dk


