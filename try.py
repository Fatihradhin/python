try:
    angka1 = int(input('masukan angka: '))
    angka2 = int(input('masukan angka: '))
    hasil = angka1 + angka2
    print(f'jawabannya adalah {hasil}')
except ValueError:
    print('kesalahan dalam input.')
if hasil == 7:
    print('Selamat, anda memperoleh angka terpilih!!')
else:
    print()
    
try:
    x = int(input('masukan tebakan anda: '))
except ValueError:
    print('angka saja')
else:
    if x == 7:
        print('selamat, kamu benar')
    else:
        print('yah belum tepat nih')