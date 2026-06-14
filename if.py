#Statement if memerlukan sebuah kondisi yang dibangun dengan menggunakan operator logika dan operator relasional. Sedangkan else akan menerima kondisi yang tidak sesuai dengan kondisi di dalam if atau sebelumnya.
nilai = 45
if nilai >85: #harus ada aturan yang mau di-if kan dan setelhnnya diberi (:) agar statment turun ke if, ya  pokoknya gitu lah
    print("gacor")
else: #else disini kondisi selain si if, jadi yang "kena" if itu cuma 85> sisanya masuk ke else.
    print ("good")
    
    
#terus juga ada elif (bukn alif). elif adalah singkatan dari else-if yang ana dipakai buat menambahkan aturan.

umur = 15
if umur <13:
    print("bocah")
elif umur >13 and umur <18: #nah elif disini inbaratya buat nambahin aturn if baru. 
    print("Jembutan")
else:
    print("dewasa")
    
    
#nah, ada lagi nested if, yaitu if di dalam if. Bila kondisi pertama terpenuhi, maka kondisi di dalamnya akan diperiksa dan bila kondisi di dalam kondisi pertama terpenuhi, maka kode akan dieksekusi. 
#ginian sebenrnya rawan eror jadi be careful 
nilai = 90
if nilai > 80:
	print ("Selamat, kamu dapat nilai A")
	if nilai > 95:
		print ("Selamat kamu dapat bonus voucher pendidikan karena nilai kamu A")
	elif nilai == 100:
		print ("Selamat kamu dapat buku pelajaran gratis selama satu semester karena nilai kamu A sempurna.")
elif nilai > 70 and nilai <=80:
	print ("Selamat, kamu dapat nilai B")
elif nilai > 60 and nilai <=70:
	print ("Selamat, kamu dapat nilai C")
elif nilai > 45 and nilai <=60:
	print ("Selamat, kamu dapat nilai D")
else:
	print ("Maaf, kamu dapat nilai E. Kamu harus ikut ujian remedial :(")
 
 #yah  intinnya kalo ga terlalu butuh bngt, mending pake elif
 #oke, dah