#function adalah sebuah hal yang bisa mempersingkat. diawali dengan def nama_function():
def sambutan():
    print("selamat datang")
    
#lalu bisa diberikan parameter yaitu dengan cara masukin argumen di () nya, kalo lleuh dari satu argumen, pakai koma
def sapa(nama):
    print(f"hai, {nama}.\n Senang bertemu denganmu")
    
sambutan()
x = input(f"siapa namamu?: ")
sapa(x)
print("<------------------------>")
#lalu ada return, nah return ini bisa nyimpen nilai fungsi ke variable, kalo kita ga pakai return, hasil dari fungsi is gone.
def test(a, b):
    return a * b

hasil = test(7, 8)
print(hasil)
print("<--------------------->")
#with str
def aku(nama):
    return "hai, " + nama

halo = aku("ujang")
print(halo, "Senang bertemu dengan anda")
print("<------------------------------->")
 #bisa juga kita issin by default, jadi meski kosong, dia bakalan tetep keisi(opsional)
 
def perkenalan (nama, kendaraan="Motor"):
     return nama + kendaraan

huhu = perkenalan("Ujang")
print(huhu)
print("<----------------->")
#keyword argument, memungkin kan kita menullis parameter tidak sesuai dengan urutannya. yaitu dgn cara menulis parameter itu sendiri.
def idnt(name, umur, kota):
    print(f"nama saya {name}")
    print(f"saya berumur {umur} tahun")
    print(f"saya berasal dari kota {kota}")
    print("<--------------------------------->")
    
idnt("Ujang", 18, "Tasikmalaya") #ini versi berururt
idnt(kota="Tasikmalaya", umur=18, name="Ujang")
    #ini versi acakadut, tapi output tetep terurut
    
