
lista = [34,67,89,90,37,67,59]
suma=0
PesoMax=lista[0]

for i in range (len(lista)):
    for j in range(i+1,len(lista)):
        suma =lista[i]+lista[j]
        if suma<=150:
           print("La suma de:",lista[i],"+",lista[j],"=",suma)
           if suma>PesoMax:
               PesoMax=suma
print("El peso maximo es: ",PesoMax)               

           


    

       
