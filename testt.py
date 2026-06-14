def homepage():
    print('selamat datang king, ')
    



a = 0
    
while a == 0:
    b = input('pisang atau jagung?: ').lower()
    if b == "pisang":
        print('coba lagi')
    else:
        print('gacor kang!!! balik kke homepage ya')
        a +=1
        
while a == 1:
    homepage()
    break