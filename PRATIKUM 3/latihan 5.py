kodekaryawan = int(input('masukan kode karyawan :'))
namakaryawan = input('masukan nama karyawan :')
golongan = input('masukan golongan :')
status = input('masukan status (1: menikah, 2: belum) : ')
if(status == '1') :
    jumlahanak = int(input('masukan Jumlah Anak : '))
    tunjanganmenikah = 10 / 100
    tunjangananak = 5 / 100 * jumlahanak
    statusmenikah = 'sudah menikah'
else:
    jumlahanak = 0
    tunjanganmenikah = 0
    tunjangananak = 0
    statusmenikah = 'belum menikah'



if(golongan == 'A'):
    gajipokok = 10000000
    potongan = 2.5
    jumlahtunjanganmenikah = 10000000 * tunjanganmenikah
    jumlahtunjangananak = 10000000 * tunjangananak
    gajikotor =10000000 + jumlahtunjanganmenikah + jumlahtunjangananak
    jumlahpotongan = 2.5 / 100 * gajikotor
    gajibersih = gajikotor - jumlahpotongan
elif(golongan == 'B'):
    gajipokok = 8500000
    potongan = 2.0
    jumlahtunjanganmenikah = 8500000 * tunjanganmenikah
    jumlahtunjangananak = 8500000 * tunjangananak
    gajikotor = 8500000 + jumlahtunjanganmenikah + jumlahtunjangananak
    jumlahpotongan = 2.0 / 100 * gajikotor
    gajibersih = gajikotor - jumlahpotongan
elif(golongan == 'C'):
    gajipokok = 7000000
    potongan = 1.5
    jumlahtunjanganmenikah = 7000000 * tunjanganmenikah
    jumlahtunjangananak = 7000000 * tunjangananak
    gajikotor = 7000000 + jumlahtunjanganmenikah + jumlahtunjangananak
    jumlahpotongan = 1.5 / 100 * gajikotor
    gajibersih = gajikotor - jumlahpotongan
elif(golongan == 'D'):
    gajipokok = 5500000
    potongan = 1.0
    jumlahtunjanganmenikah = 5500000 * tunjanganmenikah
    jumlahtunjangananak = 5500000 * tunjangananak
    gajikotor = 5500000 + jumlahtunjanganmenikah + jumlahtunjangananak
    jumlahpotongan = 1.0 / 100 * gajikotor
    gajibersih = gajikotor - jumlahpotongan

    print('==========')

print('struk rincian gaji karyawan')

print('----------')

print('nama karyawan :' + namakaryawan + '(kode kayawan :' + str(kodekaryawan) +')')
print('golongan :' + golongan)
print('status nikah :' + statusmenikah)
print('jumlah anak :' + str(jumlahanak))

print('----------')
    
print('gaji pokok : Rp' + str(gajipokok))
print('tunjangan menikah : Rp' + str(jumlahtunjanganmenikah))
print('tunjangan anak : Rp' + str(jumlahtunjangananak))

print('----------')

print('gaji kotor : Rp' + str(gajikotor))
print('potongan (' + str(potongan) + '%): Rp' + str(jumlahpotongan))

print('----------')

print('gaji bersih : Rp' + str(gajibersih))
