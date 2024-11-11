%{
#include <stdio.h>
#include <stdlib.h>

int occurrences[26] = {0};
%}

%%

[a-z]   { occurrences[yytext[0] - 'a']++; }
.|\n  ;
%%
int main() {
    yylex();
    printf("Lettre:  |  Occurrences:\n");
    for (int i = 0; i < 26; i++) {
        printf("%c: %d\n", 'a' + i, occurrences[i]);
    }
    return EXIT_SUCCESS;
}k