from ex2.functions import rowSort, contDivisibleByThree, columnSumGreaterNine, askColumnsAndRows, fillMatrix
from rich import print as rprint


class Ex2:
    def __int__(self):
        self.matrix = askColumnsAndRows()
        self.printInitMessage()

    def printInitMessage(self):
        while True:
            inciso = input('\n>>> Inserte un inciso entre a, b, c, d: ')

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

    def incisoA(self):
        fillMatrix(self.matrix)

    def incisoB(self):
        contDivisibleByThree(self.matrix)

    def incisoC(self):
        columnSumGreaterNine(self.matrix)

    def incisoD(self):
        rowSort(self.matrix)
