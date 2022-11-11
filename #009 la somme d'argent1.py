# <somme d'argent>
# var Money,n50,n20,n2,n1,left:entier
Money = int(input('Hom much money you have:'))
n50 = Money // 50
left = Money % 50
n20 = left // 20
left = left % 20
n2 = left // 2
left = left % 2
n1 = left
print('You have:', '\"', n50, '\"', '50Dhs')
print('     and:', '\"', n20, '\"', '20Dhs')
print('     and:', '\"', n2, '\"', '2Dhs')
print('     and:', '\"', n1, '\"', '1Dh')
