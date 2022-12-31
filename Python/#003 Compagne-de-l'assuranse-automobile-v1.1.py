# var age,acc,permi,contra,G,Result:entier
#     A1,P1:bool

age = int(input('Quel est vôtre âge?: '))  # سن
# عمر رخصة السياقة
permi = int(input('Combien dannées que vous avez prendre votre permis: '))
# عدد مرات التسبب في حادث
acc = int(input('Combien daccidents que vous avez déjà fait?: '))
contra = int(input(' avec nous ?: '))  # عدد سنوات تأمين سيارة

A1 = age >= 25
P1 = permi >= 2
R = contra - acc
G = 0

if (A1):
    G = G+1
if (P1):
    G = G+1

G = G + R
if (age - permi < 16) or (age-contra < 16) or (age < 16) or (age > 85) or (acc > 60) or (acc < 0) or (contra > 69) or (contra < 0) or (permi <= 0) or (permi > 69):
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
    Result = 'Blue'
else:
    Result = 'Logique Error'
if (isinstance(Result, int)):
    print('Input Error')
else:
    print(Result)
