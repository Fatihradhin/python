#list itu adalah sebuah... apa ya? semacam data gitu lah yang tersimpan dan memiliki seragam atau beragam tipe data.
#Maksud gue lo bisa ngisi sebuah list dengan angka aja atau campuran dari angka, string, objek, bahkan list didalam list pun bisa.
#Untuk membuat list lo bisa pakai tanda "[" dan "]" dan pakai tanda koma buat misahin setiap elemennya. exp:
nama = ["mulyono", "janggar", "wowok"] #seragam
umur = ["limapulluh tujuh", 43, True] #beragam
alamat = [["oslo"], ["jtg"], ["hambalang"]] #list didalam list
#nah, ada namanyaa tuh tuple. jadi  tuple itu kumpulan data kayak list namun ga bsia di ubah. kalo list masih bisa diubah
buah = ["apel", "anggur", "mangga"] 
buah[1] = "semangka" #kita ganti anggur jadi semangka
print(buah)
#hasil output bakalan keluar [apel, semangka, mangga]. nah kalo tuple itu immutable
senjata = ("AK-47", "M16", "M1187")
senjata[2] = "K-1" #jangan lupa di mode komen dulu yang ni biar ga eror
print(senjata)
#output nya error, karena ya tuple gabisa diubah, biasanya dipake buat data data tetap kaya tempat tanggal lahir, dsb. 
#hbis tuh ada yg namanya dictionary. Ini itu isinya key-value gitu, yaitu sebuah data yang saling berpasangan(nama : adul adudul, umur : 18) ini key(nama,umur) dan value(adul adudul,18)
data = {
    "nama": "piere gasly",
    "team": "bwt alpine",
    "umur": "29 Tahun"
}
print(data)
#tuple dan dictionary juga bisa dibuat jadi satu didalam sebuah list
combo = [["ahmad", 19, True], (1, 2, 3), {"nama": "andy cole"}]
print(combo)
#oke, dah