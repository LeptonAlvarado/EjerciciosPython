"""
Escribir una funci ́on que determine si un numero entero pasado en par ́ametro es una potencia de 2 o no

Ejemplo: ante la ejecuci ́on de la funci ́on con el entero 7 de entrada, se devolver ́af alse
"""
def es_potencia_dos(numero):
    m = numero-1
    if numero & m == 0:
        return True
    else:
        return False

print(es_potencia_dos(7))