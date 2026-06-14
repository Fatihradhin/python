#global var adalah variable yang bisa dipakai didalam def
#variablle ii sebelum diambil harus diawali dengan global nama_var

k =  input('masukan nama: ')
j = input('kamu biasa dipanggil apa?: ')
def kenalan():
    global k #k itu var luar yang bisa dipakai didalam asal ada global sebelumnya, kalo dari dalam keluar gabisa api kalo  dari luuar kedalam bisa.
    print()
    print(f'salam kenal, {k}!!')

kenalan()

#versi lbih banyak awkoakwokwoawk

condition = 0
def hai():
    global condition
    global j
    global k
    while condition == 0:
        a = input(f'gimana kabar kamu, {j}?: ').lower()
        match a:
            case 'baik' | 'baik baik aja' | 'alhamdulilah baik' | 'lumayan' | 'lumayan lah' | 'sehat, alhamdulillah' | 'aku baik baik aja':
                print()
                print('wah senang mendengarnya, pertahankan terus ya!!')
                condition +=1
            case 'kurang baik'| 'kacau' | 'lagi down' | 'down' | 'capek' | 'kurang sehat' | 'lumayan berat':
                print()
                print(f'waduh wkwkw, semangat yah {k}!! namanya juga idup.')
                condition +=1
            case _:
                print()
                print('maaf nih pak/bu/mba/mas, jawabannya yang lain ada gak, saya ngetik opsi\nnya satu satu soalnya HAHAHAHHA')
                print()

hai()