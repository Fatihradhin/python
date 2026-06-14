#oke,  jadi skrg kitta bahas etoode pengolahan list, jadi kkita isa memanipulasi isi list
#pertama ada .reverse() ini buat ngebalik isi darii lsit

angka = [4, 2, 1, 5, 3, 6, 7, 1, 4]
angka.reverse() #untuk penulisannya, gak didalam kurung karena itu namanya method gblk, ststmn kaya print() itu built in fctn.
print(angka)

#kedua ada .sort sama penulisan nya kaayak reverse, cuma fungsinyabeda. sort buat nyortir daata lo dari yang awalnya berantakam jadi teruurt
angka.sort()
print(angka)
#nh ada caranya gimana biar bisa sort dari besrs k kecil, ya tonggal di reverse blokgh
angka.sort(reverse = True)

#terus ada count() dia menghitung berapaa kali data itu munucl di list
print(angka.count(4)) 

#lalu adda index, ya gaperlu gue jelasin lah inndex itu apa, dasar bgt soalnya.
print(angka.index(3))

#append ini adalah method uangg digunakan buat menambahkan data di akhir list(biasanya)
angka.append("Rusdi")
print(angka)

#lalu ada saudaranya pop, kebalikannya, dia ngehapus data di list
angka.pop() #kalo tanpa indexing, dia otomatis hapus yg terakhjir
print(angka)
#bisa juga lo masukin kategorinya 
angka.pop(4)
print(angka)
#nah pop ini selain bisa ngehapus, dia juga bisa ngambil data


#insert, simple nya, lo masukin angka kedalam index yang udh ada yang puna, jadi pemilik sebeumnya disruh geser
angka.insert(4, 4) #urutannya (posisi index, angka/nilai)
print(angka)

#remove, yaitu ngebuang data lo. lah, bedanya apa saama pop? mah kalo pop itu lo hapus data sesuai index, kkalo remove ya nilainya lo  hapus
angka.remove(7)
print(angka) 

#sedikit tambahan, ada metode yang ditulis diluar print dan didalam print. 
#bedanya itu method nag diluar print, adalah method yang berhubungan langsung dengan dta, yang artinya merubah data lalu menampilkan nya, sementara yang didalam print, dia cuma ngambil nilai dari data, lalu dikembalikan lagi. (kalo lu belajar excel, lo bisa samain kayak rumus count sum dan if bertingkat)

#ada len() buat ngitunng panjang list
y = len(angka)
print(y)

#ada del yang mana menghapus data sesuai index nya
#oke, dah
print(angka.count())