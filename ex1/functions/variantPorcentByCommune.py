import matplotlib.pyplot as plt
from rich import print as rprint


def variantPorcentByCommune(casos, comuna):
    # Arreglo de variantes
    variantes = []
    # Arreglo para la cantidad de casos por variante
    numero_casos = []

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
        plt.axis("equal")
        plt.show()
    else:
        rprint("[bold red]La comuna no exite o no presenta casos")
