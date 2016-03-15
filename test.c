#include "aes.h"
#include "read_file.h"
#include <time.h>

int main() {
	time_t time0 = time(NULL);
	FILE *fileIN, *fileOUT;
	int i,j;	

	unsigned char temp[32] = {0x00  ,0x01  ,0x02  ,0x03  ,0x04  ,0x05  ,0x06  ,0x07  ,0x08  ,0x09  ,0x0a  ,0x0b  ,0x0c  ,0x0d  ,0x0e  ,0x0f};	

	//*********************************************************
	// The KeyExpansion routine must be called before encryption.
	time_t time1;
	time_t time2;
	fileIN = fopen ("tester.mp3", "rb");
	fileOUT = fopen ("EncryptedFile.txt", "wb");
	time1 = time(NULL);
	CipherHelper(fileIN, fileOUT, fileSize(fileIN), 1, temp);
	time2 = time(NULL);
	printf("Time took to Encrypted File =  %f\n\n", difftime(time2, time1));

//	       *********************************************************
	fileIN = fopen ("EncryptedFile.txt", "rb");
	fileOUT = fopen ("DecryptedFile.mp3", "wb");
	time1 = time(NULL);
	CipherHelper(fileIN, fileOUT, fileSize(fileIN), 0, temp);
	time2 = time(NULL);
	printf("Time took to Decrypted File =  %f\n\n", difftime(time2, time1));

	time_t time4 = time(NULL);
	printf("Time took The program to complete =  %f\n\n", difftime(time4, time0));
	return 0;
}