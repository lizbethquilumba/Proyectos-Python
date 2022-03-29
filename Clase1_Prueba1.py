nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
fullName=nombre+" "+apellido
anioNacimiento=int(input("Ingrese el anio de nacimiento: "))
anioActual=int(input("Ingrese el anio actual: "))
edad=anioActual-anioNacimiento
print("Su nombre completo: ",fullName )
print("Su edad es: ",edad)