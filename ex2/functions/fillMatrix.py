from rich import print as rprint
from rich.table import Table

def fillMatrix(matrix):
    cloneMatrix = matrix

    rprint('\n[yellow bold]Advertencia: Inserte los números que desee separados por coma. En caso de escribir menos números que el tamaño de la fila el resto serán rellenados con 0\n')

    for fila in range(len(matrix)):
        numbers = input(f'>>> Inserte los números de la fila {fila}: ')

        # separar los números por comas
        # utilizar 'strip()' para eliminar los espacios en blanco alrededor del número
        separatedNumbers = [num.strip() for num in numbers.split(',') if num.strip() != '']

        if len(separatedNumbers) > 0:
            # recorrer cada uno de los números insertados
            for numIndex in range(len(separatedNumbers)):
                # verificar que es un número
                if not separatedNumbers[numIndex].isnumeric():
                    rprint(f'[bold red] {separatedNumbers[numIndex]} no es un número')
                # verificar que el número se puede insertar mientras que no supere el tamaño de la fila
                elif numIndex < len(cloneMatrix[fila]):
                    cloneMatrix[fila][numIndex] = float(separatedNumbers[numIndex])

    # imprimir matriz en consola
    table = Table()

    # añadir columnas
    table.add_column('')
    for column in range(len(cloneMatrix[0])):
        table.add_column(f'Columna {column + 1}')

    for rowIndex in range(len(cloneMatrix)):
        # añadir filas
        stringNums = [str(num) for num in cloneMatrix[rowIndex]]
        table.add_row(f'Fila {rowIndex + 1}', *stringNums)

    rprint('\n', table)








