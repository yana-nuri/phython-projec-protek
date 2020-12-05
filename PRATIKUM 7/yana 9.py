print ("=========================YANA NURIKA============================")
print ("===========================K3520079=============================")
buah = {'apel'  : 5000,
        'jeruk' : 8500,
        'mangga': 7800,
        'duku'  : 6500}

def jumlahBuah():
    jumlah = int(input("berapa Kg : "))
    
    print("-------------------------------------------")
    print("Total Harga : ", buah.get(namaBuah,0)*jumlah)


namaBuah = input('Nama Buah Yang Dibeli : ')

try:

    if(namaBuah in buah.keys()):
        jumlahBuah()

    else:
        print('Maaf, Buah yang anda cari kebetulan lagi kosong')

except ValueError:
    print('Silahkan isikan dengan huruf angka buat jumlah buah yang diinginkan')
    jumlahBuah()
