import csv
import sys
import time
import os

filename = 'member.csv'
if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username','password'])
        

def login ():
    status = True
    while status == True:
        nama = input('masukan username: ')
        password = input('masukan password: ')
        with open('member.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nama and row[1] == password:
                    print()
                    print()
                    teks = 'Loading...'
                    for huruf in teks:
                        sys.stdout.write(huruf)
                        sys.stdout.flush()
                        time.sleep(0.3)
                    print('\nKamu berhasil login!!')
                    return
            else:
                print()
                print('!!!')
                print('kayaknya salah')
                print()

def create ():
    print()
    print('ayo kita bikin akun buat kamu')
    print()
    nama = input('masukan username: ')
    ps = input('masukan password: ')
    with open('member.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, ps])
    print()
    sys.stdout.write('membuat akun') 
    sys.stdout.flush()
    for i in range(3):
        time.sleep(1)
        sys.stdout.write('.')
        sys.stdout.flush( )
    time.sleep(1)
    print('\nPembuatan akun berhasil!!')
     

def system ():
    status = True
    while status == True:
        print('Welcome!!')
        print()
        try:
            a = input('sudah punya akun (sudah/belum): ')
            if a == 'sudah':
                print()
                print('baiklah, kita login dulu')
                login()
                print('Hello world!!')
                status = False
                return
            elif a == 'belum':
                print()
                b = input('mau buat satu? (ya/tidak): ')
                if b == 'ya':
                    create()
                    print()
                    print('kamu akan dialihkan ke halaman utama')
                    time.sleep(2)
                    continue
                elif b == 'tidak':
                    print()
                    print('oke, kamu dikeluarkan')
                    status = False
                    return
                else:
                    print()
                    print('kamu salah memasukan opsi. kamu akan dibawa ke halaman utama')
                    time.sleep(2)
            else:
                print()
                print('kamu salah memasukan opsi. kamu akan dibawa ke halaman utama')
                time.sleep(2)
        except ValueError:
            print('Terjadi kesalahan!!!')
            print()
            
system()