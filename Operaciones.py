from Menu import Menu
import os



class Operaciones(Menu):

    def __init__(self):
        pass

    def menuOperaciones(self):
        opcion = self.menu(["1. Presentar Mensaje", "2. Variables", "3. Conversiones", "4. Números y Operaciones", "5. Concatenaciones", "0. Salir"], "*" * 15 + " MENU DE OPERACIONES " + "*" * 16)
        os.system("cls")

        if opcion == '1':
            print("*" *15 + " Presenta un mensaje " + "*"*15 + "\n")
            print("Hola Mundo")

            #Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuOperaciones()

        elif opcion == '2':
            print("*" * 15 + " Variables " + "*" * 15 + "\n")

            nombre = "Anderson Arroba"
            print(nombre)

            edad = 22
            print(edad)

            edad = True
            print(edad)

            sueldo = 350.75
            print(sueldo)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuOperaciones()

        elif opcion == '3':
            print("*" * 15 + " Conversiones " + "*" * 15 + "\n")

            numero1 = "35"
            numero2 = "18"
            print(numero1 + numero2)

            num1 = int(numero1)
            num2 = int(numero2)
            print(num1 + num2)

            sueldo = 1200.43
            sueldoEntero = int(sueldo)
            print(sueldoEntero)

            valor = "4500.89"
            valorDecimal = float(valor)
            print(valorDecimal * 3)

            edad = 100
            print(len(str(edad)))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuOperaciones()

        elif opcion == '4':
            print("*" * 15 + " Números y Operaciones " + "*" * 15 + "\n")

            entero = 23
            decimal = 31.78
            complejo = 12 + 5j
            # booleano = True

            """
            print(entero)
            print(decimal)
            print(complejo)
            print(booleano)
            """

            num1 = 20
            num2 = 4

            print("Suma:", (num1 + num2))
            print("Resta:", (num1 - num2))
            print("Multiplicación:", (num1 * num2))
            print("División:", (num1 / num2))
            print("División Exacta:", (num1 // num2))
            print("Potencia:", (num1 ** num2))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuOperaciones()

        elif opcion == '5':
            print("*" * 15 + " Concatenaciones " + "*" * 15 + "\n")

            texto1 = "Hola"
            texto2 = "Mundo"
            textoFinal = texto1 + " " + texto2
            print(textoFinal)

            print("El saludo es: %s %s" % (texto1, texto2))

            saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
            print(saludoFinal)

            # saludoFinal = "Saludo: {} {}".format(texto1, texto2)
            # print(saludoFinal)

            saludoFinal2 = "Saludo: {y} {x}".format(x=texto2, y=texto1)
            print(saludoFinal2)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuOperaciones()

        elif opcion == '0':
            pass


#opc = Operaciones()
#opc.menuOperaciones()