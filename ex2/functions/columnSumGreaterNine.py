from rich import print as rprint
def columnSumGreaterNine(matrix):

    if len(matrix) > 0:

        for i in range(len(matrix[0])):
            columnSum = 0

            for j in range(len(matrix)):
                columnSum += matrix[j][i]

            rprint(f'- Suma de la columna de índice {i}: {columnSum}', end=' ')
            if columnSum > 9:
                rprint('[blue]> 9')
            elif columnSum < 9:
                rprint('[blue]< 9')

    else:
        rprint('[bold red]La matriz está vacía. Debe rellenarla antes de ejecutar este inciso.')

