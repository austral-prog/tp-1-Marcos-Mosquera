def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas=int(total_segundos/3600)
    minutos=int((total_segundos-(horas*3600))/60)
    total_segundos=total_segundos-(minutos*60)-(horas*3600)
    print(horas)
    print(minutos)
    print(total_segundos)