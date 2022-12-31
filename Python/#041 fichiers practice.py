#### put in src_of_desktop you desktop src
###   ||
###   ||
###   ||
###   \/
src_of_desktop = '/home/najdaoui/Desktop/'


#######################################
nom_fichier = 'monfichier.txt'
def exer_1_1():
    global monfile
    monfile = open(src_of_desktop+nom_fichier ,'x')
    monfile.close()

    monfile = open(src_of_desktop+nom_fichier ,'w',encoding='utf-8')
    monfile.write('Python est un langage de programmation oriente objet.')
    monfile.close()
def exer_1_2():
    monfile = open(src_of_desktop+nom_fichier ,'r')
    print(monfile.read())
    monfile.close()
#######################################
nom_fichier1 = 'myFile.txt'
def exer_2_1():
    global monfile1
    monfile1 = open(src_of_desktop+nom_fichier1 ,'x')
    monfile1.close()

    monfile1 = open(src_of_desktop+nom_fichier1 ,'w',encoding='utf-8')
    for i in range(5):
        monfile1.write('Ligne numero '+str(i+1)+'\n')
    monfile1.close()
def exer_2_2():
    global monfile1
    monfile1 = open(src_of_desktop+nom_fichier1 ,'r+')
    monlist = monfile1.readlines()
    monfile1.close()
    monfile1 = open(src_of_desktop+nom_fichier1 ,'w',encoding='utf-8')
    monlist.insert(2,'desole ! le contenu de cette ligne a ete change !')
    for i in range(len(monlist)):
        monfile1.write(monlist[i])
    monfile1.close()
#######################################
nom_fichier2 = 'myFile2.txt'
def exer_3_1():
    global monfile3
    monfile3 = open(src_of_desktop+nom_fichier2  ,'x')
    monfile3.close()

    monfile3 = open(src_of_desktop+nom_fichier2 ,'w',encoding='utf-8')
    monfile3.write('Python est un langage de programmation souple et flexible.')
    monfile3.close()
    ##1-ajouter
    monfile3 = open(src_of_desktop+nom_fichier2 ,'a',encoding='utf-8')
    monfile3.write('\nCe contenu a ete ajoute via un code Python !')
    monfile3.close()
#######################################
nom_fichier4 = 'myFile4.txt'
def exer_4_1():
    global monfile4
    monfile4 = open(src_of_desktop+nom_fichier4 ,'x')
    monfile4.close()

    monfile4 = open(src_of_desktop+nom_fichier4 ,'w',encoding='utf-8')
    monfile4.write('Python est le meilleur langage de programmation.')
    monfile4.close()

def exer_4_2():
    global monfile4
    monfile4 = open(src_of_desktop+nom_fichier4 ,'r+')
    line = monfile4.readlines()[0].split(' ')
    line.pop(4)
    monfile4.close()
    monfile4 = open(src_of_desktop+nom_fichier4 ,'w',encoding='utf-8')
    monfile4.write(' '.join(line))
    monfile4.close()

#######################################

'''_______________________________________________________________'''

'''1'''
# exer_1_1()
# exer_1_2()
'''2'''
# exer_2_1()
# exer_2_2()
'''3'''
# exer_3_1()
'''4'''
# exer_4_1()
# exer_4_2()
'''_______________________________________________________________'''
# Coded By Zobair Najdaoui