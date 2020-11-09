from operator import *

def jumlah(a,b):
    hasil = a + b
    return hasil

def kali(a,b):
    hasil = a * b
    return hasil

def kurang(a,b):
    hasil = a - b
    return hasil

def bagi(a,b):
    hasil = a / b
    return hasil
#a
x = kali(4,6)
y = jumlah(2,x)
z = kurang(y,4)

print(z)

#b
k = jumlah(4,7)
l = kurang(6,9)
m = kali(k,l)

print(m)

#c
p = jumlah(10,2)
q = jumlah(7,5)
r = kurang(12,34)
s = bagi(p,q)
t = bagi(s,r)
