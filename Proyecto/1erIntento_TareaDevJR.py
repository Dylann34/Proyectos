import math
def calcular_paneles(dimensiones_panel, dimensiones_techo):
    # Ahora hay que solicitar las dimensiones de los paneles y del techo
    a = int(input("Ingrese la dimensión A del Panel: "))
    b = int(input("Ingrese la dimensión B del Panel: "))
    x = int(input("Ingrese la dimensión X del Techo: "))
    y = int(input("Ingrese la dimensión Y del Techo: "))
    dimensiones_panel = a, b
    dimensiones_techo = x, y 
    
    #Calcula cuántos paneles caben horizontalmente y verticalmente
    paneles_horizontales = a / x
    paneles_verticales = b / y
    
    # Calcula el total de rectángulos
    total_paneles = paneles_horizontales * paneles_verticales

    # Calcula cuántos paneles caben dentro de las dimensiones del techo
    cantidad_paneles = calcular_paneles(dimensiones_panel, dimensiones_techo)

    print(f"La cantidad de paneles que caben dentro de las dimensiones del techo ingresadas es: {cantidad_paneles}")

    return total_paneles
calcular_paneles()