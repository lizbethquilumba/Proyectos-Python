lista  = [1,"Hola",3.5,False]

while len(lista)>0:
    print(lista)
    elem = int (input("Ingrese la posicion del elemento a eliminar: "))
    if elem>len(lista)-1:
        print("El elemento esta fuera de rango\n")
        continue
    del(lista[elem])
    print()
