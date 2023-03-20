def rowSort(matrix):
    if len(matrix) == 0:
        print('La matriz esta vacia. Llenar antes de llevar a cabo esta operacion')
    else:
        rowIndex = int(input('Inserte el indice de la fila a ordenar: '))

        while (not rowIndex in range(0, len(matrix))):
            print('INDICE INVALIDO! No puede ser menor que cero o mayor que ' + str(len(matrix) - 1))
            rowIndex = int(input('Inserte el indice de la fila a ordenar: '))

        print('La fila ordenada de mayor a menor es: ' + str(sortRowGreaterToLower(matrix, rowIndex)))


def sortRowGreaterToLower(matrix, index):
    return sorted(matrix[index], key=None, reverse=True)

