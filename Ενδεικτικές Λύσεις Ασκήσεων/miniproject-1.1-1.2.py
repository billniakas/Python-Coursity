# Εισαγωγή στον Προγραμματισμό με Python
# Εβδομάδα 1
# Ενδεικτικες λύσεις mini-project
#===================================================
# Άσκηση 1.1

import math as ma

x = int(input('x = '))
y = int(input('y = '))

print('Πηλίκο x/y: {:10.5f}'.format(x/y))
print('Yπόλοιπο x%y: {:10d}'.format(x%y))
print('Λογάριθμος x με βάση το y: {:10.5f}'.format(ma.log(x,y)))
print('Τετραγωνική ρίζα του x: {:10.5f}'.format(ma.sqrt(x)))
print('e**x: {:10.5f}'.format(ma.exp(x)))


#===================================================
# Άσκηση 1.2

import math as ma
R = 6372.8

p1 = float(input('Πλάτος 1ου: '))
m1 = float(input('Μήκος 1ου: '))
p2 = float(input('Πλάτος 2ου: '))
m2 = float(input('Μήκος 2ου: '))

dp = ma.radians(p1-p2)
dm = ma.radians(m1-m2)

a = ma.sin(dp/2)**2 + ma.cos(ma.radians(p1))*ma.cos(ma.radians(p2))*ma.sin(dm/2)**2
c = 2*ma.asin(ma.sqrt(a))

d = R*c

print('Ζητούμενη απόσταση 1-2: {:12.5} km'.format(d))
