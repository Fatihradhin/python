while True:
    try:
        a = int(input('masukan umur: '))
        b = input('masukan nama: ')
        break
    except ValueError:
        print()
        print('terjadi kesalahan!!!\nharap input ulang!!')
        print()