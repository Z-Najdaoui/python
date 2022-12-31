# Le jeu de pendu
def MotValid(mot, n):
    if (n > 25 or n < 4):
        print("##\nNumber of caracter need to be between 4 and 25.\n##")
        return False
    for el in mot:
        if (ord(el) > 90 or ord(el) < 65):
            print("##\nCaracters need to be (A-B,Majuscules).\n##")
            return False
    print("\n"*100)
    print("Game Started")
    return True
#---------------
def convertirCH(mot):
    return list(mot)
#---------------


def initialiserSolution():
    while True:
        mot = input("Enter mot(4-24 majuscules):")
        n = len(mot)
        if MotValid(mot, n):
            Tcar = convertirCH(mot)
            return [Tcar,n]
            break
#---------------


def creerEssai(n):
    t = ['*'] * n
    return t
# Tessai = creerEssai(10)
# print(Tessai)
#---------------


def afficherC(Tcar, n):
    TcarStr = ''
    for i in range(n):
        TcarStr = TcarStr + Tcar[i]
    print(TcarStr)
#---------------
def jouer(Tcar, TEssai, caracter, n):
    ThereIs = False
    for i in range(n):
        if Tcar[i] == caracter:
            TEssai[i] = Tcar[i]
            ThereIs = True
    if ThereIs:
        print('\nLucky :)')
        print(TEssai)
        print()
    if not(ThereIs):
        print('\nOh Nooo :(')
        print(TEssai)
        print()
    return [ThereIs,TEssai]
# jouer(['a','b','c','c'],['*','*','*','*'],'b',4)
#---------------
def estFini(TEssai,n):
    for i in range(n):
        if TEssai[i] == '*':
            return False
    return True
#---------------
'''This the last part where I will call my funtions'''
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("^^                                           ^^")
print("^^         Welcom in \"Jeu du pendu\"          ^^")
print("^^                                           ^^")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
R = initialiserSolution()
essais = 0
n = R[1]
Tcar = R[0]
TEssai = creerEssai(n)

while True:
    caracter = input('Enter Caracter: ')
    R2 = jouer(Tcar, TEssai, caracter, n)
    if not(R2[0]):
        essais+=1
        if essais == 5:
            print('The word was:',end=" ")
            afficherC(Tcar,n)
            print('\n\nPendu')
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^        ___________________           ^")
            print("^       ||------------------           ^")
            print("^       ||               |             ^")
            print("^       ||            _(+Q+)_          ^")
            print("^       ||              /|\            ^")
            print("^       ||              / \            ^")
            print("^       ||                             ^")
            print("^     __||_______________              ^")
            print("^     -------------------              ^")
            print("^                                      ^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            break
    else:
        if estFini(R2[1],n):
            print("suuuuper, you complete the Word ---->",end=' ')
            afficherC(Tcar,n)
            print("\n\ngagné")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^       |   |^^^|   |                  ^")
            print("^       |   |0 0|   |                  ^")
            print("^        \   \ O/   /                  ^")
            print("^         \___||___/                   ^")
            print("^            |  |                      ^")
            print("^            |__|                      ^")
            print("^            /  \                      ^")
            print("^           /    \                     ^")
            print("^          |      |                    ^")
            print("^                                      ^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            break