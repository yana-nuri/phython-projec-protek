print ("=========================YANA NURIKA============================")
print ("===========================K3520079=============================")
buah = {'apel'   : 5000,
        'jeruk'  : 8500,
        'mangga' : 7800,
        'duku'   : 6500}

def jumlahBuah():
    jumlah = int(input('Berapa Kg : '))
    harga = buah.get(namaBuah, 0)*jumlah
    return harga

print ('Daptar Buah : ')
for a,b in buah.items():
    print ('- ' ,a, ' : ' ,b)

total =[]
lanjutTidak = True

while (lanjutTidak == True):
    namaBuah = input ('\n Nama buah yang akan anda beli : ').lower()

    if (namaBuah not in buah.keys ()):
        print('maaf buah yang anda cari tidak valid atau tidak ada' )
        continue
    else:
        try:
            harga = jumlahBuah ()
            total.append(harga)

            pilihan = input ('Apa mau beli buah yang lainnya atau tidak (y/n) ? ').lower()
            if (pilihan == 'y'):
                lanjutTidak = True
            elif (pilihan == 'n'):
                lanjutTidak = False
            else :
                print('Inputan Tidak Valid')
                break
        except TypeError:
            print ('Silahkan ikutan arahan kami dengan menggunakan simbol (y/n), Terimakasih')
            continue
        except ValueError:
            print ('\n Invalid silahkan coba kembali')
            continue

print ('=========================================')
print ('Total Harga Buah Yang di Beli Anda : ' , sum(total))
