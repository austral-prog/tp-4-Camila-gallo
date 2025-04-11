def line():
    import math
    a= float(input("Ingrese el coeficiente A:"))
    b= float(input("Ingrese el coeficiente B:"))
    x1= float(input("Ingrese el coeficiente X1:"))
    x2= float(input("Ingrese el coeficiente X2:"))
    print(f"El coeficiente A de su ecuación de la recta es: {a}" )
    print(f"El coeficiente B de su ecuación de la recta es: {b}" )
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}" )
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}" )
    print("")
    Y1= a*x1+b
    Y2= a*x2+b
    print('Para la siguiente ecuación: \n\tY = 2.3X + -4.0')
    print("")
    print(f"Dados los siguientes puntos: \n\tP1 ({x1},{Y1}) \n\tP2 ({x2},{Y2})")
    distancia = math.sqrt((x2 - x1)**2 + (Y2 - Y1)**2)
    print("")
    print(f"La distancia entre ellos es {distancia}")
    
