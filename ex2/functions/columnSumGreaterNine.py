def columnSumGreaterNine(matrix):

    if len(matrix) == 0:
        print('La matriz esta vacia. Llenar antes de llevar a cabo esta operacion.')
    else:
        for i in range(len(matrix[0])):
            columnSum = 0
            for j in range(len(matrix)):
                columnSum += matrix[j][i]
            print('Suma de la columna '+str(i)+': '+str(columnSum), end = '')
            if columnSum > 9:
                print('> 9')
            elif columnSum < 9:
                print(' < 9')
    pass