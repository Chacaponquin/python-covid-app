def fillMatrix(matrix):
    cloneMatrix = matrix
    number = input('Con qué número desea llenar la matriz?: ')

    for i in range(len(cloneMatrix)):
        for j in range(len(cloneMatrix[i])):
            print(i, j)
            cloneMatrix[i][j] = int(number)

    pass
