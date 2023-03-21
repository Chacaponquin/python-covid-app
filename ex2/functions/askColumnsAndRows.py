from rich import print as rprint

def askColumnsAndRows():
    rows = input('>>> Inserte la cantidad de filas de la matriz: ')

    if(rows.isnumeric() and int(rows) > 0):
        columns = input('>>> Inserte la cantidad de columnas de la matriz: ')

        if(columns.isnumeric() and int(columns) > 0):
            matrix = []

            for i in range(int(columns)):
                newColumn = []

                for j in range(int(rows)):
                    newColumn.append(0)

                matrix.append(newColumn)

            return matrix
        else:
            rprint('[bold red]El número de columnas debe ser mayor que 0')
    else:
        rprint('[bold red]El número de filas debe ser mayor que 0')





