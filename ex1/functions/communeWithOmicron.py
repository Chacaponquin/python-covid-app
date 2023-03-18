def communeWithOmicron(casos):
    # Arreglo de comunas
    comunas = []

    #Buscar la cantidad de comunas con omicron
    for registro in casos:
        # Verificar que no se ha añadido la comuna previamente
        if registro.comuna not in comunas:
            # Si la variante en la comuna es omicron se añade al arreglo de comunas
            if registro.tipoVariante == 'omicron':
                comunas.append(registro.comuna)
    print("Las comunas con casos de la variante omicron son:")
    print(*comunas, sep=",")


