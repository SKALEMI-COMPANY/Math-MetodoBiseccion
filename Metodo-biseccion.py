# Skalemi Company
# Si te surge alguna duda, contáctame.
# michaelvinces.skalemi@gmail.com

import math

def biseccion(f, a, b, tolerancia):
  
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return "No se puede garantizar la existencia de una raíz en el intervalo dado."

    n_iteraciones = 0
    c_anterior = None

    while (b - a) / 2 > tolerancia:
        c = (a + b) / 2
        fc = f(c)

        n_iteraciones += 1
        print(f"Iteración {n_iteraciones}:")
        print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6f}")

        if c_anterior is not None:
            Porcentaje_error = abs((c - c_anterior) / c) * 100
            print(f"Porcentaje de error: {Porcentaje_error:.2f}%")

        if fc == 0:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        c_anterior = c
        #Imprime la ultima iteración
        if (b-a)/2<tolerancia:
            c_anterior = c
            c = (a + b) / 2
            fc = f(c)
            n_iteraciones += 1
            print(f"Iteración {n_iteraciones}:")
            print(f"a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6f}")
            error = abs((c - c_anterior)) * 100
            print(f"Porcentaje de error: {error:.2f}%")

    return (a + b) / 2

# Solicitar la ecuación al usuario
ecuacion = input("Ingrese la ecuación: ")
f = lambda x: eval(ecuacion)

# Solicitar los límites y la tolerancia al usuario
a = float(input("Ingrese el límite inferior: "))
b = float(input("Ingrese el límite superior: "))
tolerancia = float(input("Ingrese la tolerancia: "))

# Ejecutar el método de bisección
print(f"\nMétodo de bisección para la ecuación: {ecuacion}")
print(f"Intervalo [{a:.6f}, {b:.6f}] con tolerancia {tolerancia:.6f}")
print("Iteraciones:")

Resultado = biseccion(f, a, b, tolerancia)

print(f"\nLa aproximación de la raíz es: {Resultado:.6f}")
