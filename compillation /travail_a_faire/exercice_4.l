%{
	#include "entet.h"
	int num_lignes = 0;
	int num_chars = 0;
	int num_comments = 0;
	int count=0;
	char id[5]="";
	char func[100]="";
	Symbole *tab=NULL;
%}

%%
\n 		{num_lignes++; num_chars++;}
. 		{num_chars++;}

[0-9]+ 	{printf("entier trouvé : %s\n",yytext);}

"/*"([^*]*"*"+)*"/"	{num_comments++;}
"//".*				{num_comments++;}

[a-zA-Z_][a-zA-Z0-9_]*\( 	{
	if (search_symbole(tab,yytext)==0)
	{
		sprintf(id,"F%d",count++);
		sprintf(func,"%s )",yytext);
		tab = ajouter_symb(tab,func,"Fonction",id);
    }
	
	//printf("nom de la  fonction trouvée : %10s  | Type : Fonction | Etiquette : F%d  \n", yytext,count);

	}

%%

int main(void){
	yylex();
	afficher(tab);
	printf("total lignes : %d\n",num_lignes);
	printf("total caractères : %d\n",num_chars);
	printf("total commentaires : %d\n",num_comments);
	detruir_liste(tab);
	return 0;
}
