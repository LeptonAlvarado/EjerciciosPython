"""
Se tiene un arreglo de caracteres C y se sabe que el ´ultimo elemento de C es el único que contiene un
cero. Dar el código para contar las ocurrencias aisladas del carácter ’a’ (es decir, cuando los caracteres
vecinos a una ’a’ no sean ’a’s).

Ejemplo: ante la ejecución de la funci´on con la siguiente cadena de entrada:
{a, d, a, a, f, a, g, r, r, a, 0},
se debe devolver 3
"""

def obtener_ocurrencias(lista_caracteres):
    contador_ocurrencias = 0

    for datos in range(len(lista_caracteres)-1):
        if datos == 0:
            if lista_caracteres[0] == 'a' and lista_caracteres[1] != 'a':
                contador_ocurrencias += 1
        else:
            if lista_caracteres[datos-1] != 'a' and lista_caracteres[datos] == 'a' and lista_caracteres[datos+1] != 'a':
                contador_ocurrencias += 1

    print(contador_ocurrencias)

lista = ['a','a','a','f','a','h','a','r','r','a','0']
obtener_ocurrencias(lista)
