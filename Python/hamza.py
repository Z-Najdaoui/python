def PriHansTae(pu,nd):
    pht=pu*nd
    return pht
    
def TVA(pht):
    TVA2= pht*0.18
    return TVA2

def TTC(TVA,pht):
    TTC2=pht+TVA
    print('TTC= ',TTC2)

pu=float(input('ecrer le pri unitaire'))
nd=float(input('ecrer le nombre da '))

r =PriHansTae(pu,nd)
print('Pri hans tae ',r)
rr=TVA(r)
print('TVA',rr)
TTC(rr,r)
