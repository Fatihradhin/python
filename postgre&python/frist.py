#untuk  bisa mengkoneksikan py dengan postgre user harus menginstall psycopg2 terlebih dahulu.
import psycopg2 #import psycopg2 agar bisa memakai fungsi fungsi didalamnya.
koneksi = psycopg2.connect( #karena menggunakan oop, jadi harus dituliskan segala class nya
    host="localhost", 
    port="5432",
    database="nathanradhin",
    user="postgres",
    password="postgresqlsuperadmin"
    )
cursor = koneksi.cursor() #ini adalah cursor ibarat jari dimana kamu menunjuk ke postgre 

cursor.execute("select * from lohloh.mahasiswa") #ini adalah perintah untuk postgre
hasil = cursor.fetchall() #ini untuk ambil hasilnya
print(hasil)
cursor.close() #jangan lupa ditutup
koneksi.close()