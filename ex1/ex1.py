from ex1.functions.readRegisters import readRegisters

from ex1.functions.communeBars import showBarGrafic


def Ex1():
    # crear registros
    registros = readRegisters()

    showBarGrafic(registros)
