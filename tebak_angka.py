def jb ():
    print()
    print('SELAMATT KAMU BENAR!!!! MAMAH KAMU PASTI BANGGA')
    print()
    x = input('mau lanjut ke level selanjutnya atau udahan?: ')
    match x:
        case 'lanjut' | 'gas lanjut' | 'gass lanjut' | 'lanjut aja' | 'lanjut lah':
            level2()
        case 'udahan' | 'stop' | 'berhenti' | 'selesaikan sesi':
            print()
 

def jb2 ():
    print()
    print('Jawaban benar! well done, mate!')
    print()
    
def level2 ():
    print()
    print('<==Selamat Datang Di Level 2==>')
    print()
    print('disini saya akan memberi hint sebanyak 4x.\nsemoga membantu. ')
    print()
    print('dari 20 sampai 50, tebak angka utamanya')
    attempts = 3
    while attempts !=0:
        print()
        try:
            a = int(input('masukan tebakan: '))
            if a == 34:
                jb2()
                attempts -=3
        except ValueError:
            print('kesalahan input')
            print()    

def m ():
    print()
    print('waduhhh, mendekati nih.. coba tebak ulang')
def l ():
    print()
    print('aiisshhh, kelewat broo.. coba tebak lagi')

def app():
    print()
    print('=== Selamat datang di game kecil dan aneh namanya tebak angka ===')
    print()
    print('terdapat tiga level berbeda dengan tingkat kesulitan yang berbeda juga.\ndi level 1 anda dapat mengulang sesi sesuka hati\nnamun di level 2 dan 3, anda hanya bisa main sekali sesi. setiap sesi terdapat 3 kesempatan, gunakan dengan baik atau...You\'re done.')
    print()
    print('harap dibaca baik baik, karena saya tidak ingin menjelaskannya lagi nanti.')
    print()
    input('klik enter jika anda ingin memulai...')
    print()
    level1()
    
    
def level1 ():
    print('<===Selamat datang di level 1===>')
    print()
    print('coba anda tebak, dari rentang 1-10 angka berapa yang menjadi nilai utama nya?')
    attemps = 3
    while attemps != 0 or attemps ==0:
        print()
        if attemps == 0:
            print()
            print('yah sayang banget kamu belum benar tebakannnya. coba lain waktu yaa!!')
            print()
            x = input('mau ulang lagi atau keluar?: ').lower()
            match x:
                case 'ulang lagi' | 'ya, ulang lagi' | 'ulang lagi deh' | 'ulang':
                    print('OKEEE, SEMANGATTT!!')
                    attemps +=3
                    continue
                case 'keluar' | 'keluar aja deh' | 'udahan' | 'aku mau keluar':
                    break
        else:
            try:
                jawaban = int(input('masukan tebakan: '))
                if jawaban == 7:
                    jb()
                    break
                elif jawaban == 6:
                    m()
                    attemps -=1
                    print(f'sisa kesempatan: {attemps}')
                elif jawaban == 8:
                    l()
                    attemps -=1
                    print(f'sisa kesempatan: {attemps}')
                elif jawaban >10:
                    print()
                    print('kamu melewati batas yang ditentukan!')
                elif jawaban <1:
                    print()
                    print('kamu melewati batas yang ditentukan!')
                else:
                    print()
                    print('waduhhh, masih jauh massehh.')
                    attemps -=1
                    print(f'sisa kesempatan: {attemps}')
            except ValueError:
                print('harap masukan input yang benar!')
    print()
    print('baiklah, have a nice day :)')
app()