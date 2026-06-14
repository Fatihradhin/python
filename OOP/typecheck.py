#melakukan pengecekan terhadap objek apakah dia darii class tertentu atau subclass tertentu.
class Kendaraan:
    def __init__(self,typek,merk,tahun,warna):
        self.typek = typek
        self.merk = merk
        self.tahun = tahun
        self.warna = warna
        
b1 = Kendaraan('2736l','Bacakan',1998,'merah')
print(b1.__dict__)
#type check dengan cara
print(isinstance(b1,Kendaraan)) #True

#kalo subclass

class Motor(Kendaraan):
    def __init__(self, typek, merk, tahun, warna):
        super().__init__(typek, merk, tahun, warna)
        
        
m = Motor('k384lm','Ducati',2022,'merah')

print(isinstance(m,Motor))
#trus kalau mau tau parent nya sama atau gak
print(isinstance(m,Kendaraan))