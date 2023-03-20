from rich import print as rprint
def totalVaccinated(casos):
    # Variable para almacenar el total de personas vacunadas
    vacunados = 0
    #Buscar la cantidad de personas vacunadas
    for registro in casos:
        if registro.estaVacunado is True:
            vacunados= vacunados + 1


    rprint(f'El total de vacunados es: [blue]{vacunados}')

