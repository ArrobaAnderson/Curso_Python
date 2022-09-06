from Menu import Menu
import os



class Paquetes(Menu):

    def __init__(self):
        pass

    def menuPaquetes(self):
        opcion = self.menu(["1. Paquete", "0. Salir"], "*" * 17 + " MENU DE PAQUETES " + "*" * 17)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Paquete " + "*" * 15 + "\n")

            #Funciones de Cadenas
            def contar_letras(texto):
                return len(texto)

            #Funciones Numéricas
            def multiplicar(n1, n2):
                return n1 * n2

            def potenciar(base, exponente):
                return base ** exponente


            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPaquetes()

        elif opcion == '0':
            pass

#opc = Paquetes()
#opc.menuPaquetes()