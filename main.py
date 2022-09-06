from Menu import Menu
from Operaciones import *
from Secuencias import *
from Sentencias import *
from Bucles import *
from Generadores import *
from Excepciones import *
from Modulos import *
from Paquetes import *
from POO import *
import os



class Main(Menu):

    def __init__(self):
        pass

    def menuMain(self):
        opcion = self.menu(["1. Operaciones", "2. Secuencias", "3. Sentencias", "4. Bucles", "5. Generadores", "6. Excepciones", "7. Módulos", "8. Paquetes", "9. POO", "0. Salir"], "*" * 18 + " MENU PRINCIPAL " + "*" * 18)
        os.system("cls")

        if opcion == '1':
            operacione = Operaciones()
            if operacione.menuOperaciones() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '2':
            secuencia = Secuencias()
            if secuencia.menuSecuencias() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '3':
            sentencia = Sentencias()
            if sentencia.menuSentencias() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '4':
            bucle = Bucles()
            if bucle.menuBucles() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '5':
            generador = Generadores()
            if generador.menuGeneradores() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '6':
            excepcion = Excepciones()
            if excepcion.menuExcepciones() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '7':
            modulo = Modulos()
            if modulo.menuModulos() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '8':
            paquete = Paquetes()
            if paquete.menuPaquetes() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '9':
            poo = POO()
            if poo.menuPOO() != '0':
                os.system("cls"), self.menuMain()

        elif opcion == '0':
            os.system("cls")
            print("\n" + "*" * 30)
            print("* Gracias por usar este menu *")
            print("*" * 30 + "\n")




opc = Main()
opc.menuMain()