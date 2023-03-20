from ex1.functions import readRegisters, showBarGrafic, communeWithOmicron, variantPorcentByCommune, totalVaccinated
from rich import print as rprint


class Ex1:
    def __init__(self):
        # crear registros
        self.registros = readRegisters()

        self.printInitMessage()

    def incisoA(self):
        showBarGrafic(self.registros)

    def incisoB(self):
        communeWithOmicron(self.registros)

    def incisoC(self):
        comuna = input(
            ">>> Inserte una comuna para saber la distribución de sus variantes: ")
        variantPorcentByCommune(self.registros, comuna)

    def incisoD(self):
        totalVaccinated(self.registros)

    def printInitMessage(self):
        while True:
            inciso = input('\n>>> Eliga un inciso entre: a, b, c, d: ')

            if inciso == 'a':
                self.incisoA()
            elif inciso == 'b':
                self.incisoB()
            elif inciso == 'c':
                self.incisoC()
            elif inciso == 'd':
                self.incisoD()
            else:
                rprint('[bold red]No existe ese inciso')
