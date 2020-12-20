print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

import random

def randomyanaString(x, n):
    listRandom = []

    for i in range(n):
        a = list(random.sample(x, len(x)))
        b = ''.join(a)

        if(b in listRandom):
            continue
        else:
            listRandom.append(b)
            print (b)

teks = input("Masukan teks yang ingin kamu acak : ")
n = int(input("Berapa banyak hasil acakan yang kamu inginkan ? "))

randomyanaString(teks,n)
