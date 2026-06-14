#jadi, sebelumnnya udah belajar list[] nah sekarang tuple()
#nah, tuple ini sama kayak list, bisa di isi apa aja. string, float, anything. dan, as you know, tuple itu data  yang tetap  dan ga bisa dimodifikasi
a = ("nasi uduk", "bakso", "mie ayam")
#a[1] = "Karedok"
print(a)
#object does suport bla bla katanya, tapi lo bisa ubah isi tuple dengan cara.. lo konversi tuple itu ke list. gimana tuh..?
b = list(a) #buat variable baru sebagai "rumah" buat tuple yang akan ditapil kan dengan mode list
#abis tuh, lo langsung ubah dah
b[1] = "karedok"
print(b)
#sebelum iitu jangan lupa baris ke-4 di komen dulu, and....voila!!
#you can also to convert the list into the tuple like before.
c = tuple(b)
print(c)

#oke, dah