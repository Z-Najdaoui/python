# <somme d'argent donne>
# var num50,num20,num1,num2:entier
# debut
num50 = int(input('Nombre de billets de cinquante dirhams:'))
num20 = int(input('Nombre de billets de vingt dirhams:'))
num2 = int(input('Le nombre de pièces en coupures de deux dirhams:'))
num1 = int(input('Le nombre de pièces en coupure un dirham:'))
somme = (num50*50 + num20*20 + num2*2 + num1*1)
# fin
print('La somme d\'argent est :', somme, 'DH')
