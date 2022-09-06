from Menu import Menu
import os



class Excepciones(Menu):

    def __init__(self):
        pass

    def menuExcepciones(self):
        opcion = self.menu(["1. Excepciones", "2. Raise", "0. Salir"], "*" * 16 + " MENU DE EXCEPCIONES " + "*" * 16)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Excepciones " + "*" * 15 + "\n")

            numero1 = 20
            # numero2 = 0
            numero2 = 2

            # print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

            try:
                resultado = numero1 / numero2
            # except:
            except ZeroDivisionError:
                print("No se puede dividir entre 0...")
            finally:
                print("Yo siempre aparezco.")

            print("Aquí termina mi programa.")

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuExcepciones()

        elif opcion == '2':
            print("*" * 15 + " Raise " + "*" * 15 + "\n")

            def evaluarNota(nota):
                if nota < 0:
                    raise ValueError("Valor incorrecto...")
                    # raise ZeroDivisionError("Este mensaje es personalizado.")
                elif nota >= 16:
                    print("Excelente")
                elif nota >= 11:
                    print("Aprobado")
                else:
                    print("Desaprobado")

            #evaluarNota(-7)
            evaluarNota(12)

            print("Este es el fin de mi programa.")

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuExcepciones()

        elif opcion == '0':
            pass

#opc = Excepciones()
#opc.menuExcepciones()