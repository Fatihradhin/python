#multiple inheratenc adalah kondisi dimana child punya 2 parent, agar child mewarisi 2 behavior berbeda.
class Mage:
    def __init__(self,name):
        self.name = name
        
    def magic_damage(self):
        print(f'Magic damage by {self.name}')
    def magically(self):
        print(f'Potion of invisibility used by {self.name}')
        
class Fighter:
    def __init__(self,name):
        self.name = name
        
    def pyshically(self):
        print(f'regen activated by {self.name}')
    def  pyshical_damage(self):
        print(f'super punch launched by {self.name}')
        
#inilah pelakunya
class Hybrid(Mage,Fighter):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return self.name
        
a = Hybrid('Makar')
a.magically()
a.magic_damage()
a.pyshical_damage()
a.pyshically()

#Namun, hal  seperti ini tidak disarankan, karena bsa menyebabkan diamond problem.  