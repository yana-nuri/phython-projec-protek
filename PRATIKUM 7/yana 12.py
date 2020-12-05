print ("=========================YANA NURIKA============================")
print ("===========================K3520079=============================")
buah = {'apel'   : 5000,
        'jeruk'  : 8500,
        'mangga' : 7800,
        'duku'   : 6500}

def jumlahBuah(namaBuah):
    jumlah = int(input('Berapa Kg : '))
    harga = buah.get(namaBuah, 0)*jumlah
    return harga

def tukuBuah(buahDict):
    print('Daftar Buah : ')

    for a,b in buah.items():
        print ('- ',a, ' : ' ,b)

    total =[]
    lanjutTidak = True

    while (lanjutTidak == True) :
        namaBuah = input('\n Nama buah yang akan anda beli : ').lower()

        if (namaBuah not in buahDict.keys ()):
            print ('Maaf buah yang anda masukan tidak invalid atau tidak ada dari daftar menu kami ')
            continue
        else :
            try:
                harga = jumlahBuah (namaBuah)
                total.append(harga)
                pilihan = input('Apakah anda ingin beli buah yang lainnya juga (y/n) ? ').lower()

                if (pilihan == 'y'):
                    lanjutTidak = True
                elif (pilihan == 'n'):
                    lanjutTidak = False
                else:
                    print('Inputan Anda Tidak Valid')
                    break
            except TypeError:
                    print ('Tolong periksa kembali inputan anda karena terjadi kesalah, mungkin anda tidak menyantumkan perintah (y/n) ')
                    continue
            except ValueError:
                    print('\n Inputan anda Invalid silahkan coba kembali')
                    continue
    print ('===============================')
    print ('Total harga buah yang dibeli : ' , sum(total))

def nambahBuah(buahDict):
    namaBuahBaru = input('Masukan nama buah : ').lower()

    while True:
        try:
            if(namaBuahBaru in buahDict.keys() ):
                print ('Buah ', namaBuahBaru, 'buah sudah didalam data anda, silahkan masukan harga buahnya ?')
                hargaBuahBaru = int(input('\n Masukan harga buah dalam bentuk angka : '))

                dictBuahBaru = {namaBuahBaru : hargaBuahBaru}
                buahDict.update(dictBuahBaru)

                print('Data Buah : ')

                for a,b in buah.items() :
                    print ('- ' ,a, '(harga : ' ,b, ')')
            else:
                hargaBuahBaru = int(input('\n masukan harga dalam bentukan angka : '))

                print('Data Buah : ')

                for a,b in buah.items() :
                    print('- ' ,a, '(harga : ' ,b, ')')
            break
        except ValueError:
            print ('\n Inputan Invalid silahkan coba lagi ')
            continue
def menghapusBuah(buahDict):
    hapusBuah = input('masukan nama buah yang anda ingin hapus : ').lower()
    if(hapusBuah in buahDict.keys()):
        del buahDict [hapusBuah]
        print('Buah ', hapusBuah, 'buah yang ingin anda hapus sudah berhasil')

        print('\n Data Buah : ')
        for a,b in buah.items():
            print ('- ' ,a, '(harga : ' ,b, ')')
        else:
            print('Buah yang diinginkan tidak ada dalam menu kami')

print ('Daftar menu : ')
print ('a. Tambah Data Buah')
print ('b. Beli Buah')
print ('c. Hapus Buah Di Dalam Menu Buah')
print ('10. Keluar')

while True :
    pilihanDaftarMenu = input('\n pilihan Menu : ').lower()

    if(pilihanDaftarMenu == 'a'):
        nambahBuah(buah)
    elif(pilihanDaftarMenu == 'b'):
        tukuBuah(buah)
    elif(pilihanDaftarMenu == 'c'):
        menghapusBuah(buah)
    elif(pilihanDaftarMenu == '10'):
        break
    else:
        print('oops inputan anda ada yang salah, tolong periksa kembali')
        continue
    
                                
        
            
