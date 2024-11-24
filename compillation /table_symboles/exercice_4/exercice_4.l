%{
	#include "tabSymbole.h"

	int num_lignes = 0;
	int num_chars = 0;
	int num_comments = 0;
%}

%%
\n 		{num_lignes++; num_chars++;}
. 		{num_chars++;}

[0-9]+ 	{
	if (!search_symbole(table, yytext)) {
    	sprintf(id,"Entier_%d",++i);
        table = ajouter_symb(table, yytext, "Entier", id);
    }
}

"/*"([^*]*"*"+)*"/"	{num_comments++;}
"//".*				{num_comments++;}

[a-zA-Z_][a-zA-Z0-9_]*\( 	{
	if (!search_symbole(table, yytext)) {
    	sprintf(id,"fonc_%d",++j);
        table = ajouter_symb(table, yytext, "fonction", id);
    }
}

%%

int main(void){
	yylex();
	printf("total lignes : %d\n",num_lignes);
	printf("total caractères : %d\n",num_chars);
	printf("total commentaires : %d\n",num_comments);
	afficher(table);
	detruir(table);

	return 0;
}
