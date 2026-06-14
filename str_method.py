#str method adalah metode yang menempel di datta type string tsb.
nama = "Quaresma"
#1, upper. dia berfungsi buat "Nge-Capslock" isi string
nama_besar = nama.upper()
print(nama_besar) #QUARESMA
#2, ada lower. that's the opposite of upper
nama_kecil = nama.lower()
print(nama_kecil) #quaresma
#3, capitalize. dari namanya aja kita bisa taau. dia fungsinya untuk mengubah huruf pertama string menjadi "capitalize"
nama_kapital = nama.capitalize()
print(nama) #Quaresma
#4, title. kalo capitalize cuma meng-capitalize kan awal string, title ini akan meng-capitalize kan setiap kata didalam string.
nama_asli = "ricardo quaresma"
nama_title = nama_asli.title()
print(nama_title) #Ricardo Quaresma.
#strip, for remove the excces spaces.
exp = "  Ricardo Quaresma  "
exp_fix = exp.strip()
print(exp_fix)
#lalu  ada replace(dari, menjadi) nah itu tuh bbuatt ngeganti dari x menjadi y
exp2 = f"Ricardo Quaresma bermain untuk Brazil" #dia sepupu an sama zico(walaupun jauh)
exp2_fix = exp2.replace("Brazil", "Portugal")
print(exp2_fix) #da mengganti Brazil jadi Portugal
#ada count, menghitung jumlah karrakter yang ada di str itu
ez = "lalala  lilili  "
ez_count = ez.count("a")
print(ez_count)
a5s = "kobe bryan"
a4s = a5s.find("bryan")
print(a4s) #nampilin hasilnya index

#lalu  ada yag namanya itu "escape karakter". nah dia ini berfungsi buat memanipulasi  hasil output lah, bisa dibilag gt.
#1, ada (\n) atau enter. nah dia ini tuh berfungsi  buat lu  menambahkan newline/enter tanpa perlu meng-enter statment tsb
kalimat = "baris pertama\nbaris kedua"
print(kalimat)
#tanpa perlu mengenter statment nya kita bisa mendapatkan output yg diinginkan.
#2, (\t) atau tab. tab inni ya as you guys know memberikan spasi dengan jarak yang berbeda dgn spasi biasanya.
kalimat2 = "nama:\tfatih\numur:\t18"
print(kalimat2)
#di output nya bakalan ada spasi sejajar  yang diberikan Tab.
#3, \\ ini yang buat path/lokasi  itu loh, kalo  cuma satu backslallsh bakalan error jadi pakai dua. kalo ada 2? ya pake 4
kalimat3 = "c:\\users\\Fatih R"
print(kalimat3)
#trus  ada \"\" nah ini tuh buat string kayak sometimes lu perlu ngasihh  kode petik bbuuat suatu kalimat  yang memiliki makna lain atau ssuatu dialog.
kalimat4 = "dia berjalan ke arahku \"Hai, lama tak terlihat...\" ujarnya sambil memegang sebungkus martabak manis khas bangka"
#atau
kalimat5 = "Kementrian yang dibuat oleh Prabowo itu \"membengkak\" karena banyak nya mentri"
print(kalimat4)
print(kalimat5)

#lalu  ada uga f-string, ini op karena lo bisa nyelesain expresi  tanpa perlu line tmbahan. caranya tinggal tambahin f diawal string
satu = "uno"
dua = "dos"
kalimat6 = f"Bahasa Spanyol nya satu itu {satu}, dan bahasa Spanyol nya dua adalah {dua}"
print(kalimat6)
#atau
x = 17
y = 23
kalimat7 = f"hasil perkalian dari x dengan y adalah: {x * y}"
print(kalimat7)
