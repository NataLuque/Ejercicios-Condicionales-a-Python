num=int(input("Ingresa tu numero del 0 al 20"))
if num >= 0 and num <= 20:
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13 or num == 17 or num == 19:
        print("El numero es un numero primo")
    else:
        print("El numero no es un numero primo")
else:
    print("El numero no esta entre el rango")
