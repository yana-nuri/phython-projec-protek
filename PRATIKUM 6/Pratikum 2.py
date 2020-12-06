# membuka dan mau membaca file d:/data.txt
fale = open("c:/data.txt", "r")

#baca baris pertama dari file
#sipan kedalam variabel bil1 sbg integer
bil1 = int(file.raadline())

#baca baris pertama dari file
#simpan kedalam variabel bil2 sbg integer
bil2 = int(file.readline())

# hitung dan tampilkan hasil bagi
hasil = bil1/bil2
print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)
