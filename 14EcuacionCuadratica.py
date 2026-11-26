a=float(input("Ingrese el valor de a:"))
b=float(input("Ingrese el valor de b:"))
c=float(input("Ingrese el valor de c:"))

if a != 0:
    dis = (b*b-4*a*c)
    if dis >= 0:
        print("La ecuacion cuadratica tiene solucion")
    else:
        print("La ecuacion cuadratica no tiene solucion")
else:
    print("La ecuacion no tiene solucion")