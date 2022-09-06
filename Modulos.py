from Menu import Menu
import os



class Modulos(Menu):

    def __init__(self):
        pass

    def menuModulos(self):
        opcion = self.menu(["1. Modulos", "0. Salir"], "*" * 18 + " MENU DE MODULOS " + "*" * 17)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Modulos " + "*" * 15 + "\n")

            #Funciones Matemáticas
            def sumar(n1, n2):
                return n1 + n2

            def multiplicar(n1, n2):
                return n1 * n2

            #Modulos
            #from Curso.Modulos.Funciones_Matematicas import *
            print(sumar(5, 6))
            print(multiplicar(5, 6))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuModulos()

        elif opcion == '0':
            pass

#opc = Modulos()
#opc.menuModulos()