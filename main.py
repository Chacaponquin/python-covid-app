from rich import print as rprint
from rich.table import Table

from ex1.ex1 import Ex1
from ex2.ex2 import Ex2

class Main:
    def __int__(self):
        flag = False
        while not flag:
            ex = input("\n>>> Qué ejercicio desea ejecutar?, o escribe cerrar para parar el programa: ").strip()

            if ex == '1':
                self.printEx1Message()
                Ex1().start()
            elif ex == '2':
                self.printEx2Message()
                Ex2().start()
            elif ex == 'cerrar':
                flag = True
            else:
                rprint('[bold red]Debe seleccionar uno de los dos ejercicios')

    def printEx2Message(self):
        table = Table()

        table.add_column("Inciso", justify="left",
                         style="cyan", no_wrap=True)
        table.add_column("Contenido", style="magenta", no_wrap=True)

        table.add_row(
            'Inciso A', 'Llenar la matriz con un número')
        table.add_row(
            'Inciso B', 'Obtener la cantidad de valores divisibles y mayores que 3 en una columna')
        table.add_row(
            'Inciso C', 'Obtiene la suma de cada columna de la matriz e indica si es mayor que 9')
        table.add_row(
            'Inciso D', 'Devuelve una fila ordenada de mayor a menor')

        rprint(table)

    def printEx1Message(self):
        table = Table()

        table.add_column("Inciso", justify="left",
                         style="cyan", no_wrap=True)
        table.add_column("Contenido", style="magenta")

        table.add_row(
            'Inciso A', 'Gráfico de barras de la cantidad de casos por comuna.')
        table.add_row(
            'Inciso B', 'Comunas en las que predomina la variante omicron.')
        table.add_row(
            'Inciso C', 'Porcentaje por variantes de una comuna')
        table.add_row(
            'Inciso D', 'Total de personas vacunadas')

        rprint(table)


Main().__int__()
