try :
    file = input('Masukan Nama File : ')
    print('isi file', file, 'adalah : ')
    print(open (file, 'r').read())
except FileNotFoundError:
    print("Fale tidak ditemukan silahkan coba lagi ")
except UnicodeDecodeError:
    print('oops, File yang anda tuju tidak bisa dibuka, karena tidak menggunakan berformat ".txt"')
    
