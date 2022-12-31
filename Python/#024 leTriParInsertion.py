def leTriParInsertion(T):
    for i in range(1,len(T)):
        pos =i-1
        # print(T)
        while pos>=0 and T[pos]>T[i]:
            pos-=1
        pos+=1
        r = T[i]
        for j in range(i-1,pos+1,-1):
            T[j+1]=T[j]
        T[pos] = r
    
    print(T)


def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        #on insère l'élément à sa place
        tableau[j]=en_cours
    print(tableau)



tableau = []
e=1
# print('\nenter \'s\' for stop!\n')
# while True:
#     arrs = input('number-'+str(e)+' : ')
#     if arrs == 's':
#         break
#     arrs = int(arrs)
#     tableau.append(arrs)
#     e+=1
tableau = [4,3,2,1]
tri_insertion(tableau)



    
    











