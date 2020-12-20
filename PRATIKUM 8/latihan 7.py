print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

msh = ['K001:ROHISAN ARI :1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listAnyar = []

for i in range(len(msh)):
    a = msh[i].split(':')
    listAnyar.append(a)

    b = listAnyar[i][2].split('-')
    b.reverse()

    bJoined = '/'.join(b)
    listAnyar[i][2] = bJoined

print('=' * 65)
print('NIM'.ljust(10), 'NAMA MAHASISWA'.ljust(20), 'TGL LAHIR'.ljust(20), 'TEMPAT LAHIR'.ljust(10))
print('-' * 65)

for i in range(len(listAnyar)):
    print(listAnyar[i][0].ljust(10), listAnyar[i][1].ljust(20), listAnyar[i][2].ljust(20), listAnyar[i][3].ljust(10),)
    
