file = open('daftar.txt', 'r')
while True:
    try:
        nama = input('masukan nama: ' ).capitalize()
        if nama == '':
            print()
            print('terjadi kesalahan!!')
            continue
        umur = input('masukan umur: ')
        if umur == '':
            print()
            print('terjadi kesalahan!!')
            continue
        status = input('masukan status (pekerja, pelajar, dll.): ').capitalize()
        if status == '':
            print()
            print('terjadi kesalahan!!')
            continue
        break
    except ValueError:
        print('masukan nilai yang benar!')
        
l = file.read()
print(l)
file.close()