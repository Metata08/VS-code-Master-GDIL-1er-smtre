import numpy as np


def tri_par_insertion (tab):
    for i in range(1,np.size(tab)):
        cle=tab[i]
        j=i-1
        while j>=0 and cle<tab[j]:
            tab[j+1]=tab [j]
            j-=1
        tab[j+1]=cle

    return tab


n = int(input("donner la taille du tableau : "))
tableau = np.zeros((n,), dtype=int)
tableau
print("donner les elmts du tableau : ")
for i in range(n):
    tableau[i] = int(input())
a = tri_par_insertion(tableau)

print(a)
