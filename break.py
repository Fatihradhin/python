#bagian dari loop dimana dia bisa menghentikan loop meski nili nya masih true
x = 1

while x <= 10:
    print(x)
    if x == 5:
     break
    x +=1
#biasanya digabung sama while true, karena kondisi whille yang akan selalu true, perlu break sebgai jalan keluarnya

#misalnya ada kasus batas salah  memasukan password, break disini bisa jadi jalan.
attemps = 2

while True:
    statment = input("Masukan password: ")
    if statment != "admin123":
        print(f"password salah, sisa percobaan {attemps}")
        attemps -=1
        if attemps ==-1:
            print("kesempatan habis. kamu di blokir")
            break
    else:
        print("password benar")
        print("welcome to the los pollos hermanos\nmy name is gustavo radhinn")
        break
    
