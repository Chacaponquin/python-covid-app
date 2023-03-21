from ex1.functions import readRegisters, showBarGrafic, communeWithOmicron, variantPorcentByCommune, totalVaccinated
from rich import print as rprint


class Ex1:
    def __init__(self):
        # crear registros
        self.registros = readRegisters()

        self.printInitMessage()

    def printInitMessage(self):
        flag = False
        while not flag:
            inciso = input('\n>>> Inserte un inciso entre: a, b, c, d, o escribe atras para ir al menú principal: ')

            if inciso == 'a':
                self.incisoA()
            elif inciso == 'b':
                self.incisoB()
            elif inciso == 'c':
                self.incisoC()
            elif inciso == 'd':
                self.incisoD()
            elif inciso == 'atras':
                flag = True
            else:
                rprint('[bold red]No existe esta opción')

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


