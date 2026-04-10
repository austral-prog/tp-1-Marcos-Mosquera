from math import pi


def circle():
    """
    Ejercicio 6 - Geometría de Círculo

    Dado el radio de un círculo, calcular e imprimir:
    1. El área (π × radio²)
    2. La circunferencia (2 × π × radio)
    """
    radio = 5
    PI = 3.1416 # Da error con 3.14
    area = PI * radio**2
    print(area)
    circunferencia = 2 * PI * radio
    print(circunferencia)
