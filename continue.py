#kalo break itu menghentikan paksa perulangan, continue menghentikan perulangan apabila sebuh statment itu false, dan melanjutkan kembali perulangan apabila true.

for i in range (10): #ulang setiap index di range 10
    if i % 2 == 0: #kalo i dibagi 2 sisa 0, maka continue(lanjutkan perulangan) kalo gak 0, maka di print.
        continue
    print(i)
    
#output = 1 3 5 7 9