#include "read_file.h"
const char * file_Type(char filename []){
	int i = 0, j = 0;
	int file_length = strlen(filename) - 1;
	static char type[5];
	
	while(i < file_length){
		if(filename[i] == '.'){
			i++;
			for(; i <= file_length; i++, j++)
				type[j] = filename[i];
		}
		i++;
	}
	return type;	
}

const char * read_Message(FILE * file){
	int i = 1, j = 0;
	static char message[10000001];
	char character;
	
	while(1)
	   {
	      character = fgetc(file);
	      if( feof(file) ){
	          break;
	      }
	      if(i%3 == 0){
			  message[j] = character;
			  j++;
	      }
		  i++;
	   }
	   return message;
}

void decrypt_File(FILE * file, char filename[]){
	FILE * write_file;
	write_file = fopen(filename, "wb");
	int counter = 1;
	char character;
	
	while(1){
	      character = fgetc(file);
	      if( feof(file) ){
	          break ;
	      }
		  if(counter%3){
			  fputc(character, write_file);
		  } 
		  counter++;
	  }  
	  fclose(write_file);
}

void encrypt_File(FILE * file, char filename[], char message[]){
	FILE * encrypted_file;
	
	encrypted_file = fopen(filename, "wb");
	int counter = 1, j = 0;
	char character;
	
	while(1){
	      character = fgetc(file);
	      if( feof(file) ){
	          break;
	      }
		  if(counter%3 == 0){
			  if(j < strlen(message)){
			  	fputc(message[j], encrypted_file);
			  	j++;
				counter++;
		  	  } else {
		  	  	fputc('0', encrypted_file);
				counter++;
		  	  }
		  } 
		  fputc(character,encrypted_file);
		  counter++;
	  }  
	  
	  fclose(encrypted_file);	
}


void splitFiles(FILE * readFile, int filesize, int pieceSize){
	int splitNumber = (filesize/pieceSize) + 1;
	int lastPiece = (int) filesize % pieceSize;
	int i,j;


	FILE * pieces[splitNumber];
	unsigned char storage1[pieceSize + 1];
	unsigned char storage2[lastPiece + 1];
	
	for (i = 0 ,j = 0; i < splitNumber ; i++, j += pieceSize ){
	
		if(i == splitNumber-1){
			fseek(readFile, j, SEEK_SET);
			fread(&storage2, 1, lastPiece, readFile);
			pieces[i] = fopen(randomFileName(), "wb");
			fwrite(&storage2, 1, lastPiece, pieces[i]);
			
		} else {
			pieces[i] = fopen(randomFileName(), "wb");
			fseek(readFile, j, SEEK_SET);
			fread(&storage1, 1, pieceSize, readFile);
			fwrite(&storage1, 1, pieceSize, pieces[i]);
		}
		
		fclose(pieces[i]);
	}
	
}

const char * randomFileName(){
	char c= 'a';
	char *string = (char*) malloc (sizeof(char) * 11);
	int i;
	for ( i =0; i <10; i++){
		string[i] = c + (rand() %26);
	}
	string[10] = '\0';
	return string;
}


int fileSize(FILE * file){
	int size = 0;
	fseek(file,0L, SEEK_END);
	size = ftell(file);
	fseek(file,0L, SEEK_SET);
	return size;	
}

int findSizeofPieces(int fileSize){
	if (fileSize <= 100){
		return 10;
	} else if (fileSize <= 1000){
		return 50;
	} else if (fileSize <= 10000){
		return 1000;
	} else if (fileSize <= 100000){
		return 10000;
	} else if (fileSize <= 1000000){
		return 100000;
	} else if (fileSize <= 50000000){
		return 1000000;
	} else if (fileSize <= 100000000){
		return 10000000;
	} else if (fileSize <= 1000000000){
		return 100000000;
	} 
	return 1000000000;
}


void piece_Files(FILE * file, char[] piece, int location){
  FILE * open_piece;
  open_piece = fopen(piece,"rb");
  unsigned char storage[fileSize(open_piece];
			/*
  Open piece, check message, write open_piece to file
  if it's the last piece, return, else recursively get next file)

			 */


}


