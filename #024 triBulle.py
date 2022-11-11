def triBulle(tab):
    n = len(tab)

    for i in range(1,n):
        for j in range(0, n-1):
            if tab[j] > tab[j+1]:
                 tab[j], tab[j+1] = tab[j+1], tab[j]
                
    return tab

tableu = []
e=1
print('enter \'s\' for stop!')
while True:
    arrs = input('number-'+str(e)+' : ')
    if arrs == 's':
        break
    arrs = int(arrs)
    tableu.append(arrs)
    e+=1
print(triBulle(tableu))
