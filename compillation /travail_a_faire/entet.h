#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct symbole
{
	char *mot;
	char *type;
	char *etiquette;
	struct symbole *suiv;
} Symbole;

Symbole *ajouter_symb(Symbole *tab, char *m, char *t, char *e)
{
	Symbole *nouvSym = (Symbole *)malloc(sizeof(Symbole));
	nouvSym->mot = (char *)malloc(sizeof(char) * strlen(m));
	nouvSym->type = (char *)malloc(sizeof(char) * strlen(t));
	nouvSym->etiquette = (char *)malloc(sizeof(char) * strlen(e));

	strcpy(nouvSym->mot, m);
	strcpy(nouvSym->type, t);
	strcpy(nouvSym->etiquette, e);
	nouvSym->suiv = NULL;

	if (!tab)
	{
		return nouvSym;
	}
	else
	{
		Symbole *p = tab;
		while (p->suiv)
		{
			p = p->suiv;
		}
		p->suiv = nouvSym;
		return tab;
	}
}

int search_symbole(Symbole *tab, char *mot)
{
	int tr=0;
	if (tab)
	{
		Symbole *ptr=tab;
		while (ptr)
		{
			if (strcmp(ptr->mot,mot) == 0)
			{
				tr= 1;
				break;
			}
			ptr = ptr->suiv;
		}
	}
	return tr;
}

void afficher(Symbole *tab)
{

	// printf("%*s |%*s |%*s\n", 10, " Mot", 5, "Type", "ETIQUETTE");

	Symbole *ptr = tab;

	// while (ptr)
	// {
	// 	printf("%*s |%*s |%*s\n", 5, ptr->mot, 5, ptr->type, ptr->etiquette);
	// 	ptr = ptr->suiv;
	// }

	printf(" %12s 	|	%12s 	|	%12s\n", "MOT", "TYPE", "ETIQUETTE");

	while (ptr)
	{
		printf(" %12s 	|	%12s 	|	%12s\n", ptr->mot, ptr->type, ptr->etiquette);
		ptr = ptr->suiv;
	}
}

void detruir_liste(Symbole *tab)
{
	Symbole *p = tab;
	while (p != NULL)
	{

		while (p->suiv != NULL)
		{
			p = p->suiv;
		}
		free(p->mot);
		free(p->type);
		free(p->etiquette);
		free(p);
		p = tab;
	}
	printf("Liste détruite\n");
}