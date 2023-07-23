#calcular el area de un triangulo
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Pedimos al usuario que ingrese la base y la altura del triángulo
try:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))

    # Llamamos a la función para calcular el área y mostramos el resultado
    area_del_triangulo = calcular_area_triangulo(base, altura)
    print("El área del triángulo es:", area_del_triangulo)

except ValueError:
    print("Error: Asegúrate de ingresar valores numéricos válidos para la base y la altura.")
