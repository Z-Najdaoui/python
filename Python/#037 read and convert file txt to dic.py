myFile = open("file.txt","r")
list = myFile.readlines()
keys = list[0].rstrip('\n').split(';')
myDic = {}
for i in range(1,len(list)):
    for j in range(len(keys)):
        myDic[keys[j]] = list[i].rstrip('\n').split(';')[j]
    print(myDic)