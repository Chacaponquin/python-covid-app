import matplotlib.pyplot as plt


def contCaseByCommune(casosEstudiar):
    # Arreglo de comunas
    comunas = []
    # Arreglo de cantidad de casos por comunas
    contComunas = []

    # Buscar la cantidad de casos que tiene cada comuna
    for registro in casosEstudiar:
        # Verificar que no se han contado los casos de esa comuna, para evitar repeticiones
        if registro.comuna not in comunas:
            cantCasos = 0

            for registroCheck in casosEstudiar:
                if registroCheck.comuna == registro.comuna:
                    cantCasos += 1

            # Añadir la comuna y la cantidad de casos a los arreglos
            comunas.append(registro.comuna)
            contComunas.append(cantCasos)

    return comunas, contComunas


def showBarGrafic(casos):
    comunas, caseComunas = contCaseByCommune(casos)

    # figsize es una tupla de dos elementos donde el primero indica el ancho y el segundo la altura
    f, ax = plt.subplots(figsize=(18, 6))
    # crear todas las barras del grafico
    plt.bar(comunas, caseComunas, label='Casos')
    plt.title('Cantidad de casos por comuna')
    # configuracion del tamaño de la fuente
    ax.legend(fontsize=14)

    plt.show()
