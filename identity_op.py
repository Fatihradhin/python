#Operator identitas adalah cara bagaimana kita mengenali suatu variabel di dalam memori di Python. Kita dapat membandingkan isinya bila isinya identik ataupun lokasi memorinya.
#operatornya cuma dua, is, is not, tapi ada satu lagi tambahan op yang masuk ke sinni yaitu id(). lagi lagi ini true/false ya
angka1 = 10
angka2 = 10
angka3 = "10"

print (angka1 is angka2) #dia bakalan mastiin meskipun variable beda tapi nilai nya sama maka true
print (id(angka1) is id(angka2)) #ini semacam ngasih identitas, jadi python ngasih identitas berupa nomer acak yang unik ke vaiable ini
print (angka1 is not angka3) #ini bakalan mastiin kalo isinya tuh beda, dari isi maupun type data ny
print (angka1 is angka3)