%{
#include "tabSymbole.h"
int count[25] = {0}; //tableau pour les lettres 'a' à 'z'
%}
%%
[a-z] {if (!search_symbole(table, yytext)) {
    	sprintf(id,"Let_%d",j++);
        table = ajouter_symb(table, yytext, "Lettre", id);
    }
    count[yytext[0] - 'a']++;}
.|\n {/*ignorer tous les autres caratères*/}
%%
int main(void){
	yylex();
	for(int i=0; i<26; i++){
		if (count[i]>0){
			printf("%c : %d\n", 'a' + i , count[i]);
		}
	}
	afficher(table);
	return 0;
}