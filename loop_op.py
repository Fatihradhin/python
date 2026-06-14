#loop itu pengulangan. alih alih nulis print() satu satu, mending pake loop
#loop ada 2, for dan while

#for loop itu adalah looping dengan build in range(). aoantuh wwkw, range punya 3 parameter nilai awal, akhir, dan penambah nilai.
for i in range(1, 7, 2):
    print(i)
#i nya  itu iteratur ya satt, jadi ga ngaruh. Mau lu ubah jadi malaysia juga bisa (malaysia si tukang timpa xixi)
for malaysia in range(1, 7, 2):
    print(malaysia)
#selain itu, lo juga bisa pakai pengurangan kalau lu mau looping menurun
for i in range(5, 1, -1): #jangan tolol, harus ngurut 5-1 jangan 1-5 lu nurun 1. bakalan crash ntar vscode nya bblokk.
    print(i)
    
#lalu ada while loop, yaitu looping yang sama kaya for, bedanya for dipakai kalau jumlah perulangannya udah jelas,
#sedangkan while dipakai kalau belum tahu kapan harus berhenti, tergantung kondisi.
i = 0
while i > 10: #while <variable> <parameter> <pembanding>
    print(i)
    i += 1 #variable nya ditulis dulu, baru asigment nya.
#loop juga bisa dipakai di list, tuple, and dictonary. but, it would be good if wefirst learn what a list, tuple, and dictionary are.


#loop  juga bisa dipakaikan else, kerja  nya jika looping sudah mencapai fase false, maka else akan bekerja.
