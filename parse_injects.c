
/* parse_injects.c - naive CSV reader; not production-ready */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    FILE *f = fopen("injects_master.csv","r");
    if(!f){ perror("open"); return 1; }
    char line[2048];
    int row=0;
    while(fgets(line,sizeof(line),f)){
        if(row==0){ row++; continue; } // skip header
        char *p = strtok(line,",");
        int col=0;
        while(p){
            if(col==0) printf("ID:%s ", p);
            if(col==1) printf("Minute:%s ", p);
            if(col==2) printf("Phase:%s ", p);
            if(col==4) printf("Message:%s ", p);
            p = strtok(NULL,",");
            col++;
        }
        printf("\\n");
        row++;
    }
    fclose(f);
    return 0;
}
