a = int(input('donner l\'age du client: '))
b = int(input('donner les annes de permis : '))
c = int(input('donner le nombre d\'accident: '))
d = int(input('donner le nombre d\'annees d\'assurance: '))
if a < 25 and b < 2:
    if c == 0:
        r = 'tarif rouge'
    else:
        r = 'refuse'
elif (a < 25 and b >= 2) or (a >= 25 and b < 2):
    if c == 0:
        r = 'tarif orange'
    elif c == 1:
        r = 'tarif rouge'
    else:
        r = 'refuse'
elif (a >= 25 and b >= 2):
    if c == 0:
        r = 'tarif vert'
    elif c == 1:
        r = 'tarif orange'
    elif c == 2:
        r = 'tarif rouge'
    else:
        r = 'refuse'
if d >= 1:
    if r == 'tarif rouge':
        r = 'tarif orange'
    elif r == 'tarif orange':
        r = 'tarif vert'
    elif r == 'tarif vert':
        r = 'tarif bleu'
print('type de tarif:', r)
