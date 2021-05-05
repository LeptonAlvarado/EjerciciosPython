"""
Implemente una funci ́onvoid SumDiagonals(int data[N][M], int result[])que calcule la suma decada
una de las diagonales cuya orientaci ́on es hacia la derecha y abajo, en la matriz data, y almacenelos
resultados en el array result.
Ejemplo: ante la ejecuci ́on de la funci ́on con la siguiente matriz data:
[10   26
12    20
−5    4]
la funci ́on debe almacenar en result el siguiente contenido:{26,30,16,−5}
"""
lista_data = [[10,26], [12,20], [-5,4], [10, 3]]

def sumDiagonals(data, result):
    fila = 0
    for row in data:
        for elemt in range(len(row)):
            if fila == 0 and elemt == 1:
                result.append(data[0][1])
            elif fila != 0 and elemt == 1:
                suma = data[fila-1][elemt-1] + data[fila][elemt]
                result.append(suma)
        fila += 1

    result.append(data[len(data)-1][0])

    print(result)

sumDiagonals(lista_data, result=[])