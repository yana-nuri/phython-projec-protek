import os

try:
    file = input('Masukan Nama Fale : ')
    if os.path.exists(file) :
        mode = 'a'
    else:
        mode = 'r'

    isiFile = open(file, mode)

    lanjut = True
    while(lanjut==True):
        data = input('data apa yang ingin anda tambahkan : ')
        isiFile.write('\n' + data)

        opsi = input('Apakah ada lagi ? (y/n) : ')
        if (opsi == 'y'):
            lanjut = True
        elif (opsi == 'n'):
            lanjut = False
        else :
            print ('Input Tidak valid')
            break
    isiFile.close()

except FileNotFoundError :
    print('Fale Tidak Ditemukan')
    
    
            
