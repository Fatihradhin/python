#abc method (abstract base class) adalah class yang tidak bisa di isi atau diapakan kali. dia murni hanya blue print yang memberikan parameter dan aturan main.
#analogi sederhana, abc tuh kayak blueprint rumah, di sana ada jendla, pintu, dll. tai ga dintentuin sama blue print nnya, mau jendela nya bulat,kotak segi tiga, hexagon, pentagon, terserah.
from abc import ABC, abstractmethod

class Home:
    
    @abstractmethod
    def window(self,shape):
        pass
    @abstractmethod
    def door(self,shapes):
        pass
    @abstractmethod
    def wall(self,material):
        pass

class CustomHome(Home):
    def __init__(self,name,shape,shapes,material):
        self.name = name
        self.shape = shape
        self.shapes = shapes
        self.material = material
        
    def window(self, shape):
        return f'Bentuk jendela{self.name} adalah {self.shape}'
    def door(self,shapes):
        return f'Bentuk pintu {self.name} adalah {self.shapes}'
    def wall(self,material):
        return f'tembok di {self.name} menggunakan material {self.material}'
        
        
rmh = CustomHome('woodhome','circle','rectanggle','wood')

print(rmh.window('circle'))