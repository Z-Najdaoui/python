def leTriParInsertion(tableau):
    for i in range(1,len(tableau)):
        post = tableau[i]
        j=i

        while j>0 and tableau[j-1] > post:
            tableau[j]=tableau[j-1]
            j=j-1

        tableau[j] = post
    
    
    print(tableau)

tableau = []
e=1
print('\nenter \'s\' for stop!\n')
while True:
    arrs = input('number-'+str(e)+' : ')
    if arrs == 's':
        break
    arrs = int(arrs)
    tableau.append(arrs)
    e+=1
leTriParInsertion(tableau)



    
    











