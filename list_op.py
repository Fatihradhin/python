#nah, kalo sebelumnya belajar tentang apa itu list, kita sekarang bljar bagaiana list beroperasi.
#so, list itu bisa kamu tambah degan list lainnya.

a = [1, 2, 3, 4, 5]
b = a + a #artinya nilai b itu adaalah isi a dtiambah a itu sendiri(dgn kata lain dikali 2)
print(b) #hasilnya akan ada satu list dengan nilai list a 2x lipat.

#lalu bbisa juga dikalikan

c = [1, 2, 3, 4, 5, 6]
d = c * 10
print(d)
#hasilnya? yaps, bakalan ada satu list dengan nilai 10x lipat variabel c

#then, ada yang namanya map() itu fungsi buat mengubah setiap elemen di dalam list dengan aturan tertentu.
#Bayangin lo punya daftar angka, dan pengen semua angka itu dikali dua — nah, map() bisa ngelakuin itu tanpa harus pakai for loop panjang

angka = [1, 2, 3, 4, 5]
hasil = list( #list disini maksudnya hasilnya nanti bakalan ditampilkan dalam bentuk list.
    map( #nah, map nya bakalan nerapin rumus yang ada di depannya ke semua elemen (maksunya ke semua elemen isi di list, mau itu angka, string, float dll.)
        lambda x: x * 2, angka #nah lambda x ini adalah rumusnya yang akan dijalankan oleh map, nah x nya disini itu cuma variable sementara. x * 2 maksudnya kali 2 ke semua elemen list, makanya list nya ditulis stlhnya
    )
)
print(hasil)

#ada juga filter() nah filter ini intinya itu ngubah isi list terntu, jadi kalau map() itu semuanay, filter() ini cuma yang dikategorikan.
hasil2 = list(
    filter( 
        lambda x: x % 2 == 0, angka #nah kalo lo liat, disini tuh ada == (sama dengan) sbg syarat.
    )
)
print(hasil2)

#bisa juga digabung dengan built infuction kayak sum, max minn

nomer = [1, 2, 3, 4, 5, 6]
print(sum(nomer)) #diia aan  menghitunng selurh  jumah di dalam lisst, bukan per karakter tapiper nilai
print(max(nomer))
print(min(nomer))

#oke, dah