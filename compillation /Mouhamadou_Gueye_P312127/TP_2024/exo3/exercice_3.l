%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
 
[a-z A-Z_][a-zA-Z0-9_]*    {
                              printf("Identificateur: %s\n", yytext);
                           }

0[xX][0-9a-fA-F]+          { printf("Hexadécimal: %s\n", yytext); }  
0[0-7]+                    { printf("Octal: %s\n", yytext); }        
[1-9][0-9]*|0              { printf("Décimal: %s\n", yytext); }      

"<="                       { printf("Opérateur relationnel: <=\n"); }
"<>"                       { printf("Opérateur relationnel: <>\n"); }
"<"                        { printf("Opérateur relationnel: <\n"); }
"=="                       { printf("Opérateur relationnel: ==\n"); }
">="                       { printf("Opérateur relationnel: >=\n"); }
">"                        { printf("Opérateur relationnel: >\n"); }

"while"                    { printf("Mot clé: while\n"); }
"for"                      { printf("Mot clé: for\n"); }
"if"                       { printf("Mot clé: if\n"); }
"else"                     { printf("Mot clé: else\n"); }
"int"                      { printf("Mot clé: int\n"); }
"float"                    { printf("Mot clé: float\n"); }
"char"                     { printf("Mot clé: char\n"); }


[ \t\n]+                  

.                          { printf("Caractère non reconnu: %s\n", yytext); }

%%

int main(void) {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
