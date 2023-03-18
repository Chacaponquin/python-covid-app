from ex1.ex1 import Ex1
from ex2.ex2 import Ex2

class Main:
    def __int__(self):
        while(True):
            ex = input('Qué ejercicio quiere ejecutar?: ')

            if ex == '1':
                Ex1()
            elif ex == '2':
                Ex2()
            else:
                print('ERROR')

Main().__int__()

