# var age,acc,permi,contra,G,Result:entier
#     A1,P1:bool

contra = (input('Est ce que vous déjà une assurance avec nous?oui/non: '))

if (contra == 'non'):
    age = int(input('Quel est vôtre âge?: '))  # سن
    # عمر رخصة السياقة
    permi = int(input('Combien dannées que vous avez prendre votre permis: '))
    # عدد مرات التسبب في حادث
    acc = int(input('Combien daccidents que vous avez déjà fait?: '))

    A1 = age >= 25
    P1 = permi >= 2
    G = 0

    if (A1):
        G = G+1
    if (P1):
        G = G+1

    G = G - acc

    if ((age - permi < 16) or (age < 16) or (age > 85)
       or (acc > 60) or (acc < 0) or (permi <= 0) or (permi > 69)):
        Result = 0
    elif (G <= (-1)):
        Result = 'Refuse de l\'assurer'
    elif (G == 0):
        Result = 'Rouge'
    elif (G == 1):
        Result = 'Orange'
    elif (G == 2):
        Result = 'Vert'
    elif (G >= 3):
        Result = 'Bleu'
    else:
        Result = 'Logique Error'
    if (isinstance(Result, int)):
        print('Input Error')
    else:
        print(Result)
elif (contra == 'oui'):

    colour = input('Quel est votre type colour: ')
    acc = int(input('Combien daccidents que vous avez déjà fait?: '))
    age = int(input('Quel est vôtre âge?: '))
    permi = int(input('Combien dannées que vous avez prendre votre permis: '))

    if (colour == 'rouge'):
        G = 0
    elif (colour == 'orange'):
        G = 1
    elif (colour == 'vert'):
        G = 2
    elif (colour == 'bleu'):
        G = 3
    elif (colour):
        G = -100

    if (age == 25):
        G = G+1
    if (permi == 2):
        G = G+1

    G = G + 1
    G = G - acc

    if ((age - permi < 16) or (age < 16) or (age > 85)
       or (acc > 60) or (acc < 0) or (permi <= 0) or (permi > 69)):
        Result = 0
    elif (G <= (-70)):
        Result = 0
    elif (G <= (-1)):
        Result = 'Refuse de l\'assurer'
    elif (G == 0):
        Result = 'Rouge'
    elif (G == 1):
        Result = 'Orange'
    elif (G == 2):
        Result = 'Vert'
    elif (G >= 3):
        Result = 'Bleu'
    else:
        Result = 'Logique Error'
    if (isinstance(Result, int)):
        print('Input Error')
    else:
        print(Result)
