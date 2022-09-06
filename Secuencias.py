from Menu import Menu
import os



class Secuencias(Menu):

    def __init__(self):
        pass

    def menuSecuencias(self):
        opcion = self.menu(["1. Cadenas", "2. Tuplas", "3. Listas", "4. Diccionarios", "0. Salir"], "*" * 16 + " MENU DE SECUENCIAS " + "*" * 16)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Cadenas " + "*" * 15 + "\n")

            texto = "biEnvenIdoS al cUrso de Pyhon"

            print(texto)
            print(texto.lower())
            print(texto.upper())
            print(texto.title())  # Convierte una cadena a un formato de título.
            print(texto.find("al"))  # Posición donde encuentra la cadena o porción.
            print(texto.count("e"))  # Cantidad de ocurrencias de una letra o porción.

            textoFinal = texto.replace("e", "3")
            print(textoFinal)

            valor = texto.isnumeric()  # Arroja true o false dependiendo si es un número.
            print(valor)

            cadenaSeparada = texto.split(" ")
            print(cadenaSeparada)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSecuencias()

        elif opcion == '2':
            print("*" * 15 + " Tuplas " + "*" * 15 + "\n")

            tupla = (1, 2, 3)
            print(tupla)
            tupla2 = (7, "Anderson", True, 450.1, 16 + 7j, 15, "Felicidad", False)
            print(tupla2)
            tupla3 = (9, 3, (4, 5, 6))
            print(tupla3)
            print(tupla2[1])
            # tupla2[1] = "Arroba"
            print(tupla2[-1])  # Acceder al último elemento.
            print(tupla2[0:4])
            print(tupla2[-2])

            a, b, c = tupla
            print(a)
            print(b)
            print(c)

            tuplaFinal = tupla + tupla3
            print(tuplaFinal)

            print(tuplaFinal.count(3))
            print(tuplaFinal.index(9))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSecuencias()

        elif opcion == '3':
            print("*" * 15 + " Listas " + "*" * 15 + "\n")

            lista1 = ["Anderson", 25, 98.3, True, "Jose", 56.3]
            print(lista1)
            print(lista1[:])
            print(lista1[2])
            print(lista1[-1])

            print(lista1[0:3])
            print(lista1[:2])
            print(lista1[3:])

            lista1.append("Arroba")
            print(lista1)

            lista1.insert(4, "Ecuador")
            print(lista1)

            lista1.extend(["Daemon", 110, False])
            print(lista1)

            print(lista1.index("Jose"))

            lista1.remove(56.3)
            print(lista1)

            lista1.pop()
            print(lista1)

            lista2 = ["Lucas", "Gissela"]
            lista3 = lista1 + lista2
            print(lista3)

            print(lista2 * 4)

            print("Arroba" in lista1)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSecuencias()

        elif opcion == '4':
            print("*" * 15 + " Diccionarios " + "*" * 15 + "\n")

            miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
            print(miDiccionario["Perú"])
            print(miDiccionario)

            miDiccionario["Venezuela"] = "Caracas"
            print(miDiccionario)

            miDiccionario["España"] = "Barcelona"
            print(miDiccionario)

            del miDiccionario["España"]
            print(miDiccionario)

            dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
            print(dic2[25])

            llaves = ("España", "Francia", "Inglaterra")
            dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
            print(dicPaises)

            datosPersonales = {"Ape": "García", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
            print(datosPersonales)
            print(datosPersonales["Anios"])

            print(datosPersonales.get('Apel', "Oscar"))

            print(datosPersonales.keys())
            valores = tuple(datosPersonales.values())
            print(valores)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuSecuencias()

        elif opcion == '0':
            pass

#opc = Secuencias()
#opc.menuSecuencias()