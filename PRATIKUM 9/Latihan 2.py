print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

file = open("file.txt", "a")

i = True
while ( i == True) :
    nim = input("Masukkan NIM : ")
    namaMhs = input("Masukkan Nama Mhs : ")
    alamat = input("Masukkan Alamat : ")

    file.write(nim + "|" + namaMhs + "|" + alamat + "\n")
    ulangi = input("Ulangi input lagi (y/n) : ")

    if (ulangi == "y") :
        i = True
    elif  (ulangi == "n"):
        i = False
    else :
        print ("Inputan anda tidak valid")
        continue

file.close()
