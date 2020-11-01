kodekaryawan = input('masukan kode karyawan :')
namakaryawan = input('masukan nama karyawan :')
golongan = input('masukan golongan :')

print('==========')

print('struk rincian gaji karyawan')

print('-----------------------------------------------------------')

print('nama karyawan :' + namakaryawan + '(kode kayawan :' + kodekaryawan + ')')
print('golongan :' + golongan)

print('-----------------------------------------------------------')

if(golongan == 'A'):
    gajipokok = 10000000
    potongan = 2.5
    jumlahpotongan = 2.5 / 100 * 10000000
    gajibersih = 10000000 - jumlahpotongan
elif(golongan == 'B'):
    gajipokok = 8500000
    potongan = 2.0
    jumlahpotongan = 2.0 / 100 * 8500000
    gajibersih = 8500000 - jumlahpotongan
elif(golongan == 'C'):
    gajipokok = 7000000
    potongan = 1.5
    jumlahpotongan = 1.5 / 100 * 7000000
    gajibersih = 7000000 - jumlahpotongan
elif(golongan == 'D'):
    gajipokok = 5500000
    potongan = 1.0
    jumlahpotongan = 1.0 / 100 * 5500000
    gajibersih = 5500000 - jumlahpotongan
print('gajipokok : Rp' + str(gajipokok))
print('potongan (' + str(potongan) + '%): Rp' + str(jumlahpotongan))

print('-----------------------------------------------------------')

print('gajibersih : Rp' + str(gajibersih))
