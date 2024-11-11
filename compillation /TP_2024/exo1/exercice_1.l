%{
#include <stdio.h>
#include <stdlib.h>  
int num_lignes = 0;
int num_chars = 0;
%}
%%
\n              { num_lignes++; num_chars++; }
.               { num_chars++; }
%%

int main(void) {
    yylex();
    printf("Le fichier a %d lignes et %d caractères\n", num_lignes, num_chars);
    return EXIT_SUCCESS;
}
