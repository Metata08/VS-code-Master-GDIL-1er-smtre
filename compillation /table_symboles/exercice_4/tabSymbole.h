#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct symbole {
    char *mot;
    char *type;
    char *etiquette;
    struct symbole *suiv;
} Symbole;

Symbole *table = NULL;
int i=0, j=0, k=0, l=0, m=0;
char id[10];

Symbole *ajouter_symb(Symbole *tab, char *m, char *t, char *e) {
    Symbole *nouvSym = (Symbole *)malloc(sizeof(Symbole));
    nouvSym->mot = strdup(m);
    nouvSym->type = strdup(t);
    nouvSym->etiquette = strdup(e);
    nouvSym->suiv = NULL;

    if (!tab) {
        return nouvSym;
    } else {
        Symbole *p = tab;
        while (p->suiv) {
            p = p->suiv;
        }
        p->suiv = nouvSym;
        return tab;
    }
}


int search_symbole(Symbole *tab, char *mot) {
    Symbole *ptr = tab;
    while (ptr) {
        if (strcmp(ptr->mot, mot) == 0) {
            return 1; // Trouvé
        }
        ptr = ptr->suiv;
    }
    return 0; // Non trouvé
}

void afficher(Symbole *tab) {
    printf("\n%-15s | %-15s | %-20s\n", "MOT", "TYPE", "ETIQUETTE");
    printf("-----------------------------------------------\n");

    Symbole *ptr = tab;
    while (ptr) {
        printf("%-15s | %-15s | %-18s\n", ptr->mot, ptr->type, ptr->etiquette);
        ptr = ptr->suiv;
    }
}


void detruir(Symbole *tab)
{
    Symbole *p = tab;
    while (p!= NULL)
    {
        Symbole *tmp = p->suiv;
        free(p->mot);
        free(p->type);
        free(p->etiquette);
        free(p);
        p = tmp;
    }
    free(tab);
    printf("Liste détruite\n");
}