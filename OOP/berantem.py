import time
import sys
class Hero:
    @classmethod
    def mage(cls,name,hp,attackpower,defense):
        return cls('mage',name,hp,attackpower,defense)
    @classmethod
    def tank(cls,name,hp,attackpower,defense):
        return cls('Tank',name,hp,attackpower,defense)
    @classmethod
    def carry(cls,name,hp,attackpower,defense):
        return cls('Carry',name,hp,attackpower,defense)
    
    def __init__ (self,role,name,hp,attackpower,defense): #self adalah si hero itu, yya pokook nya  gt
        self.role = role
        self.name = name
        self.hp = hp
        self.attackpower = attackpower
        self.defense = defense
        
    def attack (self, Hero):
        print(f'{self.name} attack {Hero.name}')
        damagea = self.attackpower**2
        damageb = self.attackpower + Hero.defense
        damage = damagea // damageb
        if Hero.role == 'Tank':
            bonus = int(Hero.hp * 0.015)  
            damage += bonus
        Hero.hp -= damage
        print(f'hp {Hero.name}: {Hero.hp}')


    def unattack (self, Hero):
        print(f'{self.name} attack by {Hero.name}')
        damagea = Hero.attackpower**2
        damageb = Hero.attackpower + self.defense
        damage = damagea // damageb
        if self.role == 'Tank':
            bonus = int(self.hp * 0.015)  
            damage += bonus
        self.hp -= damage
        print(f'hp {self.name}: {self.hp}')

gatotkaca = Hero.tank('Gatotkaca',150,27,60)
herp = Hero.carry('Herp',100,38,80)
Invoker = Hero.mage('Invoker',100,34,37)

def battle (a,b):
    print(f'\n{a.name} akan melawan {b.name}')
    teks = 'Bersiap...'
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(0.3)
    time.sleep(2)
    print('\n')
    input('Enter untuk menyerang')
    a.attack(b)

def app ():
    print(gatotkaca.__dict__)
    print(herp.__dict__)
    a = int(input('mau pilih siapa? Gatotkaca(1) atau Herp(2): '))
    if a ==1:
        battle(gatotkaca,herp)
    elif a ==2:
        battle(herp,gatotkaca)
    else:  
        print()


app()