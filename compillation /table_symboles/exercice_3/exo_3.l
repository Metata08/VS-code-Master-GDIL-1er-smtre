%{
#include "tabSymbole.h"
%}
%%

[a-zA-Z_][a-zA-Z0-9_]* {
    if (!search_symbole(table, yytext)) {
    	sprintf(id,"V%d",i++);
        table = ajouter_symb(table, yytext, "Identificateur", id);
    }
}

0[xX][0-9a-fA-F]+ {
    if (!search_symbole(table, yytext)) {
    	sprintf(id,"H%d",j++);
        table = ajouter_symb(table, yytext, "Hexadécimal", id);
    }
}

0[0-7]* {
    if (!search_symbole(table, yytext)) {
    	sprintf(id,"O%d",k++);
        table = ajouter_symb(table, yytext, "Octal", id);
    }
}

[0-9]+ {
    if (!search_symbole(table, yytext)) {
    	sprintf(id,"D%d",l++);
        table = ajouter_symb(table, yytext, "Décimal", id);
    }
}

"<"|">"|"<="|">="|"=="|"!=" {
    if (!search_symbole(table, yytext)) {
    	sprintf(id,"Relat%d",m++);
        table = ajouter_symb(table, yytext, "Opérateur", id);
    }
}

"while"|"for"|"if"|"else"|"int"|"float"|"char" {
    if (!search_symbole(table, yytext)) {
        table = ajouter_symb(table, yytext, "Mot-clé","____");
    }
}

.|\n { /* Ignorer les autres caractères */ }

%%

int main(void) {
    printf("Analyse lexicale et génération de la table des symboles :\n\n");
    yylex();
    printf("\nTable des Symboles :\n");
    afficher(table);
    return 0;
}