import csv
myFile = open("file.csv","r")
ptr = csv.DictReader(myFile,delimiter=";")
for ligne in ptr:
    print(ligne)
    