from Menu import Menu
import os



class Bucles(Menu):

    def __init__(self):
        pass

    def menuBucles(self):
        opcion = self.menu(["1. Range", "2. For", "3. Factorial", "4. While", "5. Break, Continue, Pass", "0. Salir"], "*" * 18 + " MENU DE BUCLES " + "*" * 18)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Range " + "*" * 15 + "\n")

            numeros = range(5)  # [0, 1, 2, 3, 4]

            print(numeros[1])

            numeros1 = range(4, 10)  # [4, 5, 6, 7, 8, 9]
            print(numeros1[5])

            numeros2 = range(10, 100, 8)
            print(numeros2[9])  # [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuBucles()

        elif opcion == '2':
            print("*" * 15 + " For " + "*" * 15 + "\n")

            """
            for num in range(0, 20, 2):
                print("Valor actual: {0}".format(num))
            """

            for i in range(1, 13):
                print("{0} x {1} es: {2}".format(i, i, (i * i)))

            for nom in ["Valeria", "Jose", "Hugo", "Andrés"]:
                print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuBucles()

        elif opcion == '3':
            print("*" * 15 + " Factorial " + "*" * 15 + "\n")

            # Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
            # Factorial de 4: 1 * 2 * 3 * 4 = 24

            numero = int(input("Ingrese un número: "))

            factorial = 1
            for n in range(1, (numero + 1)):
                factorial = factorial * n

            print("El factorial de {0} es: {1}".format(numero, factorial))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuBucles()

        elif opcion == '4':
            print("*" * 15 + " While " + "*" * 15 + "\n")

            """
            indice = 1
            while indice < 10:
                print("Valor actual: {0}".format(indice))
                indice = indice + 1
            print("Hemos terminado el bucle while.")
            # Continua el programa.
            """

            inicio = 2

            while inicio <= 100:
                print("Número par: {0}".format(inicio))
                inicio += 2

            print("Hemos terminado el bucle while.")

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuBucles()

        elif opcion == '5':
            print("*" * 15 + " Break, continue, Pass " + "*" * 15 + "\n")

            # Break
            """
            for numero in range(1, 6):
                if numero == 3:
                    break  # Descanso o interrupción en este punto.
                print("El número es: {0}".format(numero))
            print("Bucle terminado.")
            """

            # Continue

            """
            for numero in range(1, 6):
                if numero == 3:
                    continue  # Continúa con el resto del bucle.
                print("El número es: {0}".format(numero))
            print("Bucle terminado.")
            """

            # Pass
            for numero in range(1, 6):
                if numero <= 3:
                    # Aquí no pasa nada y el bucle sigue trabajando.
                    pass
                else:
                    print("El siguiente valor es mayor a 3:")
                print("El número es: {0}".format(numero))

            print("Bucle terminado.")

            """
            def funcionSinImplementar():
                pass
            """

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuBucles()

        elif opcion == '0':
            pass

#opc = Bucles()
#opc.menuBucles()