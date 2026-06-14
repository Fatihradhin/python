#ada namanya set. dia ituu tipe  list yang ga berurutn dan ga punya elemen duplikat. kalo list kan ia bisa duplikat tuh.
#set ditulis pake {} atau set() 
a = {"gaga", "gaga"}
print(a)
#dia cuma nnampilin 1 gaga, kalo list bisa dua duanya.
#kalo mau nambahin data pake add(value)
a.add("baba")
print(a)
#buat hapus pake remove(value)
a.remove("baba")
print(a)
#buat aksesnya, pakai loop for, karena dia ga ada index
for urut in a:
    print(urut)