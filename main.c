#include "read_file.h"
int main(int argc, char* argv[]){
	FILE * open_file, *tester_file;
	
	open_file = fopen(argv[1], "rb");
	
	encrypt_File(open_file, "tester", "/home/jmgensemer/desktop/abc.c");
	
	tester_file = fopen("tester", "rb");
		
	decrypt_File(tester_file,"here.dmg");
	
	
	
	fclose(tester_file);
	fclose(open_file);
	return 0;
}