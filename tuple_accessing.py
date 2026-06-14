#sebenarnya, buuat access tuple sama kyk list(orang satu jenis kocak)
a = ("nasi ayam", "gorengan", "ikan bakar")
print(a[2]) #cara indeks
for i in a:
    print(i) #loop for
    
hasil = list(
    map( 
        lambda x: x.swapcase(), a #pakai map()
    )
)
print(hasil)

hasil2 = list(
    filter( #ini fiter, as you know, dia harus bersyarat (true/false)
        lambda x: ("e" in x) or ("u" in x)
        , a
    )
)
print(hasil2)

#ada yang nama nya reduce() nah  dia ini simple nya menggabungkan jadi satu
#rreduce ga bisa ditulis biasa, karen dia bukan uilt n fcntn, jadi lo harus...
from functools import reduce 
#that's what you need

ab = ("fatih","radh")

hasil3 = list(
    reduce(
        lambda x, y: x + y, ab
    )
)
print(hasil3)

h = """
konima
"""