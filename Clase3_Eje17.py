saldo = 0
op = 0
while (op!=3):
    op=int (input("Ingrese opcion: \n1.-Deposito\n2.-Retiro\n3.-Salir"))
    if op<0 or op>3:
        print("Opcion o valida")
        continue
    if op ==1:
        cant = float (input("Ingrese cantidad: "))
        saldo+=cant
    elif op==2:
        cant=float(input("Ingrese cantidad: "))
        if cant>saldo:
            print("No puede retirar esa cantidad")
        else:
            saldo-=cant
    elif op==3:
        print("Saliendo...")
print("Su saldo  total es: ",saldo)        