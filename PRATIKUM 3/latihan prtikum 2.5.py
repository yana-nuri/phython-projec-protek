print('hai ... nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secarak acak antara 0 s/d 100. silahkan tebak ya!!!')
ta=int(input('tebakan anda : '))
while True:
    if(ta < 10):
        print('hehehe....bilangan tebakan anda terlalu kecil')
        ta=int(input('tebakan anda : '))
    elif(ta > 10):
        print('hehehe....bilangan tebakan anda terlalu besar')
        ta=int(input('tebakan anda : '))
    elif(ta == 10):
        print('yeeee....bilangan tebakan anda benar')
        break
