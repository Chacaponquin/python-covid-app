from functions import readRegisters, communeBars, communeWithOmicron, variantPorcentByCommune, totalVaccinated


class Ex1:
    # crear registros
    registros = readRegisters()

    communeBars(registros)
