import numpy as np

def tri_fusion (tab):
    if len(tab) <= 1:
        return tab
    mid = len(tab) // 2
    partie_gauche = tri_fusion(tab[:mid])
    partie_droite = tri_fusion(tab[mid:])
    return fusionner(partie_gauche, partie_droite)

def fusionner(gauche, droite):
    i, j = 0, 0
    resultat = []
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat


n = int(input("donner la taille du tableau : "))
tableau = np.zeros((n,), dtype=int)
print("donner les elmts du tableau : ")
for i in range(n):
    tableau[i] = int(input())
a = tri_fusion(tableau)

print(a)

