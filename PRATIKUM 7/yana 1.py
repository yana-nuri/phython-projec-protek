print ("====================================YANA NURIKA==================================")
print ("======================================K3520079===================================")
while True :
    try :
        n = int(input("Berapa banyak data yang ingin anda input ? (Input dalam angka) : "))
        break
    except ValueError :
        print ("Input Invalid")
        continue

data =[]

i = 0

while (i < n):
    try :
        bil = int(input("Masukan bilangan bulat yang anda inginkan : "))
        data.append(bil)
        i += 1

    except ValueError :
            print ("inputan Invalid")

data.sort(reverse = True)
print(data)
