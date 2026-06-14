#kalo sebelumnya itu kita menambahkan atrribut setelah divariabelkan, maka kita akan membuatnya lebih bagus dengan __init__
#__init__ adalah function yang akan otomatis dijalankan jika kita membuat sesuatu menggunakan class. Biasanya kan, fctn ga akan dijalankan kecualli lo panggil si fctn itu, nah init nih bocah petakilan yang selalu minta ngikut kalo bapanya pergi.
class Hero:
    def __init__ (self,name,hp,attackpow,defense): #self adalah si hero itu, yya pokook nya  gt
        self.name = name
        self.hp = hp
        self.attackpow = attackpow
        self.defense = defense
        
gatotkaca = Hero('Gatotkaca',200,32,85)  
herp = Hero('herp',200,35,65)
print(gatotkaca.name)
#nah, bagaimana dengan behavior? Next segment...
def sapahero (a,b):
    print(f'Hai {a.name} dan {b.name}')


sapahero(gatotkaca,herp)
