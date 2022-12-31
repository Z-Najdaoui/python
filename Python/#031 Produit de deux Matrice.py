# <produit de deux matirice>

# Function matrice1 x matrice2

def produit(m1, m2):
    finalMatrice = []
    # get final matrie with content '0' for make it easy to add any number on it
    for i in range(0, lFinalMatirice):
        finalMatrice.append([])
        for j in range(0, cFinalMatirice):
            finalMatrice[i].append(0)

    for i in range(0, lFinalMatirice):  # put the poduit in finalMatrice
        for j in range(0, cFinalMatirice):
            for q in range(0, len(m1)):
                finalMatrice[i][j] += m1[q][j]*m2[i][q]  # culule produit
    #             print(finalMatrice)
    #         print("*1----*")
    #     print("*2----*")
    # print("*3----*")

    return finalMatrice
print('                        ____Produit of Two Matrices____\n')
print('||   It\'s Important to make "the line of matrice 1/2" = "colonnes of matrice 2/1"  ||\n')

# Enter lines and colonnes of fist and second matrice
while True:
    line1 = int(input('Enter number of lines in matirice 1 : '))
    col1 = int(input('Enter number of colonnes in matirice 1 : '))
    line2 = int(input('Enter number of lines in matirice 2 : '))
    col2 = int(input('Enter number of colonnes in matirice 2 : '))

    if line1 == col2:  # help variables
        a = 1
        l = line1
        c = col2
        cFinalMatirice = col1
        lFinalMatirice = line2
        break
    if line2 == col1:
        a = 2
        l = line2
        c = col1
        cFinalMatirice = col2
        lFinalMatirice = line1
        break


# The loops for include the matrices values
matrice1 = []
matrice2 = []

# Matrice 1 and 2
for m in range(1, 3):
    print('\nMatrice ', m, ' : ')

    if m == 1:  # Matrice 1
        for i in range(0, line1):
            m1 = []
            for j in range(0, col1):
                print('\t-Enter Value of ,line (', i+1,
                      ') colonne (', j+1, ') : ', end='')
                m1.append(float(input('')))
            print()
            matrice1.append(m1)
        print('______________________________________\n')

    else:  # Matrice 2
        for i in range(0, line2):
            m2 = []
            for j in range(0, col2):
                print('\t-Enter Value of ,line (', i+1,
                      ') colonne (', j+1, ') : ', end='')
                m2.append(float(input('')))
            print()
            matrice2.append(m2)

        print('______________________________________\n')
    print('')
if a == 2:  # switch and put matrice that we use her lines in matrice number 1
    r = matrice1
    matrice1 = matrice2
    matrice2 = r

# The suolution
result = produit(matrice1, matrice2)  # call funtion
print('\n*************************************************************\nInput:')
print('\t___________________/Matrices\___________________\n')
print('\tMatrice 1 : ', matrice1, '\n\tMatrice 2 : ', matrice2, '\n\nOutput:')
# final output
print('\n\t___________________/Style 1\___________________\n')
print('\tMatrice 1 x Matrice 2 : ', result)

# Another style(Not important)
print('\n\t___________________/Style 2\___________________\n')
print('\tMatrice 1 x Matrice 2 :')
print('\t __\n\t|')
for i in range(0, lFinalMatirice):
    print('\t|', end='  ')
    for j in range(0, cFinalMatirice):
        print(result[i][j], end='  ')
    print('')
print('\t|__')
print('\n*************************************************************')
