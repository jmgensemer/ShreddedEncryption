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











