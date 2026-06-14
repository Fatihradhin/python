import csv

nama = input('masukan nama: ')
ps = input('masukan psswrd: ')
with open('member.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([nama, ps])
    
