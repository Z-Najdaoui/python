# this's a python programme ask the user (N) number of tables and a (n) length of all this table
# and gives after user enter all values some helful things(la moyenne, sum ...)

##Enter N and n 
while True:
    N = int(input('Enter number of the tableau : '))

    if N > 0:
        break
while True:

    n = int(input('Enter lenght of tableu(s) : '))
    if n > 0:
        break


## Tabs in one tab
I = 1
tabOfAllTabs = []
while I <= N:
    print('\n')
    Ti = []

    for i in range(1, n+1):
        num = float(
            input('Enter the number ('+str(i)+') in tableau ('+str(I)+') :'))
        Ti.append(num)
    tabOfAllTabs.append(Ti)
    I += 1


## The tabels in default state
def default(tab):
    for i in range(0, N):
        print('-Tab ('+str(i+1)+') : ', tab[i])


## tab1 + tab2 + ... + tabN
tabPlustab = []
for q in range(0, N):
    y = 0
    for u in range(0, n):
        y = y + tabOfAllTabs[q][u]
    tabPlustab.append(y)


# Moynne of every tab
everyTab = []
for i in range(0, N):
    sum = 0
    for j in range(0, n):
        sum += tabOfAllTabs[i][j]
    everyTab.append(round(sum/n, 2))


# moyenne of all tabs
allTabs = 0
len = len(everyTab)
for i in range(0, len):
    allTabs += everyTab[i]
allTabs = allTabs/len


# The big number in tab minus The small number
tabBigMinusSmall = []
def bigMinusSmall(tab):
    for i in range(0, N):
        tab[i] = sorted(tab[i])
        tabBigMinusSmall.append(tab[i][-1]-tab[i][0])
    return tabBigMinusSmall
tabBigMinusSmall = bigMinusSmall(tabOfAllTabs)


# ask and give the user
while True:

    ask = input('\n\n**Enter \'s\' to stop!\n\nWhat do you want: \n\t0:The tabels in default state.\n\t1:All \
tab in one(matrice).\n\t2:Sum of every tab.\n\t3:Moyenne of every tab.\n\t4:Moyenne of all tab.\n\t5:big - small number in every tab\nThe choix number: ')
    print('\n')
    print('____________________________________________\n')
    if ask == 's':
        print('Okay :) closing ...')
        print('____________________________________________')
        break
    elif ask == '0':
        print('The tabels in default state :\n')
        default(tabOfAllTabs)
    elif ask == '1':
        print('All tables in one :', tabOfAllTabs)
    elif ask == '2':
        print('The sum fo all tabels : ', tabPlustab)
    elif ask == '3':
        print('Moyenne of every tab :', everyTab)
    elif ask == '4':
        print('Moyenne of all tab :', round(allTabs, 2))
    elif ask == '5':
        print('The big number in every tab minus The small number : \n',
              tabBigMinusSmall)

    else:
        print('No command found :(')
    print('____________________________________________')
