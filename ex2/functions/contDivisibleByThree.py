from rich import print as rprint

def contDivisibleByThree(matrix):

    if len(matrix) > 0:

        complete = False
        while not complete:

            columnIndex = input(f'Inserte el índice de la columna a analizar (de 0 a {len(matrix[0])-1}): ')

            if columnIndex.isnumeric() and 0 <= int(columnIndex) < len(matrix[0]):

                count = countNumbers(matrix, int(columnIndex))
                rprint(f'La cantidad de números divisibles y mayores que 3 en la columna es: [blue]{count}')
                complete = True

            else:
                rprint(f'[bold red]{columnIndex} no es un número de 0 a {len(matrix[0]) - 1}.')

    else:
        rprint('[bold red]La matriz está vacía. Debe rellenarla antes de ejecutar este inciso.')

def countNumbers(matrix, index):
    count = 0
    for i in range(0, len(matrix)):
        # chequear si tiene ese índice de columna
        if index in range(0, len(matrix[i])):
            # chequear la condición de que sea divisible por 3 y mayor que 3
            if matrix[i][index] % 3 == 0 and matrix[i][index] > 3:
                count += 1
    return count
