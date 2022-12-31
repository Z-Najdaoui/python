# <calcule la moyanne>

# vars
# a, c,d,ac,cc,dc,laMoyenne :entier

# m,f,i #:entier


# debut
m = 7
i = 2
f = 5
# notes
a = str(input(":أدخل نقطة الرياضيات"[::-1]))
c = str(input(":أدخل نقطة اللغة الفرنسية"[::-1]))
d = str(input(":أدخل نقطة الإسلاميات"[::-1]))

# coefficients
ac = str(a*m)
cc = str(c*f)
dc = str(d*i)

# la moyenne
laMoyenne = (str(ac + cc + dc)) / (m+i+f)

# fin
print('la Moyenne est : ', round(laMoyenne, 2), '/20')
