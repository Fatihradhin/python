#dalam py ada logika biar jalan. ada 3
#and, or, not
x = 14
y = 13

#and adalah logika dimana 2 kondisi nya harus true, kalo satu aja ga true, jadi false
print(x > y and y < x) #outputnya akan true
print(x == y and y > x) #outputnya akan false

#or adalah logika dimana yang diambil cuma salah satu kondisi nya aja, dia akan true terus KECUALI kedua opsinya false baru dia false
print(x < y or x != y) #true
print(x < y or x == y) #false

#not adalah logika dimana dia membalikan nilai logika. singkatnnya, kalo harusnya true jadi false
print(not y > x) #harusnya false karena y ga lebih besar dari x tapi karena not, jadi dibalikan nilai logikanya
print(not y != x) #harusnya true karena y ga sama dengan x tapi karena not, jadi dibalikan nilai logikanya
 
 #oke, dah