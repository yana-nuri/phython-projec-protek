print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

from datetime import  *
import os

if (os.path.exists('dataDiriPeminjamanBuku.txt')) :
    fileTeksMode = 'a'
else :
    fileTeksMode = 'w'
fileTeks = open('dataDiriPeminjamanBuku.txt', fileTeksMode)

while True :
    kode = input('Masukkan Kode Member   : ')
    nama = input('Masukkan Nama Member   : ')
    judul = input('Masukkan Judul Buku   : ')

    hariPeminjaman = date.today()
    hariDikembalikan = hariPeminjaman + timedelta(days = 7 )

    dataDiriPeminjam = [kode, nama, judul, str(hariPeminjaman), str(hariDikembalikan), '\n']
    fileTeks.write('|'.join(dataDiriPeminjam))

    ulang = input('Ulangi lagi (y/n) : ')
    if (ulang == 'y' or ulang == 'Y') :
        continue
    elif (ulang == 'n' or ulang == 'N') :
        break
    else :
        print('masukkan input yang benar')

fileTeks.close()
