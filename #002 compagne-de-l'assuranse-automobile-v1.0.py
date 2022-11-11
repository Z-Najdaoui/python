# var age,acc,permi,maison,G,Result:entier
#     A1,P1:bool
print(':ملاحضات'[::-1])
print('1-أدخل جميع معطيات على شكل أرقام '[::-1])
print(
    ' 2-يجب أن تدخل عدد سنوات التي أمنت فيها المنزل عن طريق شركتنا وكم سنة وأنت تملك رخصة السياقة'[::-1])


age = int(input('Age: '))
permi = int(input('Permi: '))
acc = int(input('Nummber accidents: '))
maison = int(input('Nombre d\'années d\'assurance la maison: '))

A1 = age >= 25
P1 = permi >= 2
R = maison - acc
G = 0

if (A1):
    G = G+1
if (P1):
    G = G+1

G = G + R
if (age - permi < 16) or (age-maison < 16) or (age < 16) or (age > 85) or (acc > 60) or (acc < 0) or (maison > 69) or (maison < 0) or (permi <= 0) or (permi > 69):
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
