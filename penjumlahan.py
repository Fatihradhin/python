def tambah (a,b):
    c = a + b
    return c

def tambahan (a):
    return a +1

numbers = [1,2,3,4,5,6,7,8,9,10]
afternum = []
for i in numbers:
    afternum.append(tambahan(i))
print(afternum)