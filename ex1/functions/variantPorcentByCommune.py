import matplotlib.pyplot as plt
from rich import print as rprint
from rich.tree import Tree
from rich.table import Table

def variantPorcentByCommune(casos, comuna):
    # Arreglo de variantes
    variantes = []
    # Arreglo para la cantidad de casos por variante
    numero_casos = []
    # Arreglo para los diferentes tipos de variantes
    tipo_variante = ["omicron", "delta", "alfa", "beta"]

    # Buscar en la comuna la cantidad de casos por variantes
    for registro in casos:
        # Verificar si la comuna del registro coincide con la comuna buscada
        if registro.comuna == comuna:
            # Verificar si la variante ha sido añadida con anterioridad al arreglo de variantes
            # En caso de ser cierto se incrementa en uno la cantidad de casos en la posicion del
            # arreglo de numero casos correspondiente
            # En caso de no ser cierto se añade al arreglo de variantes y se inicializa en 1
            # la cantidad de casos correspondientes en el otro arreglo
            if registro.tipoVariante in variantes:
                numero_casos[variantes.index(registro.tipoVariante)] = \
                    numero_casos[variantes.index(registro.tipoVariante)] + 1
            else:
                variantes.append(registro.tipoVariante)
                numero_casos.append(1)

    # Verificar si existen variantes, en caso de existir, construir gráfico de pastel
    if len(variantes) > 0:
        plt.pie(numero_casos, labels=variantes, autopct="%0.2f %%")
        plt.title(f"Distribución de variantes en {comuna}")
        plt.axis("equal")
        plt.show()

        #Para mostrar por consola el resultado
        total = sum(numero_casos)
        for v in tipo_variante:
            if v not in variantes:
                variantes.append(v)
                numero_casos.append(0)

        table = Table()
        table.add_column("Variante", justify="left",
                         style="cyan", no_wrap=True)
        table.add_column("Porcentaje", style="magenta", no_wrap=True)
        for i in range(0, 4):
            table.add_row(variantes[i], str(numero_casos[i]/total*100)[:5])

        rprint(table)
    else:
        rprint("[bold red]La comuna no exite o no presenta casos")
