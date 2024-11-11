import numpy as np

n=int(input("donner la taille du tableau : "))
def tri_a_bulles(tab):
    n = np.size(tab)
    for i in range(n):
        for j in range(i, n):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j],tab[i]
            else:  
                break
    return tab


tableau  = np.zeros(n)
print("donner les elmts du tableau : ")
for i in range(n):
    tableau[i] = int(input())
a=tri_a_bulles(tableau)

print(a)