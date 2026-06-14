#x = input("masukan teks: ")
#y = input("masukan kata: ")
#z = x.split(' ')

#for sortir in z:
#    if sortir == y: 
#       print(f'\"{y}\" ada pada teks \"{x}\"') 
#        break
#else:
#    print(f'\"{y}\" tidak ada pada teks \"{x}\"')
    
print("Alat pendeteksi ganjil-genap")
while True:
    a = input('Masukan angka: ')
    if a.isdigit():
        a = int(a)
        if a % 2 ==0:
            print(f'{a} adalah angka genap')
        else:
            print(f'{a} adalah angka ganjil')
    elif a == 'quit':
        print("Terimakasih, sampai jumpa!!")
        break
    else:
        print("Harap masukan input yang benar")
        