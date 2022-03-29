n = 10
f = 4

def vasos (n,x):
    total =0
    while n>=x:
         reciclados = n//x
         sobran = n%x
         total += reciclados
         n = reciclados + sobran
         print("N: ",n,"Reciclados: ",reciclados,"sobran: ",sobran,"total: ",reciclados)    
    return total 

n=30
x=8
print(vasos(n,x))    