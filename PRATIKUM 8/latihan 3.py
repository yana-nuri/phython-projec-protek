print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

def bintang(n):
    puncak = int(n / 2 + 1)
    
    for i in range(1, n + 1):
        formation = "*" * (1 + (i-1)*2)
        print(formation.center(20))

        if(i == puncak):
            for i in range(puncak -1, 0, -1):
                formation = "*" * (1 + (i-1)*2)
                print(formation.center(20))
            break

bintang(7)
