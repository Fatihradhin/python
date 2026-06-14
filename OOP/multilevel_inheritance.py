#multiple inheritance adalah sebuah cara pewarisan class berantai. Inntinya gt.
class Atlet:
    def __init__(self,name,behavior=None):
        self.name = name
        self.behavior = behavior
        
    
#pewarisan pertama
class Baller(Atlet):
    def __init__(self, name, ocuppation):
        super().__init__(name)
        self.ocuppation = ocuppation
    
    def __str__(self):
        return self.name + ' ' + self.ocuppation
a = Baller('Sami Khedira','Football Player')

print(a)

#pewarisan ketiga

class Volley(Baller):
    def __init__(self, name, ocuppation):
        super().__init__(name, ocuppation)
    
b = Volley('Janan','Volleyball player')

print(b)
