frase = input("Ingrese la fase: ")
letra = input("Ingrese la letra: ")
cont=0
for caracter in frase:
    if caracter==letra:
        cont+=1
if cont>0:
    print("La letra "+letra +" se encontro "+ str(cont) + " veces")    
else:
      print("La letra " + letra+" no se encontro ")    