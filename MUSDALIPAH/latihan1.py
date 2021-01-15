from datetime import *

def diffDate (x) :
    membagi = x.split('-')
    listHari = []

    for y in membagi :
        listHari.append(int(y))

    hari = date(listHari[0], listHari[1], listHari[2])
    hariIni = datetime.date(datetime.now())
    selisihHari = hari - hariIni
    hasilSelisih = abs(selisihHari.days)
    return hasilSelisih

'''
print(diffDate('2021-01-20'))
print(diffDate('2020-12-20'))
print(diffDate('2022-09-10'))
'''

'''
try :
    hariSekarang = input('Ketikkan tanggal yang sesuai dengan kenginan anda, dengan Format (yyyy-mm-dd) : ')
    diff = diffDate(hariSekarang)
    print ('Selisih dengan tanggal yang di input adalah : ', diff, 'hari')
except ValueError :
    print('Jangan ada spasi/tidak valid')
'''
