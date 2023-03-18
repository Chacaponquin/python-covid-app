from ex1.functions import readRegisters, showBarGrafic, communeWithOmicron, variantPorcentByCommune, totalVaccinated


class Ex1:
    def __init__(self):
        # crear registros
        registros = readRegisters()
        showBarGrafic(registros)
        communeWithOmicron(registros)
        totalVaccinated(registros)
        variantPorcentByCommune(registros, "Antofagasta")



