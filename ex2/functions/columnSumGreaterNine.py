from rich import print as rprint
def columnSumGreaterNine(matrix):
    if len(matrix) == 0:
        rprint('La matriz esta vacia. Llenar antes de llevar a cabo esta operacion.')
    else:
        for i in range(len(matrix[0])):
            columnSum = 0
            for j in range(len(matrix)):
                columnSum += matrix[j][i]
            rprint('Suma de la columna '+str(i)+': '+str(columnSum), end = ' ')
            if columnSum > 9:
                rprint('> 9')
            elif columnSum < 9:
                print(' < 9')
