ta=input("Ingrese el tipo de articulo:")
ta = ta.lower()
va=float(input("Ingrese el valor del articulo:"))

if ta == "textil":
    vd1 = va * 0
    print("El valor de descuento es ", vd1)
else:
    if ta == "electrodomestico":
        vd2 = va * 0.037
        print("El valor de descuento es ", vd2)
    else:
        if ta == "cocina":
            vd3 = va * 0.042
            print("El valor de descuento es ", vd3)
        else:
            if ta == "videojuego":
                vd4 = va * 0.078
                print("El valor de descuento es ", vd4)
            else:
                print("El tipo de articulo no es valido")
                