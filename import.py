#import adalah something yang bisa membawakan modul atau transkrip/pustaka eksteral. modul itu adalah file python yang berisi kode
#misalnya gue buat file baru yang isinya sistem pertambahan
import penjumlahan
print(penjumlahan.tambah(2,7))
#nah module di python itu ada 3 jenis yang utama. Pertama built in module. module bawaan waktu install py.
#kedua, eksternal module. module butan orang yang harus lu install dulu.
#terakhir itu adalah modulle yang lo buat senddiri. kayak sebelumnya.

#ini addalah contoh module built in module.
import time #yaa, ngatur waktu gitu lah, macamm delay.
import sys #ini system, yang artinya kita bisa ubah system kerja pythoon yg awalnya by default, jadi by me.
for hitung_mundur in range(10, 0, -1):
    print(hitung_mundur ).da print selanjutnya selama 1 detik
print('DUARRRRR!!!!')   z 

#ada eksternal, nah karenna ini buatan orang jadi kita harus install dulu, biasanya install pake (pip install 'nama module') 
#kamu harus instal di terminal.
import numpy as np
a = np.array([1,2,3,4,5])
print(a * 2 ) 