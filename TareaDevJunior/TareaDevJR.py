import math

#  Se solicitan las dimensiones de los Paneles
a = int(input("Ingrese la dimensión A del Panel: "))
b = int(input("Ingrese la dimensión B del Panel: "))

#  Se solicitan las dimensiones del Techo
x = int(input("Ingrese la dimensión X del Techo: "))
y = int(input("Ingrese la dimensión Y del Techo: "))

def calcular_paneles(a, b, x, y):
    #Calcula cuántos paneles caben horizontalmente y verticalmente
    paneles_horizontales = x / a
    paneles_verticales = y / b
    
    # Calcula el total de paneles
    total_paneles = paneles_horizontales * paneles_verticales

    return total_paneles

total_paneles = calcular_paneles(a, b, x, y)

print(f"La cantidad de paneles que caben dentro de las dimensiones del techo ingresadas es: {int(total_paneles)}")