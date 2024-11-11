import numpy as np


def tri_par_selection(tab):
    n = np.size(tab)

    for i in range(n):
        min = tab[i]
        indice_min = i
        for j in range(i+1, n):
            if min > tab[j]:
                min = tab[j]
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab


n = int(input("donner la taille du tableau : "))
tableau = np.zeros((n,), dtype=int)
tableau
print("donner les elmts du tableau : ")
for i in range(n):
    tableau[i] = int(input())
a = tri_par_selection(tableau)

print(a)
