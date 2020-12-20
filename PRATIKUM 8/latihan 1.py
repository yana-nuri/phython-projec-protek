print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

def ubuhHurufReplace(teks, a, b,):
    teksReplaced = teks.replace(a,b)
    return teksReplaced

def ubahHurufSecaraManual (teks, a, b):
    listTeks = list(teks)
    for i in range(len(listTeks)):
        if(listTeks[i] == a):
            listTeks[i] = b
    teksReplaced= ''.join(listTeks)
    return teksReplaced

teks = input("Masukan kata yang tuan inginkan / Kalimat yang ingin tuan ubah : ")
a = input("Masukan huruf yang tuan inginkan / Kata apa yang ingin tuan ubah ? ")
b = input("Ubah {0} menjadi : ".format(a))

result = ubuhHurufReplace(teks, a, b)
print(result)

hasil = ubahHurufSecaraManual(teks, a, b)
print(hasil)
