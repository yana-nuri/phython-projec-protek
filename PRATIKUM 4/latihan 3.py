def faktorial(n):
    faktorialN=1
    while(n>0):
        faktorialN=faktorialN*n
        n-=1
    return faktorialN

def kombinasi(n,b):
    c=a-b

    hasil=faktorial(a)/faktorial(b)*faktorial(c)
    print(hasil)

def permutasi(a,b):
    c=a-b

    hasil=faktorial(a)/faktorial(c)
    print(hasil)

a=5
b=3
kombinasi(a,b)

x=10
y=7
permutasi(x,y)
