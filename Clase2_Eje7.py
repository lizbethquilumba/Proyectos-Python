from random import randint
#randint(x,y)"Genera numero aleatorio entero entre "x" y "y"
#randin "Genera numero aleatorio entre 0 y 1"
#randrange (x,y,p)"Genera numero aleatorio entero enre "x" y "y" con un paso de p"
#unifrom(x,y)"Genera numero aleatorio de tipo flotante entre "x" y "y" "

ZonaUsuario=int (input("En que zona desea disparar? : "))
ZonaPortero=randint(1,6)

print("La zona cubierta por el portero es: ",ZonaPortero)

if ZonaUsuario==ZonaPortero:
    print ("No ha sido un gol")
else:
    print("Gool")
