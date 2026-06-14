class Character:
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power
        
    def  attack(self,other):
        other.health -= self.power
        print(other.health)
        
    def is_alive(self):
        True if self.health >0 else False
        
c1 = Character('Ujang',100,30)
c2 = Character('ucup',100,30)

c1.attack(c2)
c2.is_alive()