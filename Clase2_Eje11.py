anioInicio= 1500
anioFinal=2022
#En el for poner el final es obligatorio
#El inicio es opcional
r = "Los anios bisiestos entre "+str(anioInicio) + " y "+str(anioFinal)+" son: "
for i in range(anioInicio,anioFinal):
    if (i%4==0 and i%100!=0) or i%400==0:
        r=r+str(i)+" , "
print(r)