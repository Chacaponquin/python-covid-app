def askColumnsAndRows():
    rows = input('Inserte la cantidad de filas de la matriz: ')
    columns = input('Inserte la cantidad de columnas de la matriz: ')

    matrix = []

    for i in range(int(columns)):
        newColumn = []

        for i in range(int(rows)):
            newColumn.append(0)

        matrix.append(newColumn)

    return matrix
