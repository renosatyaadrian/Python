a=100
b=1000

def kuadrat(args):
    total = a**2
    print("Hasil nilai kuadrat",args,"adalah: ",total)
    return total

k = kuadrat(4)
print(k)
print("-"*50)

def tambah(args1,args2):
    global a,b
    a=args1
    b=args2
    total = a+b
    print(a,"+",b,"=",total)
    return total

def kali(args1,args2):
    global b
    b=args2
    total = a*b
    print(a,"x",b,"=",total)
    return total

#anonymous function
bagi = lambda x,y: x/y


b = tambah(5,2)
c = kali(100,2)
d = kali(b, tambah(3,2))
e = bagi(4,2)

print(c)
print(d)
