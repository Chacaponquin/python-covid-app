def contDivisibleByThree(matrix):
    if len(matrix) == 0:
        print('La matriz esta vacia. Llenar antes de llevar a cabo esta operacion.')
    else:
        columnIndex = int(input("Inserte la posicion de la columna a analizar: "))
        count = countNumbers(matrix, columnIndex)
        print('Cantidad de numeros divisibles y mayores que 3 en la columna: ' + str(count))
    pass


def countNumbers(matrix, index):
    count = 0
    for i in range(0, len(matrix)):
        # chequear si tiene ese indice de columna
        if index in range(0, len(matrix[i])):
            # chequear la condicion de que sea divisible y mayor que 3
            if matrix[i][index] % 3 == 0 and matrix[i][index] > 3:
                count += 1
    return count
