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
        print('- ' ,a, ' : ' ,b)

    total =[]
    lanjutTidak = True

    while (lanjutTidak == True):
        namaBuah = input('\n Nama buah yang akan anda beli : ').lower()

        if (namaBuah not in buahDict.keys ()):
            print ('Maaf nama buah yang anda masukan tidak invalid atau tidak ada ')
            continue
        else :
            try :
                harga = jumlahBuah (namaBuah)
                total.append(harga)
                pilihan = input('Apakah anda ingin beli buah yang lain juga atau tidak (y/n) ? ').lower()

                if (pilihan == 'y' ):
                    lanjutTidak = True
                elif (pilihan == 'n'):
                    lanjutTidak = False
                else :
                    print('Inputan Tidak Valid')
                    break
            except TypeError:
                print ('Tolong ikuti arahan dari kami yah, silahkan gunakan simbol (y/n), Terimakasih')
                continue
            except ValueError:
                print ('\n inputan Invalid silahkan coba lagi ')
                continue
    print ('=================================')
    print ('Total hagar buah yang harus yang dibeli anda : ' , sum(total))
def namaBuah(buahDict) :
    namaBuahBaru = input('Masukan nama buah : ').lower()

    while True:
        try:
            if(namaBuahBaru in buahDict.keys() ):
                print('Buah', namaBuahBaru, 'Buah sudah didalam data anda. silahkan masukan harga buahnya ? ')
                hargaBuahBaru = int(input('\n Masukan harga buah dalam bentuk angka : '))

                dictBuahBaru = {namaBuahBaru : hargaBuahBaru}
                buahDict.update(dictBuahBaru)

                print('Data Buah : ')
                for a,b in buah.items() :
                        print('- ' ,a, '(harga : ' ,b, ')')
            else:
                hargaBuahBaru =int(input('\n Masukan harga buah dalam bentuk angka : '))
                buah[namaBuahBaru] = hargaBuahBaru

                print('Data Buah : ')

                for a,b in buah.items() :
                    print('- ' ,a, '(harga : ' ,b, ')')
            break
        except ValueError :
            print('\n Inputan Invalid silahkan coba lagi ')
            continue
print('Daftar menu buah : ')
print('a. Tambahkan data buah')
print('b. Beli buah')
print('10. Keluar')

while True :
    pilihanDaftarMenu = input('\n Pilihan Menu : ').lower()

    if(pilihanDaftarMenu == 'a'):
        namaBuah(buah)
    elif(pilihanDaftarMenu == 'b'):
        tukuBuah(buah)
    elif(pilihanDaftarMenu == '10'):
        break
    else:
        print('oops inputan anda ada yang salah silahkan periksalagi ')
        continue
    

                    
                    
                    
