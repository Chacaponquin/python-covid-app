from ex1.functions import readRegisters, communeBars, communeWithOmicron, variantPorcentByCommune, totalVaccinated


class Ex1:
    def __init__(self):
        # crear registros
        registros = readRegisters()
        communeBars(registros)


