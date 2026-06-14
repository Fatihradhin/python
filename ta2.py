def apk ():
    print()
    print('=== Selamat datang di game kecil dan aneh namanya tebak angka ===')
    print()
    print('terdapat tiga level berbeda dengan tingkat kesulitan yang berbeda juga.\ndi level 1 anda dapat mengulang sesi sesuka hati\nnamun di level 2 dan 3, anda hanya bisa main sekali sesi. setiap sesi terdapat 3 kesempatan, gunakan dengan baik.')
    print()
    input('klik enter untuk lanjut...')
    print() 
    show_hall_of_fame()
    print()
    print('nama anda akan ada disana apabila berhasil memenangkan game ini.')
    input('tekan enter...')
    print()
    hasil = level1()
    if hasil == 'keluar':
        print()
        print('semoga harimu menyenangkan!!')
        return
    elif hasil == 'tidak':
        print()
        print('semoga harimu menyenangkan!!')
        return
    
    hasil2 = level2()
    if hasil2 == False:
        print()
        return
    elif hasil2 == 'tidak1':
        print()
        print('sayang sekali, tapi yasudahlah')
        return
    
    hasil3 = level3()
    if hasil3 == False:
        return
    elif hasil3 == 'Champs':
        hall_of_fame()

def level3 ():
    print()
    print('<=SELAMAT DATANG DI LEVEL 3=>')
    print()
    print('Sebelumnya, selamat!! Anda adalah segelintir orang yang mampu sampai di level ini\nHormat kepada anda.')
    print('Disini, anda akan diberi 8x hint dari yang sebelumnya 4x.\nsetiap hint secara tersirat akan memberikan tahu anda, jarak/posisi anda terhadap angka utama. Semoga membantu.')
    print()
    print('dari 1-100, mana yang menjadi angka utamanya')
    attempt = 3
    status = True
    while status == True:
     if attempt == 0:
         print('kesempatan mu habis, kamu dikeluarkan dari aplikasi')
         status = False
         return False
     else:
        try:
             y = int(input('masukan tebakan: '))
             if y == 41:
                 print()
                 print('Benarkah? ada yang b bisa memecahkan level ini..\nKamu.. kamu legenda, nama mu akan abadi di hall of fame')
                 status = False
                 return 'Champs'
             elif 87 <= y <= 100:
                 print('kamu sangat jauh, coba mundur beberapa angka')
                 attempt -=1
             elif 72 <= y <= 86:
                 print('kamu ada di satu lapis setelah lapisan yang menempel dengan jawaban..')
                 attempt -=1
             elif 60 <= y <=71:
                 print('kamu kenal Estevao Willian?')
                 attempt -=1
             elif 40 <= y <=59:
                 print('sejujurnya, dia ada disekitarmu, tapi mungkin kamu butuh petunjuk tam6ahan...')
             elif 20 <= y <=39:
                 print()
                 print('Coba main sedikit tinggi..')
                 attempt -=1
             elif y >100 or y <1:
                 print('hei, jangan bercanda')
             else:
                 print()
                 print('Kamu benar benar berfikir aku menaruhnya diangka kecil? Hahaha')
                 attempt -=1
        except ValueError:
            print()
            print('kau dari kota bodoh mana, hah?')
    
def level2 ():
    print()
    print('<===selamat datang di level 2===>')
    print()
    print('anda akan diberi 4x hint dari yang sebelumnya 2x, semoga membantu.')
    print()
    print('dari 20-50, mana yang menjadi angka utamanya')
    attempt = 3
    status = True
    while status == True:
     if attempt == 0:
         print('kesempatan mu habis, kamu dikeluarkan dari aplikasi')
         status = False
         return False
     else:
        try:
             y = int(input('masukan tebakan: '))
             if y == 34:
                 print()
                 print('kamu berhasil menebak, selamat!!\nmau lanjut ke level selanjutnya atau akhiri sesi?')
                 z = input('ya/tidak: ').lower()
                 if z == 'ya':
                     status = False 
                     return True
                 elif z == 'tidak':
                     status = False
                     return 'tidak1'
                 else:
                     print()
                     print('kamu salah memasukan opsi, kamu akan dibawa ke level 2 lagi ')
             elif y == 33:
                 print()
                 print('Sedikit lagi...')
                 attempt -=1
             elif y == 35:
                 print()
                 print('kamu melewati nya...')
                 attempt -=1
             elif y >50:
                 print()
                 print('kamu melewati batas range yang ditentukan, ini akan tetap dihitung!')
                 attempt -=1
             elif y <20:
                 print()
                 print('kamu tidak mencapai batas range yang ditentukan, ini akan tetap dihitung!')
                 attempt -=1
             elif 29 <= y <=32:
                 print()
                 print('kamu mendekatinya, semangat!!')
             elif 36<= y <=41:
                 print()
                 print('kamu melewatinya terlalu banyak coba mundur beberapa angka, semangat!!')
             else:
                 print()
                 print('salah, coba lagi..')
                 attempt -=1
        except ValueError:
            print()
            print('kau dari kota bodoh mana, hah?')
            
        

def level1 ():
    print()
    print('<===selamat datang di level 1===>')
    print()
    print('dari 1-10, mana yang menjadi angka utamanya')
    print()
    attempt = 3
    status = True
    while status == True:
     if attempt == 0:
         print('kesempatan mu habis, mulai ulang atau keluar')
         x = input('ulang/keluar: ').strip().lower()
         if x == 'ulang':
             attempt +=3
         elif x == 'keluar':
             status = False 
             return 'keluar'
         else:
             print()
             print('kamu salah memasukan opsi!')
     else:
        try:
             y = int(input('masukan tebakan: '))
             if y == 7:
                 print()
                 print('kamu berhasil menebak, selamat!!\nmau lanjut ke level selanjutnya atau akhiri sesi?')
                 z = input('ya/tidak: ').lower()
                 if z == 'ya':
                     status = False 
                     return 'ya'
                 elif z == 'tidak':
                     status = False
                     return 'tidak'
                 else:
                     print()
                     print('kamu salah memasukan opsi, kamu akan dibawa ke level 1 lagi ')
             elif y == 6:
                 print()
                 print('Sedikit lagi...')
                 attempt -=1
             elif y == 8:
                 print()
                 print('kamu melewati nya...')
                 attempt -=1
             elif y >10:
                 print()
                 print('kamu melewati batas range yang ditentukan, ini akan tetap dihitung!')
                 attempt -=1
             elif y <1:
                 print()
                 print('kamu tidak mencapai batas range yang ditentukan, ini akan tetap dihitung!')
                 attempt -=1
             else:
                 print()
                 print('salah, coba lagi..')
                 attempt -=1
        except ValueError:
            print()
            print('kau dari kota bodoh mana, hah?')
            
            
def hall_of_fame ():
    with open('halloffame.txt','a') as file:
        nama = input('Masukan nama anda (nama ini akan ditampilkan di awal program): ')
        file.write(nama + ',' + '\n')
    print()        
    print('<==Nama anda berhasil masuk ke Hall of Fame==>  \nkejeniusan anda akan terabadikan sepanjang masa.')
    print()        
    print()        
    print('Salam hangat dari Rapphilemon')        

def show_hall_of_fame ():
    judul = 'HALL OF FAME'
    print(judul)
    with open('halloffame.txt', 'r') as file:
        for nama in file:
            hall = nama.strip().split(',')
            print(hall)
            
apk()