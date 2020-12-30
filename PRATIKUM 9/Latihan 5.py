print("-------------------YANA NURIKA-----------------")
print("---------------------K3520079------------------")

start = open('BilanganPenjumlahan.txt', 'r')
finish = open('HasilPenjumlahan.txt', 'a')
file = start.readlines()

for i in range(len(file)) :
    bil = file[i]
    bil1, bil2 = bil.split('|')
    bil3 = int(bil1) + int(bil2)
    bil4 = str(bil3)
    finish.write(bil4)
    finish.write('\n')

finish.close()
hasil = open('HasilPenjumlahan.txt', 'r')

print(hasil.read())
hasil.close
