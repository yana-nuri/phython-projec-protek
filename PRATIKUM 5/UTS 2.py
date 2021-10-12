v = float(input('Masukan Kecepatan Mobil mula-mula dalam m/s : '))
a = float(input('Masukan Percepatan Mobil dalam m/s : '))
t = 10

print("Jarak yang sudah ditempuh mobil untuk setiap detiknya (mulai dari t = 1 sampai t = 10) ")

def jarak(v,a,t):
    global st
    i = 0
    while (i<t):
        i += 1
        st = (v*t) * (0.5*a*i*i)
        print('t = ', i , ' , ' , 'S(t) = ',st)

jarak(v,a,t)


      
