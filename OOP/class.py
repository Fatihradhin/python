#class is a template to make an object. Objects have two things: Attribute and Behavior. 
class Hero:
    pass

hero1 = Hero() # hero1 its an object

#now you can add this object with some attributes
hero1.name = 'Lamnabada'
hero1.hp = 100
hero1.attackpow = 36
hero1.defense = 45
print(hero1.__dict__)