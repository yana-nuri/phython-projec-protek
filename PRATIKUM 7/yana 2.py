print ("=========================YANA NURIKA============================")
print ("===========================K3520079=============================")
def dataStat(x):
    a = sum(x) / len(x)
    b = max(x)
    c = min(x)

    datasd = [a,b,c]

    return datasd

while True :
    try :
        n = int(input("Berapa banyak data yang inging anda input ? (Input dalam angka) : "))
        break
    except ValueError:
        print ("Inputan Invalid")
        continue

data = []

i = 0

while (i < n):
    try:
        bil = int(input("Masukan bilangan bulat yang anda inginkan : "))
        data.append(bil)
        i += 1

    except ValueError:
        print ("Inputan Invalid")

printData = dataStat (data)
print(printData)
