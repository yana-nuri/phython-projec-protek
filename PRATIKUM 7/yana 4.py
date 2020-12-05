print ("=========================YANA NURIKA============================")
print ("===========================K3520079=============================")
sayur = ['bayam','kangkung','wortel','selada']

def tambahSayur():
    sayurBaru = input("Masukan nama sayuran yang ingin anda tambahkan : ")
    sayur.append(sayurBaru)
    return sayur

def hapusSayur():
    sayurHapus = input("Masukan nama sayur yang ingin anda hapus : ")
    sayur.remove(sayurHapus)
    return sayur

def readSayur():
    print (sayur)

print ("apa yang program bisa lakukan buatmu : ")
print ("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print("0. Keluar")

while True:
    print()
    opsi = input("Pilihan Anda : ")

    if(opsi =='A' or opsi == 'a'):
        tambahSayur()

    elif(opsi =='B' or opsi == 'b'):
        hapusSayur()

    elif(opsi =='C' or opsi == 'c'):
        readSayur()

    elif(opsi == '0'):
        break
    else :
        print ('invutan invalid')
        continue
    
