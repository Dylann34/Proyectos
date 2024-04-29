def contar_rectangulos(dimensiones_rectangulo, dimensiones_rectangulo_pequeno):
    ancho_rectangulo, alto_rectangulo = dimensiones_rectangulo
    ancho_rectangulo_pequeno, alto_rectangulo_pequeno = dimensiones_rectangulo_pequeno

    # Calcula cuántos rectángulos caben horizontalmente y verticalmente
    horizontales = ancho_rectangulo // ancho_rectangulo_pequeno
    verticales = alto_rectangulo // alto_rectangulo_pequeno

    # Calcula el total de rectángulos
    total_rectangulos = horizontales * verticales

    return total_rectangulos

# Función para obtener las dimensiones de un rectángulo desde el usuario
def obtener_dimensiones_rectangulo():
    ancho = int(input("Ingrese el ancho del rectángulo: "))
    alto = int(input("Ingrese el alto del rectángulo: "))
    return ancho, alto

# Obtiene las dimensiones del rectángulo grande
print("Ingrese las dimensiones del rectángulo grande:")
dimensiones_rectangulo_grande = obtener_dimensiones_rectangulo()

# Obtiene las dimensiones del rectángulo pequeño
print("Ingrese las dimensiones del rectángulo pequeño:")
dimensiones_rectangulo_pequeno = obtener_dimensiones_rectangulo()

# Calcula cuántos rectángulos pequeños caben dentro del rectángulo grande
cantidad_rectangulos = contar_rectangulos(dimensiones_rectangulo_grande, dimensiones_rectangulo_pequeno)

print("La cantidad de rectángulos de dimensiones", dimensiones_rectangulo_pequeno, "que caben dentro del rectángulo de dimensiones", dimensiones_rectangulo_grande, "es:", cantidad_rectangulos)
