"""
Se tiene un arreglo de caracteres C y se sabe que el ´ultimo elemento de C es el ´unico que contiene un
cero. Dar el c´odigo para contar las ocurrencias aisladas del car´acter ’a’ (es decir, cuando los caracteres
vecinos a una ’a’ no sean ’a’s).

Ejemplo: ante la ejecuci´on de la funci´on con la siguiente cadena de entrada:
{a, d, a, a, f, a, g, r, r, a, 0},
se debe devolver 3
"""

lista = ['a','g','a','f','a','h','a','r','r','a','0']
contador_a = 0
contador_otros = 1
contador_ocurrencias = 0

for datos in lista:
    if datos == 0:
        contador_otros += 1
        if contador_otros == 2:
            contador_ocurrencias += 1
        break
    if datos == 'a':
        contador_a += 1
        if contador_a == 2:
            contador_otros = 0
            contador_a = 0
    if datos != 'a':
        contador_otros += 1
        if contador_otros == 2 and contador_a == 1:
            contador_ocurrencias += 1
            contador_otros = 1
            contador_a = 0
        elif contador_otros == 2 and contador_a == 0:
            contador_otros = 1

print(contador_ocurrencias)
