#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#ifndef READ_FILE_H_
#define READ_FILE_H_

const char * file_Type(char []);
const char * read_Message(FILE *);
void decrypt_File(FILE *, char []);
void encrypt_File(FILE *,char[], char []);
void splitFiles(FILE *, int, int);
const char * randomFileName();
int fileSize(FILE *);
int findSizeofPieces(int);


#endif // READ_FILE_H_
