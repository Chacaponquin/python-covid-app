import matplotlib.pyplot as plt


def communeBars(casosEstudiar):
    # Arreglo de comunas
    comunas = []
    # Arreglo de cantidad de casos por comunas
    contComunas = []

    # buenas
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
    comunas, caseComunas = communeBars(casos)

    # figsize es una tupla de dos elementos donde el primero indica el ancho y el segundo la altura
    f, ax = plt.subplots(figsize=(20, 6))
    # crear todas las barras del grafico
    plt.bar(comunas, caseComunas, label='Casos')
    plt.title('Cantidad de casos por comuna')

    plt.rcParams["figure.autolayout"] = True

    # hacer que la ventana ocupe toda la pantalla
    # manager = plt.get_current_fig_manager()
    # manager.full_screen_toggle()

    # configuracion del tamaño de la fuente
    ax.legend(fontsize=14)

    plt.show()
