#include <stdio.h>
#include <stdlib.h>

// Inclure les définitions générées par Flex
extern FILE *yyin;   // Flux d'entrée pour Flex
extern int yylex();  // Fonction d'analyse lexicale générée par Flex
extern char *yytext; // Texte de l'unité lexicale reconnue

int main(int argc, char *argv[])
{

    char *table[] = {
        "SI",
        "ALORS",
        "SINON",
        "TANTQUE",
        "FAIRE",
        "RETOUR",
        "ENTIER",
        "LIRE",
        "ECRIRE",
        "PLUS",
        "MOINS",
        "FOIS",
        "DIV",
        "INFERIEUR",
        "EGAL",
        "ET",
        "OU",
        "NON",
        "PARENTHESE_OUVRANTE",
        "PARENTHESE_FERMANTE",
        "ACCOLADE_OUVRANTE",
        "ACCOLADE_FERMANTE",
        "POINT_VIRGULE",
        "VIRGULE",
        "POINT_SEPARATION",
        "CARACTERE",
        "ID_VAR",
        "ID_FUNC",
        "NOMBRE",
        "FIN"};
    if (argc > 1)
    {
        // Ouvrir le fichier source
        FILE *fichier = fopen(argv[1], "r");
        if (fichier)
        {
            // Assigner le flux au fichier source pour Flex
            yyin = fichier;

            // Appeler l'analyse lexicale
            int token;
            while ((token = yylex()) != 0)
            { // yylex renvoie 0 à la fin du fichier
                printf("Token: %s Texte: %s\n", table[token - 1], yytext ? yytext : "NULL");
            }

            fclose(fichier);
        }
        else
        {
            fprintf(stderr, "Erreur : Impossible d'ouvrir le fichier %s\n", argv[1]);
            return 1;
        }
    }
    else
    {
        fprintf(stderr, "Erreur : Veuillez spécifier un fichier source à analyser.\n");
        return 1;
    }
    return 0;
}
