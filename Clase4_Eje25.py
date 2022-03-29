
def imprimir (tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print("]") 

def LlenarVacio(n):
    tabla =[]
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[" "]
    return tabla 

def asteriscos(tabla,simbolo):
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i==len(tabla)//2 or j==len(tabla)//2 or i==j or i+j==(len(tabla)-1):
                tabla[i][j]=simbolo    

tabla= LlenarVacio(5)
imprimir(tabla)  
asteriscos (tabla,"*")
imprimir(tabla)          
