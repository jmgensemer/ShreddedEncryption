import codecs
import random
import string
import os

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

"""Fragments File passed
    Args:
        readFile: File that will be Fragmented
    Returns:
        Name of the first piece
"""
def splitFiles(readFile):
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
            piece.write("haltcode00")
            piece.close()
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "ab")
            piece.seek(10)
            piece.write(readf.read(lastPiece))
        else:
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "w")
            piece.write(fnames[i + 1])
            piece.close()
            piece = open("/Applications/Shredded Encryption/" + fnames[i], "ab")
            piece.seek(10)
            piece.write(readf.read(pieceSize))
        piece.close()
    readf.close()
    os.remove(readFile)
    return fnames[0]

"""Generates the size of each File Piece
    Args:
        fileSize: Size of the file you are splitting
    Returns:
        Size of for each individual piece
"""
def findSizeofPieces(fileSize):
    x = 0
    if (fileSize <= 100):
        x = 10
    elif (fileSize <= 1000):
        x = 50
    elif (fileSize <= 10000):
        x = 1000
    elif (fileSize <= 100000):
        x = 10000
    elif (fileSize <= 1000000):
        x = 100000
    elif (fileSize <= 50000000):
        x = 1000000
    elif (fileSize <= 100000000):
        x = 10000000
    elif (fileSize <= 1000000000):
        x = 100000000
    else:
        x = 1000000000
    return x

"""Combinds File Pieces to recreate Original File
    Args:
        file_tuple: A tuple that contains (Path/Filename, First Split Piece)
"""
def piece_Files(file_tuple):
    wholefile = open(file_tuple[0], "wb")
    name = file_tuple[1]
    while(name != "haltcode00"):
        open_piece = codecs.open("/Applications/Shredded Encryption/"+name,"r", encoding="utf-8")
        nextname = open_piece.read(len(name))
        open_piece.close()
        open_piece = open("/Applications/Shredded Encryption/"+name, "rb")
        open_piece.seek(len(name))
        size = os.path.getsize("/Applications/Shredded Encryption/" + name) - len(name)
        wholefile.write(open_piece.read(size))
        os.remove("/Applications/Shredded Encryption/" + name)
        name = nextname
    wholefile.close()
