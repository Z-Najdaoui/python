# Programme Python pour l'implémentation du Tri à bulle

def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]


# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]

tri_bulle(tab)

print("Le tableau trié est:")
for i in range(len(tab)):
    print("%d " %tab[i])
