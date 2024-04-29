import math

#  Se solicitan las dimensiones de los Paneles
a = int(input("Ingrese la dimensión A del Panel: "))
b = int(input("Ingrese la dimensión B del Panel: "))

#  Se solicitan las dimensiones del Techo
x = int(input("Ingrese la dimensión X del Techo: "))
h = int(input("Ingrese la dimensión h del Techo: "))

def calcular_paneles(a, b, x, h):
    # Verifica si el techo es un triángulo isósceles
    if x != h:
        print("El techo debe ser un triángulo isósceles para usar esta función.")
        return 0
    
    # Calcula el área de los paneles solares
    solar_panel_area = a * b
    
    # Calcula el área del techo
    roof_area = (x * h) / 2
    
    # Calcula cuántos paneles solares caben en el techo
    calcular_paneles = int(roof_area / solar_panel_area)
    
    return calcular_paneles

max_count = calcular_paneles(a, b, x, h)
print(f"La máxima cantidad de Paneles que caben en este techo es: {int(max_count)}")