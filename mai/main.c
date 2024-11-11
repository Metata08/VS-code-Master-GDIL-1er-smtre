#include "annuaire.h"

int main()
{
    Annuaire ann = creer_annuaire();

    put(ann, "cle1", "la premiere cle 1");
    put(ann, "cle2", "la deuxieme cle 2");
    put(ann, "cle1", "la nouvelle valeur pour la cle 1");
    put(ann, "cle3", "la troisieme cle 3");

    recherche(ann, "cle1");

    printf("Valeur pour cle1 : %s\n", get(ann, "cle1"));

    supprimer_elmt(ann, "cle1");

    // pour s'assurer de la suppression
    recherche(ann, "cle1");

    liberer_annuaire(ann);

    return 0;
}