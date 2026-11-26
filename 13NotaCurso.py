n1=float(input("Ingrese su primera nota:"))
n2=float(input("Ingrese su primera nota:"))
n3=float(input("Ingrese su primera nota:"))
n4=float(input("Ingrese su primera nota:"))
n5=float(input("Ingrese su primera nota:"))
nt = (n1+n2+n3+n4+n5)/5
if n1 >= 0 and n1 <= 5 and n2 >= 0 and n2 <= 5 and n3 >= 0 and n3 <= 5 and n4 >= 0 and n4 <= 5 and n5 >= 0 and n5 <= 5:
    print("La definitva es: ", nt)
    if nt > 3.5:
        print("El estudiante gano el curso")
    else:
        print("El estudiante perdio el curso")
else:
    print("Error en el rango de notas permitido")
