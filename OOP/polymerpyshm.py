from abc import ABC, abstractmethod
#polymerpyshm adalah sebuah metode dimana... Ya gitu deh wkwk.
#sesuatu yang berjalan seprti bebek, bersuara seperti bebek, itu adalah bebek
class Remote:
    def __init__(self,merk):
        self.merk = merk
    def tombol_l_r(self):
        return 'Ganti'
    def tombol_u_d(self):
        return 'naik dan turun'
    
class Tv(Remote):
    def __init__(self, merk):
        super().__init__(merk)
        
    def tombol_l_r(self):
        return 'Ganti Channel'
    def tombol_u_d(self):
        return 'up n down volume'

class Youtube(Remote):
    def __init__(self, merk):
        super().__init__(merk)
        
    def tombol_l_r(self):
        return 'geser tab kiri kanan'
    def tombol_u_d(self):
        return 'geser tab atas bawah'
    
#nah polimer nya

tombol = [
    Tv('Toshiba'),
    Youtube('SUnshei')
]

for p in tombol:
    print(p.tombol_u_d())
    
#hasilnya 1 input yang sama, 2 output yang berbeda. Voilaa!!

#aa juga polymerpism yang tanpa terhubunng.

class Motor:
    def on(self):
        return 'menyalakan motor'
class Mobil:
    def on(self):
        return 'menyalakan mobil'
class Perahu:
    def on(self):
        return 'menyalakan perahu'
    
def nyala(kendaraan):
    print(kendaraan.on())
    
    
lst = [Motor(),
       Mobil(),
       Perahu()
       ]

for kendaraan in lst:
    nyala(kendaraan)


#masing masing berhasil dieksekusi.

#terus denngan abc method
class Hewan:
    @abstractmethod
    def suara(self):
        pass
    
class Mamalia(Hewan):
    def __init__(self,nama,bunyi):
        self.nama = nama
        self.bunyi = bunyi
    
    def suara(self):
        return f'suara {self.nama} itu bunyi nya {self.bunyi}'
    
class Ovipar(Hewan):
    def __init__(self,nama,bunyi):
        self.nama = nama
        self.bunyi = bunyi
    
    def suara(self):
        return f'suara {self.nama} itu bunyi nya {self.bunyi}'
    
hewan = [
    Mamalia('paus','yihaaa'),
    Ovipar('ayam','kukuruyuk')
]

def bersuara(i):
    print(i.suara())
    
for i in hewan:
    bersuara(i)
    
#SUMPAH GUE NGERJAIN TANPA REFERENSI COK WKWKWKWK, BAGUS DEH JALAN