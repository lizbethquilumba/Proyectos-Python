from random import randint
def llenarSec(n):
    lista = []
    for i in range(1,n+1):
        lista+=[i]
    return lista

def llenarAleatorio(n):
    lista = []
    num = randint(1,n)
    lista+=[num]
    for i in range(n-1):
        while num in lista:
            num = randint(1,n)
        lista+=[num]   
    return lista  
      

listaA = llenarSec(20)
listaB = llenarAleatorio(20)
print(listaA)
print(listaB)
for i in range(len(listaA)):
    print("A la persona: ",listaA[i],"es pareja con: ",listaB[i])
