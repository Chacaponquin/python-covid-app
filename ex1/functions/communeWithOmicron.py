from rich import print as rprint
from rich.tree import Tree


def communeWithOmicron(casos):
    # Diccionario de comunas
    comunas = {}

    # crear una lista con los nombres de comunas
    for reg in casos:
        if reg.comuna not in comunas.keys():
            comunas[reg.comuna] = {'omicron': 0, 'alfa': 0, 'delta': 0, 'beta': 0}

    # Buscar la cantidad de comunas con omicron
    for com in comunas.keys():
        for reg in casos:
            if reg.comuna == com:
                comunas[com][reg.tipoVariante] += 1

    returnComuna = []
    for comuna in comunas.keys():
        predOmicron = True

        # valores de cada variante en esa comuna
        values = comunas[comuna].values()

        for val in range(1, len(values)):
            if list(values)[val] >= comunas[comuna]['omicron']:
                predOmicron = False

        if predOmicron == True:
            returnComuna.append(comuna)

    tree = Tree('Las comunas con casos de la variante omicron son:', style='green')
    for com in returnComuna:
        tree.add(com, style='blue')
    rprint(tree)
