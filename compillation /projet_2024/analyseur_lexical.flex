%{
#include <stdio.h>
#include "symboles.h"
%}

entier   [0-9]
id_var  \$[a-zA-Z][a-zA-Z0-9_]*
id_function [a-zA-Z_][a-zA-Z0-9_]*\( 

%%
{entier}+              { return NOMBRE; }
{id_var}               { return ID_VAR; }
{id_function}          { return ID_FUNC; }
"si"                   { return SI; }
"alors"                { return ALORS; }
"sinon"                { return SINON; }
"tantque"              { return TANTQUE; }
"faire"                { return FAIRE; }
"retour"               { return RETOUR; }

"lire"                 { return LIRE;}
"ecrire"                { return ECRIRE; }

"("                    { return PARENTHESE_OUVRANTE; }
")"                    { return PARENTHESE_FERMANTE; }
"*"                    { return FOIS; }
"/"                    { return DIV; }
"+"                    { return PLUS; }
"-"                    { return MOINS; }
"<"                    { return INFERIEUR ; }
"="                    { return EGAL; }
"&"                     { return ET; }
"|"                    { return OU; }
"!"                   {return NON ;}

"lire"                 { return LIRE; }
"{"                    { return ACCOLADE_OUVRANTE; }
"}"                    { return ACCOLADE_FERMANTE; }

";"                    { return POINT_VIRGULE; }
","                    { return VIRGULE; }
"tantque"              { return TANTQUE; }


[ \t\n]+               { /* Ignorer espaces, tabulations, retours à la ligne */ }
"#"[^'\n']*            { /* Ignorer les commentaires */ }
%%

int yywrap() { return 1; }