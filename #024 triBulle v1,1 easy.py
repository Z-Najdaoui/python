T = [8,3,1]

while True:
    
    change = False
    
    for i in range(0,len(T)-1):
        
        if T[i] > T[i+1]:

            r = T[i]
            T[i] = T[i+1]
            T[i+1] = r

            change = True


    if change == False:
        print(T)
        break
