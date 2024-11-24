%{
	#include <stdio.h>
%}

%%

[a-zA-Z_][a-zA-Z0-9_]* {printf("identificateur : %s\n",yytext);}

0[xX][0-9a-fA-F]+ {printf("héxadécimal : %s\n",yytext);}
0[0-7]* {printf("Octal : %s\n",yytext);}
[0-9]+ {printf("Décimal : %s\n",yytext);}

"<"|">"|"<="|">="|"=="|"<>" {printf("opération de relation : %s\n",yytext);}

"while"|"for"|"if"|"else"|"int"|"float"|"char" {printf("Mot-clé : %S\n",yytext);}

.|\n

%%

int main(void){return yylex();}