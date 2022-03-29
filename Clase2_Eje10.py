numero = 20
r = "El numero "+ str(numero) + " es divisible para:  "
for i in range(1,((numero//2)+1),1):
    if numero%i==0:
        r+=str(i)+" , "
r+= str(numero)        
print(r)        