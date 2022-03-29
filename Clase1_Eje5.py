rescorrectas= int (input("Ingrese el numero de respuestas correctas:"))
respincorrectas=int (input("Ingrese el numero de respuestas incorrectas: "))
total= rescorrectas+respincorrectas
pCorrecto=(100/total)*rescorrectas
pIncorrecto=(100/total)*respincorrectas
print("Su puntaje final fue: "+str(rescorrectas)+"/"+str(total))
print("Su porcentaje de respuestas correctas es: %.2f y un porcentaje de respuetas incorrectas de: %.2f"%(pCorrecto,pIncorrecto))