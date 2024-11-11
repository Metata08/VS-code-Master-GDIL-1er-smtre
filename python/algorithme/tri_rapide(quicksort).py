import  numpy as np

def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab) // 2]
    elements_inf = [x for x in tab if x < pivot]
    elements_eq = [x for x in tab if x == pivot]
    elements_sup = [x for x in tab if x > pivot]
    return tri_rapide(elements_inf) + elements_eq + tri_rapide(elements_sup)



n = int(input("donner la taille du tableau : "))
tableau = np.zeros((n,), dtype=int)
print("donner les elmts du tableau : ")
for i in range(n):
    tableau[i] = int(input())
a = tri_rapide(tableau)

print(a)