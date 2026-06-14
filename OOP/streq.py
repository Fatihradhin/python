class Hero:
    def __init__(self,name,role,hp,attpow,defense):
        self.name = name
        self.role = role
        self.hp = hp
        self.attpow = attpow
        self.defense = defense
        
    def __str__(self):
        return (f'Nama hero: {self.name}\nRole nya: {self.role}')
    
    def __eq__(self, other_heroes):
        return self.attpow == other_heroes.attpow, self.role == other_heroes.role
    
hero1 = Hero('Juggernaut','Carry',120,58,6)
hero2 = Hero('Wraith King','Carry',120,62,3)

print(hero1)
print(hero1 == hero2)