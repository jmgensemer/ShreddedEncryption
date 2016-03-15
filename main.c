#include "read_file.h"
int main(int argc, char* argv[]){
	FILE * open_file;
	
	open_file = fopen(argv[1], "rb");
	
	
	splitFiles(open_file, fileSize(open_file) , findSizeofPieces(fileSize(open_file)));
	fclose(open_file);
	return 0;

}
