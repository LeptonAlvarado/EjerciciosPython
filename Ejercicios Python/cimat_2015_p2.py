"""
Implemente una funci ́onvoid SumDiagonals(int data[N][M], int result[])que calcule la suma decada
una de las diagonales cuya orientaci ́on es hacia la derecha y abajo, en la matriz data, y almacenelos
resultados en el array result.
Ejemplo: ante la ejecuci ́on de la funci ́on con la siguiente matriz data:
[10   26    3
12    20    5
−5    4     2]
la funci ́on debe almacenar en result el siguiente contenido:{26,30,16,−5}
"""
lista_data = [[10,26], [12,20], [-5,4]]

def sumDiagonals(data, result):
    fila = 0
    indice_f = 0
    lst =[]
    for i in range(len(data[0])):
        lst.append(0)
    data.append(lst)
    for row in data:
        indice_c = len(data)-1
        for elemt in range(len(row)):
            indice_f = fila -1
            if indice_f < 0 and elemt != 0:
                result.append(data[fila][elemt])
            elif elemt != 0:
                suma = data[fila-1][elemt-1] + data[fila][elemt]
                result.append(suma)
        fila += 1
    print(result)

sumDiagonals(lista_data, result=[])