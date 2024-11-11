#ifndef ANNUAIRE_INCLUDED_H
#define ANNUAIRE_INCLUDED_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>



#define taille_max 3
typedef struct
{
    char *cle;
    char *val;
} elmt;

typedef elmt *Annuaire;

Annuaire creer_annuaire()
{
    Annuaire A = (Annuaire)malloc(taille_max * sizeof(elmt));
    if (A == NULL)
    {
        printf("Erreur lors de l'allocation de mémoire.\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < taille_max; i++)
    {
        A[i].cle = NULL;
        A[i].val = NULL;
    }

    return A;
}

int put(Annuaire A, char *cle, char *val)
{
    int i;
    for (i = 0; i < taille_max && A[i].cle != NULL; i++)
        if (strcmp(A[i].cle, cle) == 0)
        {
            printf("Cette clé existe déjà.\n");
            return 0;
        }

    if (i == taille_max)
    {
        printf("Annuaire plein.\n");
        return 0;
    }

    A[i].cle = strdup(cle);
    A[i].val = strdup(val);
    return 1;
}

char *get(Annuaire A, char *cle)
{
    int i;
    for (i = 0; i < taille_max && A[i].cle != NULL; i++)
    {
        if (strcmp(A[i].cle, cle) == 0)
            return A[i].val;
    }
    printf("Cette clé n'existe pas.\n");
    return NULL;
}

int supprimer_elmt(Annuaire A, char *cle)
{
    int i;
    for (i = 0; i < taille_max && A[i].cle != NULL; i++)
    {
        if (strcmp(A[i].cle, cle) == 0)
        {
            free(A[i].cle);
            free(A[i].val);
            A[i].cle = NULL;
            A[i].val = NULL;
            return 1;
        }
    }
    printf(" !!! Cette clé n'existe pas.\n");
    return 0;
}

void liberer_annuaire(Annuaire A)
{
    for (int i = 0; i < taille_max; i++)
    {
        if (A[i].cle != NULL)
        {
            free(A[i].cle);
            free(A[i].val);
        }
    }
    free(A);
    printf("Annuaire libéré.\n");
}

int recherche(Annuaire A, char *cle)
{
    int i;
    for (i = 0; i < taille_max && A[i].cle != NULL; i++)
    {
        if (strcmp(A[i].cle, cle) == 0)
        {
            printf("=============================\n");
            printf("cle: %s\n", A[i].cle);
            printf("val: %s\n", A[i].val);
            printf("=============================\n");

            return 1;
        }
    }
    printf(" !!! Cette clé n'existe pas.\n");
    return 0;
}

#endif 
