num=int(input("Ingrese su numero:"))
min1=int(input("Ingrese el valor minimo del intervalo 1:"))
max1=int(input("Ingrese el valor maximo del intervalo 1:"))
min2=int(input("Ingrese el valor minimo del intervalo 2:"))
max2=int(input("Ingrese el valor maximo del intervalo 2:"))
min3=int(input("Ingrese el valor minimo del intervalo 3:"))
max3=int(input("Ingrese el valor maximo del intervalo 3:"))

if min1 >= max1 or min2 >= max2 or min3 >= max3:
    print("Error: los limites no son validos")
else:
    if (min1 < max2 and max1 > min2) or (min1 < max3 and max1 > min3) or (min2 < max3 and max2 > min3):
        print("Error: los intervalos se cruzan")
    else:
        if (num > min1 and num < max1) or (num > min2 and num < max2) or (num > min3 and num < max3):
            print("El numero esta dentro de los intervalos")
        else:
            print("El numero esta fuera de los intervalos")

            