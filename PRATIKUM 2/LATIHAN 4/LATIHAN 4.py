# Variable assignment
jarakPertama = 125
kecepatanPertama = 62
jarakKedua = 256
kecepatanKedua = 70
waktuBerangkat = 06.00
waktuIstirahat = 0.45
# Operasi penghitungan
pukulSampai = waktuBerangkat+waktuIstirahat+jarakPertama//kecepatanPertama+jarakKedua//kecepatanPertama
# Tampilkan hasil
print('Pukul sampai pak amir di kota tujuan : ' + str(pukulSampai))
