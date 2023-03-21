from rich import print as rprint

def fillMatrix(matrix):
    cloneMatrix = matrix
    number = input('>>> Con qué número desea llenar la matriz?: ')

    if(number.isnumeric()):
        number = int(number)
        for i in range(len(cloneMatrix)):
            for j in range(len(cloneMatrix[i])):
                cloneMatrix[i][j] = number
    else:
        rprint('[bold red]Debe insertar un número')



