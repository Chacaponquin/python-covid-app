from rich import print as rprint
def rowSort(matrix):

    if len(matrix) > 0:

        complete = False
        while not complete:

            rowIndex = input(f'Inserte el índice de la fila a ordenar (de 0 a {len(matrix)-1}): ')

            if rowIndex.isnumeric() and 0 <= int(rowIndex) < len(matrix):
                sortedRow = sortRowGreaterToLower(matrix, int(rowIndex))
                rprint(f'La fila ordenada de mayor a menor es: [blue]{sortedRow}')
                complete = True

            else:
                rprint(f'[bold red]{rowIndex} no es un número de 0 a {len(matrix)-1}.')

    else:
        rprint('[bold red]La matriz está vacía. Debe rellenarla antes de ejecutar este inciso.')

def sortRowGreaterToLower(matrix, index):
    return sorted(matrix[index], key=None, reverse=True)

