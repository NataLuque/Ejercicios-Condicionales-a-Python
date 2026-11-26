num=int(input("Ingrese su numero:"))
valormi=int(input("Ingrese el valor minimo del intervalo:"))
valorma=int(input("Ingrese el valor maximo del intervalo:"))

if num >= valormi and num <= valorma:
    print("Tu numero se encuentra por dentro del intervalo")
else:
    print("Tu numero se encuentra por fuera del intervalo")