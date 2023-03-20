from rich import print as rprint
def rowSort(matrix):
    if len(matrix) == 0:
        rprint('La matriz esta vacia. Llenar antes de llevar a cabo esta operacion')
    else:
        rowIndex = int(input('Inserte el indice de la fila a ordenar: '))

        while rowIndex < 0 or rowIndex > len(matrix)-1:
            rprint('El indice no puede ser menor que cero o mayor que ' + str(len(matrix) - 1))
            rowIndex = int(input('Inserte el indice de la fila a ordenar: '))

        rprint('La fila ordenada de mayor a menor es: ' + str(sortRowGreaterToLower(matrix, rowIndex)))


def sortRowGreaterToLower(matrix, index):
    return sorted(matrix[index], key=None, reverse=True)

