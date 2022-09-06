from Menu import Menu
import os



class Generadores(Menu):

    def __init__(self):
        pass

    def menuGeneradores(self):
        opcion = self.menu(["1. Generador", "2. Generador Nº2", "0. Salir"], "*" * 16 + " MENU DE GENERADORES " + "*" * 15)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Generador " + "*" * 15 + "\n")

            """
            def generaMultiplos7(limite):
                numero = 1
                listaNumeros = []
                while numero <= limite:
                    listaNumeros.append(numero * 7)
                    numero = numero + 1
                return listaNumeros  # Retorna toda la lista creada.
            print(generaMultiplos7(10))
            """

            def generadorMultiplos7(limite):
                numero = 1

                while numero <= limite:
                    yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
                    numero = numero + 1

            obtieneMultiplos7 = generadorMultiplos7(10)

            """
            # print(obtieneMultiplos7)
            for n in obtieneMultiplos7:
                print(n)
            """

            # next(): Retorna el siguiente elemento de un objeto iterable:

            print(next(obtieneMultiplos7))
            print("Acá hay 300 líneas de código...")
            print(next(obtieneMultiplos7))
            print("Acá hay 1000 líneas de código...")
            print(next(obtieneMultiplos7))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuGeneradores()

        if opcion == '2':
            print("*" * 15 + " Generador Nº2 " + "*" * 15 + "\n")

            """
            def devuelveLenguajes(*lenguajes):
                for leng in lenguajes:
                    yield leng
            """

            def devuelveLenguajes(*lenguajes):
                for leng in lenguajes:
                    yield from leng

            lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

            print(next(lenguajesObtenidos))
            print(next(lenguajesObtenidos))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuGeneradores()

        elif opcion == '0':
            pass

#opc = Generadores()
#opc.menuGeneradores()