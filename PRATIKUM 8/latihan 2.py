print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

def bintang(n):
    for i in range(1, n + 1):
        formation= "*" * (1 + (i-1)*2)
        print(formation.center(10))

bintang(4)
