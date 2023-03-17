from ex1.functions import readRegisters, showBarGrafic, communeWithOmicron, variantPorcentByCommune, totalVaccinated


class Ex1:
    def __init__(self):
        # leer registros
        self.registros = readRegisters()

        self.printInitMessage()

    def incisoA(self):
        showBarGrafic(self.registros)

    def incisoB(self):
        communeWithOmicron(self.registros)

    def incisoC(self):
        variantPorcentByCommune(self.registros)

    def incisoD(self):
        totalVaccinated(self.registros)

    def printInitMessage(self):
        while(True):
            inciso = input('Eliga un inciso entre: a, b, c, d: ')

            if inciso == 'a':
                self.incisoA()
            elif inciso == 'b':
                self.incisoB()
            elif inciso == 'c':
                self.incisoC()
            elif inciso == 'd':
                self.incisoD()
            else:
                print('ERROR')






