#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#ifndef READ_FILE_H_
#define READ_FILE_H_

const char * file_Type(char []);

const char * read_Message(FILE *);

void decrypt_File(FILE *, char []);

void encrypt_File(FILE *, char [], char []);
#endif // READ_FILE_H_