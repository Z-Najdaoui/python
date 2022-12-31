def PrixHorsTaxe(prixUnitaire, nombreArt):
    print('Prix nombre Art Est: ', prixUnitaire*nombreArt)


def TVA(prixUnitaire, nombreArt):
    print('TVA: ', round(((prixUnitaire*nombreArt)*18.6) / 100, 2))


def TTC(prixUnitaire, nombreArt):
    print('TTC: ', round((((prixUnitaire*nombreArt)*18.6)/100) +
          (prixUnitaire*nombreArt), 2))


prixUnitaire = float(input('Enter Prix Unitaire: '))
nombreArt = float(input('Enter le nomber d\'articles: '))
print("prix unitaire: ", prixUnitaire)
print("nombre d\'articles: ", nombreArt)
PrixHorsTaxe(prixUnitaire, nombreArt)
TVA(prixUnitaire, nombreArt)
print("----------------------------------")
TTC(prixUnitaire, nombreArt)
