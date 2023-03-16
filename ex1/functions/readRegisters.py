class Registro:
    def __init__(self, rut, comuna, tipoVariante, estaVacunado):
        self.rut = rut
        self.comuna = comuna
        self.tipoVariante = tipoVariante
        self.estaVacunado = estaVacunado


def createRegisters(registros) -> list[Registro]:
    # Arreglo con los casos
    casosEstudiar = []

    for registro in registros:
        # El ultimo registro siempre es una cadena vacia
        if(registro != ''):
            separatedValues = registro.split(',')

            rut = separatedValues[0]
            comuna = separatedValues[1]
            tipoVariante = separatedValues[2]
            estaVacunado = separatedValues[3] == 'si'

            # crear y guardar registro
            # en python no es necesario utilizar el 'new' para instanciar una clase
            newRegistro = Registro(rut, comuna, tipoVariante, estaVacunado)
            casosEstudiar.append(newRegistro)

    return casosEstudiar


def readRegisters() -> list[Registro]:
    # Abrir el archivo
    f = open('casosCovid.txt', 'r', encoding='utf8')

    # Separar los registros por los saltos de linea
    registros = f.read().split('\n')

    return createRegisters(registros)
