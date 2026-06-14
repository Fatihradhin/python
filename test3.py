#ps = 1
#while ps == 1:
#    password = input('masukan password: ')
#    if password != 'user123':
 #       print('password salah, coba lagi')
  #  else:
    #    print('password benar')
   #     ps -=1



while True:
    a = input("Masukan disini: ").capitalize()
    if a == 'Quit':
        b = input("apakah anda yakin? (ya/tidak): ").lower()
        if b == 'ya':
            print("Baiklah, semoga harimu menyenangkan:)")
            break
        elif b == 'tidak':
            continue
    match a:
        case "Senin" | "Selasa" | "Rabu" | "Kamis" | "Jumat" | "Sabtu" | "Minggu":
            print(f'{a} adalah nama hari')
        case "Januari" | "Februari" | "Maret" | "April" | "Mei" | "June" | "Juli" | "Agustus" | "September" | "Oktober" | "November" | "Desember":
            print(f"{a} adalah Nama bulan")
        case _: 
            print("Masukan input yang benar")