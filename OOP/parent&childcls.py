#ini adalah parent class
class Elektronic:
    def __init__(self,merk,eltype,colour,power_consumption=None): 
        self.merk = merk
        self.type = eltype
        self.colour = colour
        self.pc = power_consumption
    
    def on(self):
        print(f'Menyalakan {self.merk}')

class Handphone(Elektronic):
    def __init__(self, merk, eltype, colour,batery):
        super().__init__(merk, eltype, colour)
        self.batery = batery
    
    def onit(self):
        print(f'Turn on the device...{self.merk}')
        super().on()
h1 = Handphone('Infinix','x100','Cyan','6000 mAh')
h1.on()

