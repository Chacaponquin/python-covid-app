from rich import print as rprint

def contDivisibleByThree(matrix):
    if len(matrix) == 0:
        rprint('La matriz esta vacía. Llenar antes de llevar a cabo esta operación.')
    else:
        columnIndex = int(input("Inserte la posición de la columna a analizar: "))

        while columnIndex < 0 or columnIndex > len(matrix[0])-1:
            rprint('El indice no debe ser menor que cero o mayor que '+str(len(matrix[0])-1))
            columnIndex = int(input("Inserte la posición de la columna a analizar: "))

        count = countNumbers(matrix, columnIndex)
        rprint('Cantidad de números divisibles y mayores que 3 en la columna: ' + str(count))



def countNumbers(matrix, index):
    count = 0
    for i in range(0, len(matrix)):
        # chequear si tiene ese indice de columna
        if index in range(0, len(matrix[i])):
            # chequear la condicion de que sea divisible y mayor que 3
            if matrix[i][index] % 3 == 0 and matrix[i][index] > 3:
                count += 1
    return count
