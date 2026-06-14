list_barang = {
    'popok bayi': 39000,
    'kopi': 17500,
    'beras': 70000,
    'mie instan': 30000,
    'gula': 15000,
}

print('Daftar barang dan harga\n popok bayi: 39000\n kopi: 17500\n beras: 70000\n mie instan: 30000\n gula: 15000')

cust = input("mau belanja apa: ")
cek = cust.split(',') 
total = []
print(" ")
for barang in cek:
    barang = barang.strip()
    print(f"{barang} Rp.{list_barang[barang]:,}") 
    total.append(list_barang[barang])
akhir = sum(total)
print(" ")
print(f'Total Berbelanja:\n{akhir:,}')
print(" ")
diskon = True if akhir >50000 else False
if diskon == True:
    akhir -=500
    print(f"Diskon:\nRp.500")
else:
    print('Diskon:\n-')
print(" ")    
print(f'Total: {akhir:,}')

