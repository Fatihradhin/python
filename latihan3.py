class Stuff:
    def __init__(self,product,price):
        self.product = product
        self.price = price

baja = Stuff('Baja',1000)

class User:
    def __init__(self):
        pass

class Trolly:
    ls = []
    lp = []
    def __init__(self):
        pass
    
    def add(self,product):
        print(product.__dict__)
    
    def jawa(self):
        print('berhasil jawa')


u = User()
t = Trolly()
u.trolly = t

u.trolly.add(baja)