from Menu import Menu
import os



class Sentencias(Menu):

    def __init__(self):
        pass

    def menuSentencias(self):
        opcion = self.menu(["1. Ingreso de Datos", "2. If, Elif, Else", "3. Funciones", "4. Operadores Lógicos", "5. Operador Ternario", "6. If, In", "0. Salir"], "*" * 16 + " MENU DE SENTENCIAS " + "*" * 16)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Ingreso de Datos " + "*" * 15 + "\n")

            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            sueldo = float(input("Ingrese su sueldo: "))

            print("Hola, " + nombre)
            edadFutura = edad + 20
            print("Tu edad es:", edad)
            print("Tu edad (dentro de 20 años) será:", edadFutura)
            print("Tu sueldo es:", sueldo)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSentencias()

        elif opcion == '2':
            print("*" * 15 + " If, Elif, Else " + "*" * 15 + "\n")

            edad = int(input("Ingrese su edad: "))

            # if edad >= 18:
            #     print("Eres mayor de edad.")
            if edad > 18:
                print("Eres mayor de edad.")
            elif edad == 18:
                print("Tienes 18 años")
            else:
                print("No eres mayor de edad.")

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSentencias()

        elif opcion == '3':
            print("*" * 15 + " Funciones " + "*" * 15 + "\n")

            def saludar():
                print("Arroba")
                print("Anderson")
                print("Steven")
                return "Hola"

            print(saludar())

            def evaluarSueldoMinimo(sueldo):
                if sueldo >= 850:
                    print("Cumples con el sueldo")
                else:
                    print("Ganas menos que el sueldo mínimo")

            evaluarSueldoMinimo(100)
            evaluarSueldoMinimo(900)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSentencias()

        elif opcion == '4':
            print("*" * 15 + " Operadores Lógicos " + "*" * 15 + "\n")

            distancia = 400
            numeroHermanos = 3
            salarioPadres = 3000

            tieneBeneficio = False

            if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
                tieneBeneficio = True

            print(not tieneBeneficio)

            # if (5 > 3) and (8 < 6):
            if (5 > 3) or (8 < 6):
                print("Verdad")
            else:
                print("Es mentira...")

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSentencias()

        elif opcion == '5':
            print("*" * 15 + " Operador Ternario " + "*" * 15 + "\n")

            """
            String sexo;
            sexo = (10 > 20) ? "Masculino" : "Femenino";
            """

            sexos = ("Hombre", "Mujer")

            posicion = True
            # sexo = sexos[1]
            sexo = sexos[posicion]  # Mujer
            print(sexo)
            # sexo = sexos[0]
            sexo = sexos[not posicion]  # Hombre
            print(sexo)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSentencias()

        elif opcion == '6':
            print("*" * 15 + " If, In " + "*" * 15 + "\n")

            print("-- Cursos --")
            print("Python - Bootstrap - HTML - Django")

            curso = input("Ingrese el curso deseado: ")

            if curso in ("Python", "Bootstrap", "HTML", "Django"):
                print("Curso de {0} seleccionado.".format(curso))
            else:
                print("No existe ese curso...")

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSentencias()

        elif opcion == '0':
            pass

#opc = Sentencias()
#opc.menuSentencias()