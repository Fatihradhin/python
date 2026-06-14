def tambah():
    print('<===============================================>')
    at = 0
    while at == 0:
        try:
            print()
            print('     Masukan angka yang mau dijumlahkan.')
            print()
            angka1 = int(input("masukan angka pertama         : "))
            angka2 = int(input("masukan angka kedua           : "))
            print()
            hasil = angka1 + angka2
            print("hasilnya adalah               : ", hasil)
            print()
            print("<====== Proses penjumlahan telah selesai:) ======>")
            print()
            k = input('lanjutkan operasi atau pindah (yes/no) : ').lower()
            if k == 'yes':
                print()
            elif k == 'no':
                at +=1    
        except ValueError:
            print("=======================================")
            print("      masukan angka yang benar lah bodo")

def kurang():
    print('<===============================================>')
    at = 0
    while at == 0:
        try:
            print()
            print('     Masukan angka yang mau dikurangkan.')
            print()
            angka1 = int(input("masukan angka pertama         : "))
            angka2 = int(input("masukan angka kedua           : "))
            print()
            hasil = angka1 - angka2
            print("hasilnya adalah               : ", hasil)
            print()
            print("<====== Proses pengurangan telah selesai:) ======>")
            print()
            k = input('lanjutkan operasi atau pindah (yes/no) : ').lower()
            if k == 'yes':
                print()
            elif k == 'no':
                at +=1    
        except ValueError:
            print("=======================================")
            print("      masukan angka yang benar lah bodo")

def kali():
    print('<===============================================>')
    at = 0
    while at == 0:
        try:
            print()
            print('     Masukan angka yang mau dikalikan.')
            print()
            angka1 = int(input("masukan angka pertama         : "))
            angka2 = int(input("masukan angka kedua           : "))
            print()
            hasil = angka1 * angka2
            print("hasilnya adalah               : ", hasil)
            print()
            print("<====== Proses perkalian telah selesai:) ======>")
            print()
            k = input('lanjutkan operasi atau pindah (yes/no) : ').lower()
            if k == 'yes':
                print()
            elif k == 'no':
                at +=1    
        except ValueError:
            print("=======================================")
            print("      masukan angka yang benar lah bodo")

def bagi():
    print('<===============================================>')
    at = 0
    while at == 0:
        try:
            print()
            print('     Masukan angka yang mau dibagikan.')
            print()
            angka1 = int(input("masukan angka pertama         : "))
            angka2 = int(input("masukan angka kedua           : "))
            print()
            hasil = angka1 / angka2
            print("hasilnya adalah               : ", hasil)
            print()
            print("<====== Proses pembagian telah selesai:) ======>")
            print()
            k = input('lanjutkan operasi atau pindah (yes/no) : ').lower()
            if k == 'yes':
                print()
            elif k == 'no':
                at +=1    
        except ValueError:
            print("=======================================")
            print("      masukan angka yang benar lah bodo")
        except ZeroDivisionError:
            print("=======================================")
            print("      in real life, itu ga terhingga, but in computer, that's error.")

def app():
    stop = 0
    while stop == 0:
        print()
        print('         <==Ceritanya bikin kalkulator==>\nmasukan angka sesuai kategori untuk memulai sesi:)')
        print()
        print('ketik (1) untuk penjumlahan')
        print()
        print('ketik (2) untuk pengurangan')
        print()
        print('ketik (3) untuk perkalian')
        print()
        print('ketik (4) pembagian')
        print()
        print('ketik (5) untuk akhiri sesi')
        print()
        try:
            decision = int(input("opsi berapa?: "))
            if decision == 1:
                tambah()
            elif decision == 2:
                kurang()
            elif decision == 3:
                kali()
            elif decision == 4:
                bagi()
            elif decision == 5:
                k = input('kamu beneran mau pergi?? (ya/tidak): ').lower()
                if k == 'ya':
                    print()
                    print('okedeh, semoga harimu menyenangkan!!!')
                    print()
                    return
                elif k == 'tidak':
                    print()
                    print('yeeey!! kamu ga jadi pergi :)')
                    print()
                else:
                    print('bung, kau dari kota bodoh mana? bukannya sudah ku beri opsi?\n<!kamu dikeluarkan oleh admin!>')
                    stop =+1
            else:
                print('maaf, masukan angka yang tertea saja ya :)')
        except ValueError:
            print('waduh, sepertinya anda tidak bisa baca, saya sarankan anda\nuntuk akhiri sesi saja :)')
            
            
if __name__ == '__main__':
    app() 