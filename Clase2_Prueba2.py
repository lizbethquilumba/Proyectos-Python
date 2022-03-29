numeromaximo=100

for i in range(1,numeromaximo):
    
    if i%3==0 and i%5==0:
        print("Es divisible para 3 y 5: fizzbuzz",i)
    elif i%3==0:
        print("Es divisible para 3: fizz",i)
    elif i%5==0:
        print("Es divible para 5: buzz",i)
