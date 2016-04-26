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
    path = "/Applications/ShreddedEncryption/FragmentedFiles/"
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
            piece = open(path + fnames[i], "w")
            piece.write(change_filename("haltcode00"))
            piece.close()
            piece = open(path + fnames[i], "ab")
            piece.seek(10)
            piece.write(readf.read(lastPiece))
        else:
            piece = open(path + fnames[i], "w")
            piece.write(change_filename(fnames[i + 1]))
            piece.close()
            piece = open(path + fnames[i], "ab")
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
    path = "/Applications/ShreddedEncryption/FragmentedFiles/"
    wholefile = open(file_tuple[0], "wb")
    name = change_filename(file_tuple[1])
    while(name != "haltcode00"):
        open_piece = codecs.open(path+name,"r", encoding="utf-8")
        nextname = open_piece.read(len(name))
        open_piece.close()
        open_piece = open(path+name, "rb")
        open_piece.seek(len(name))
        size = os.path.getsize(path + name) - len(name)
        wholefile.write(open_piece.read(size))
        os.remove(path + name)
        name = change_filename(nextname)
    wholefile.close()
    decrypt_file(file_tuple[0], key)

"""append \0 to the passed text to make its length divisible by 16.
    Args:
        s: plaintext in bytes
    Uses:
        block_size = 16 (Size of a data block (in bytes))
    Returns:
        edited text after padding which its length is now divisible by 16       
"""
def pad(plaintext):
    return plaintext + b"\0" * (AES.block_size - len(plaintext) % AES.block_size)

"""encrypt a plaintext using the key and AES 256-bit key
    it uses Cipher-Block Chaining (CBC).
    Args:
        plaintext: a line of text
        key: the key used to encrypt the plaintext
    Returns:
        cipheredtext
"""
def encrypt_text(plaintext, key):
    plaintext = pad(plaintext)
    iv = Random.new().read(AES.block_size)
    ciphertext = AES.new(key, AES.MODE_CBC, iv)
    return iv + ciphertext.encrypt(plaintext)

"""decrypt a cipheredtext using the key and AES 256-bit key
    it uses Cipher-Block Chaining (CBC).
    Args:
        cipheredtext: a line of cipheredtext
        key: the key used to decrypt the cipheredtext
    Returns:
        plaintext
"""
def decrypt_text(cipheredtext, key):
    iv = cipheredtext[:AES.block_size]
    ciphertext = AES.new(key, AES.MODE_CBC, iv)
    plaintext = ciphertext.decrypt(cipheredtext[AES.block_size:])
    return plaintext.rstrip(b"\0")

"""it reads in a file in bytes and it encrypts its content
    using encrypt_text(plaintext, key) function.
    Args:
        fileinName: name of file to be encrypted
        key: the key used to encrypt the file content
"""
def encrypt_file(fileinName, key):
    fileoutName = fileinName + '.enc'
    with open(fileinName, 'rb') as f:
        plaintext = f.read()
    cipheredtext = encrypt_text(plaintext, key)
    with open(fileoutName, 'wb') as f:
        f.write(cipheredtext)
        os.remove(fileinName)
        os.rename(fileoutName,fileinName)

"""it reads in a file in bytes and it decrypts its content
    using decrypt_text(cipheredtext, key) function.
    Args:
        fileinName: name of file to be decrypted
        key: the key used to encrypt the file content
"""
def decrypt_file(fileinName,key):
    fileoutName = fileinName + '.dec'
    with open(fileinName, 'rb') as f:
        ciphertext = f.read()
    plaintext = decrypt_text(ciphertext, key)
    with open(fileoutName, 'wb') as f:
        f.write(plaintext)
    os.remove(fileinName)
    os.rename(fileoutName, fileinName)

"""Generates a 256-bit key using time and date information.
    Returns:
        key in bytes
"""
def getKey():
    password = bytes(memoryview(time.ctime().encode()))
    dk = hashlib.pbkdf2_hmac('sha256', password, b'salt', 100000)
    return dk


