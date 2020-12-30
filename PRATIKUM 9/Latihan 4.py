print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

McrNim = input("Masukkan NIM yang mau dicari : ")
file = open("file.txt", "r")
isiFile = file.readlines()

for i in range(len(isiFile)) :
    Mahasiswa = isiFile[i]
    a,b,c= Mahasiswa.split("|")
    if (a == McrNim) :
        data = "Ada"
        print("Data Mahasiswa")
        print("NIM   : ", a)
        print("Nama   : ", b)
        print("Alamat   :", c)
        break

    else :
        data = "Tidak Ada"

if (data=="Tidak Ada") :
    print ("Data mahasiswa tidak ditemukan")
