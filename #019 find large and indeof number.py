numero = 0
grandNumber = 0
for i in range(1, 3):
    a = (input('Enter le nomber numero'+str(i)+': '))
    if a > grandNumber:
        grandNumber = a
        numero = i
print('Le p-lus grand de ces nombres est: ',
      grandNumber, '\nc\'est le nombre numero: ', numero)
