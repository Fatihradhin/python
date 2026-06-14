#bikin kalkulator biar inget lagi sama py, wkwkw.

def tambah():
    a = 0
    while a == 0:
        try:
            inp1 = int(input('Masukan angka: '))
            inp2 = int(input('Masukan angka: '))
            print()
            print(inp1 + inp2)
            print()
            hasil = input('lanjut? (ya/tidak): ').lower()
            if hasil == 'ya':
                print('ok')
            else:
                print('ok')
                a +=1
        except ValueError:
            print('Maaf, saya tidak paham. coba masukan angka saja')
def kurang():
    a = 0
    while a == 0:
        try:
            inp1 = int(input('Masukan angka: '))
            inp2 = int(input('Masukan angka: '))
            print()
            print(inp1 - inp2)
            print()
            hasil = input('lanjut? (ya/tidak): ').lower()
            if hasil == 'ya':
                print('ok')
            else:
                print('ok')
                a +=1
        except ValueError:
            print('Maaf, saya tidak paham. coba masukan angka saja')
def kali():
    a = 0
    while a == 0:
        try:
            inp1 = int(input('Masukan angka: '))
            inp2 = int(input('Masukan angka: '))
            print()
            print(inp1 * inp2)
            print()
            hasil = input('lanjut? (ya/tidak): ').lower()
            if hasil == 'ya':
                print('ok')
            else:
                print('ok')
                a +=1
        except ValueError:
            print('Maaf, saya tidak paham. coba masukan angka saja')
def bagi():
    a = 0
    while a == 0:
        try:
            inp1 = int(input('Masukan angka: '))
            inp2 = int(input('Masukan angka: '))
            print()
            print(inp1 / inp2)
            print()
            hasil = input('lanjut? (ya/tidak): ').lower()
            if hasil == 'ya':
                print('ok')
            else:
                print('ok')
                a +=1
        except ValueError:
            print('Maaf, saya tidak paham. coba masukan angka saja')
        
def homepage():
    print('kalkulator, apa yang ingin anda hitung?')
    