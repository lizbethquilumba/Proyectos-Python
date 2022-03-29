sexo="m"
edad=67
cotizaciones=900
aniosServicio=25

if aniosServicio>=25 and cotizaciones>=750:
    if (sexo=="m" and edad>=60) or (sexo=="f" and edad>=55): 
      print("Usted aplica para ser jubilado")
    else:
        print("Usted aplica para se jubilado")
else:
        print("Usted no aplica para ser jubilado")