from Menu import Menu
import os



class POO(Menu):

    def __init__(self):
        pass

    def menuPOO(self):
        opcion = self.menu(["1. Cuenta", "2. Curso", "3. Herencia", "4. Herencia Multiple", "5. Persona", "6. Polimorfismo", "7. Relaciones entre Clases", "0. Salir"], "*" * 20 + " MENU DE POO " + "*" * 19)
        os.system("cls")

        if opcion == '1':
            print("*" * 15 + " Cuenta " + "*" * 15 + "\n")

            class Cuenta():

                def __init__(self, pro, sal, mon):
                    self.__propietario = pro
                    self.__saldo = sal
                    self.__moneda = mon

                # Getters (métodos GET)
                def get_Saldo(self):
                    return self.__saldo

                def get_Propietario(self):
                    return self.__propietario

                def get_Moneda(self):
                    return self.__moneda

                # Setters (métodos SET)
                def set_Moneda(self, moneda):
                    self.__moneda = moneda

            cuenta1 = Cuenta("Anderson Arroba", 15000, "Soles")
            print(cuenta1.get_Saldo())
            print(cuenta1.get_Moneda())
            cuenta1.set_Moneda("Dólares")
            print(cuenta1.get_Moneda())

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '2':
            print("*" * 15 + " Curso " + "*" * 15 + "\n")

            class Curso():
                """
                nombre = "Matemática"
                creditos = 5
                profesion = "Ingeniería Civil"
                """

                # Estado inicial del objeto:
                def __init__(self, nom, cre, pro):
                    self.nombre = nom
                    self.creditos = cre
                    self.profesion = pro
                    self.__imparticion = "Presencial"  # Propiedad encapsulada.

                def mostrarDatos(self):
                    dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
                    print(dat.format(self.nombre, self.creditos, self.__imparticion))
                    docenteAsignado = self.__verificarDocente()
                    if docenteAsignado:
                        print("Existe docente asignado.")
                    else:
                        print("No es necesario asignar un docente...")

                def __verificarDocente(self):
                    # print("Verificando si existe docente asignado...")
                    if self.__imparticion == "Presencial":
                        return True
                    else:
                        return False

                # toString()
                def __str__(self):
                    texto = "Nombre: {0} - Créditos: {1}"
                    return texto.format(self.nombre, self.creditos)

            curso1 = Curso("Python", 5, "Ingeniería de Software")
            print(curso1)
            curso1.mostrarDatos()

            # curso2 = Curso("Lenguaje", 4, "Ingeniería Industrial")
            # print(curso2.nombre)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '3':
            print("*" * 15 + " Herencia " + "*" * 15 + "\n")

            class Persona():

                def __init__(self, apePat, apeMat, nom):
                    self.apellidoPaterno = apePat
                    self.apellidoMaterno = apeMat
                    self.nombres = nom

                def mostrarNombreCompleto(self):
                    txt = "{0} {1}, {2}"
                    return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

                def datos(self):
                    print(self.mostrarNombreCompleto())

            class Estudiante(Persona):

                def __init__(self, apePat, apeMat, nom, pro):
                    super().__init__(apePat, apeMat, nom)
                    self.profesion = pro

                def datos(self):
                    super().datos()
                    print("Profesión: {0}".format(self.profesion))

            # estu1 = Estudiante("Arroba", "Cordova", "Anderson", "Ingeniería de Software")
            per1 = Persona("Arroba", "Cordova", "Anderson")
            # print(estu1.mostrarNombreCompleto())
            # print(estu1.profesion)
            # estu1.datos()

            print(isinstance(per1, Estudiante))

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '4':
            print("*" * 15 + " Herencia Multiple " + "*" * 15 + "\n")

            class ClaseA():

                def __init__(self, par1, par2):
                    self.parametro1 = par1
                    self.parametro2 = par2

            class ClaseB():

                def __init__(self, par3, par4, par5):
                    self.parametro3 = par3
                    self.parametro4 = par4
                    self.parametro5 = par5

            class ClaseX(ClaseA, ClaseB):
                pass

            cX1 = ClaseX(15, 21)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '5':
            print("*" * 15 + " Persona " + "*" * 15 + "\n")

            class Persona():
                apellidos = ""
                nombres = ""
                edad = 0
                despierta = False

                def despertar(self):
                    self.despierta = True
                    print("Buen día.")

            persona1 = Persona()
            persona1.apellidos = "Arroba Cordova"
            print(persona1.apellidos)
            persona1.despertar()
            print(persona1.despierta)

            persona2 = Persona()
            persona2.apellidos = "Vega Pluas"
            print(persona2.apellidos)
            # persona2.despertar()
            print(persona2.despierta)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '6':
            print("*" * 15 + " Polimorfismo " + "*" * 15 + "\n")

            class Estudiante():

                def describir(self):
                    print("Soy un buen estudiante.")

            class Docente():

                def describir(self):
                    print("Me dedico a enseñar cursos.")

            class Trabajador():

                def describir(self):
                    print("Trabajo dentro de una gran empresa.")

            def describirPersona(persona):
                persona.describir()

            # doc1 = Docente()
            doc1 = Trabajador()
            describirPersona(doc1)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '7':
            print("*" * 15 + " Relaciones entre Clases " + "*" * 15 + "\n")

            class Pais():

                def __init__(self, nom, pre):
                    self.nombre = nom
                    self.presidente = pre

                def __str__(self):
                    txt = "País: {0} - Presidente: {1}"
                    return txt.format(self.nombre, self.presidente)

            class Ciudad():

                def __init__(self, nom, hab, pai):
                    self.nombre = nom
                    self.habitantes = hab
                    self.pais = pai

                def __str__(self):
                    txt = "Ciudad: {0} - N° Habitantes: {1} ({2})"
                    return txt.format(self.nombre, self.habitantes, self.pais)

            class Urbanizacion():

                def __init__(self, nom, ciu):
                    self.nombre = nom
                    self.ciudad = ciu

                def __str__(self):
                    txt = "Urbanización: {0} ({1})"
                    return txt.format(self.nombre, self.ciudad)

            pais1 = Pais("Ecuador", "Anderson Arroba")
            print(pais1)

            ciudad1 = Ciudad("Leonardo", 150000, pais1)
            print(ciudad1)

            urba1 = Urbanizacion("Deyanira", ciudad1)
            print(urba1)

            # Regreso al menu
            print("\n" + "*" * 42)
            print("* Presione enter para regresar al menu *")
            input("*" * 42 + "\n"), os.system("cls"), self.menuPOO()

        elif opcion == '0':
            pass

#opc = POO()
#opc.menuPOO()