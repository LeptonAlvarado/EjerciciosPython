"""
Se tiene un arreglo de caracteres C y se sabe que el ´ultimo elemento de C es el ´unico que contiene un
cero. Dar el c´odigo para contar las ocurrencias aisladas del car´acter ’a’ (es decir, cuando los caracteres
vecinos a una ’a’ no sean ’a’s).

Ejemplo: ante la ejecuci´on de la funci´on con la siguiente cadena de entrada:
{a, d, a, a, f, a, g, r, r, a, 0},
se debe devolver 3
"""

lista = ['a','a','a','f','a','h','a','r','r','a','0']
contador_ocurrencias = 0

for datos in range(len(lista)-1):
    if datos == 0:
     if lista[0] == 'a' and lista[1] != 'a':
         contador_ocurrencias += 1
    else:
        if lista[datos-1] != 'a' and lista[datos] == 'a' and lista[datos+1] != 'a':
            contador_ocurrencias += 1

print(contador_ocurrencias)
