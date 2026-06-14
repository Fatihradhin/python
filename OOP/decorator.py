#ketika kita mau manggil method di class pasti gini
class Motor:
    def __init__(self,name,seri):
        self.name = name
        self.seri = seri
        
    def maju(self):
        print(f'{self.name} Maju')
        
m = Motor('Matar',932847)
m.maju() #kaya gini, cuma ada yang lebih clean jadi kayak atribut biasa..

#tambahin @property, alat untuk menampilkan method seperti atribut biasa..

class Robot:
    def __init__(self,name,seri):
        self.name = name
        self.seri = seri
        
    @property
    def intro(self):
        print(f'Hai, namaku {self.name}, aku robot asli medan')
        
u = Robot('Ucok',7328)

u.intro #lebih clean bukan?

#terus ada static method yang ga perlu self,class.

class Smartphone:
    def __init__(self,name,seri):
        self.name = name
        self.seri = seri
    
    @staticmethod
    def buka_instagram():
        print('Instagram dibuka')
        
Infinix = Smartphone('Infinix',2386)
Infinix.buka_instagram()

#intinya dia tuh buat lu yang mau taruh method di dalam class, tanpa terkoneksi dengan self atau class itu sendiri(Method biasa.)

#ada lagi namanya classmethod yang akses ke class nya, bukan ke object(self)

class Lamp():
    @classmethod
    def basiclamp(cls,name):
        return cls(name,10)
    
    @classmethod
    def midlamp(cls,name):
        return cls(name,35)
    
    @classmethod
    def megalamp(cls,name):
        return cls(name,50)
    
    def __init__(self,name,watt):
        self.name = name
        self.watt = watt
lamp1 = Lamp.midlamp('Haisyu')

print(lamp1.name)
print(lamp1.watt)

#intinya buuat variasi, alih lalih pake init terus tulis satu satu, mending buat "intruki tambahan" biar langsung sat set.


class Bankaccount:
    __name = ''
    __saldo = 0
    
    def __init__(self,name):
        self.__name = name
        
    def get_saldo(self):
        return self.__saldo
    
    def topup(self,jumlah):
        self.__saldo += jumlah
        
    def take_money(self,total):
        if self.__saldo < total:
            raise ValueError('Saldo ga cukup!')
        self.__saldo -= total
        print(f'Saldo berhasil ditarik, sisa uang {self.__saldo}')
    
b1 = Bankaccount('Rapphilemon')
b2 = Bankaccount('Radhin')
b2.topup(40)
print(b2.get_saldo())
print(b1.get_saldo())
