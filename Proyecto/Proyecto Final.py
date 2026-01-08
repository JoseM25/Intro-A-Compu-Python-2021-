import sys


# Menu
def menu():

    RespuestaMenu = 0
    print("\n", "MENU PRINCIPAL")
    print("[1] Cifrado Cesar")
    print("[2] Cifrado llave")
    print("[3] Sustitucion Vigenere")
    print("[4] Cifrado Palabra Inversa ")
    print("[5] Cifrado Codigo Telefonico")
    print("[6] Cifrado Codigo Binario")
    print("[7] Salir", "\n")

    RespuestaMenu = str(
        input(
            "Seleccione el metodo de encriptacion o desencripacion que desea utilzar:"
        )
    )
    nMenu = 1
    while nMenu == int(1):
        if (RespuestaMenu) > "0" and (RespuestaMenu) < "7":
            return RespuestaMenu
        elif (RespuestaMenu) == "7":
            sys.exit("fin del programa")
        else:
            print("La respuesta debe de ser un numero entre 1 y 7", "\n")
            return menu()


# Submenu
def submenu():

    nSub = 1
    while nSub == int(1):
        RespuestaSubmenu = 0
        print("\n", "SUBMENU")
        print("[1] Cifrar")
        print("[2] Descifrar")
        print("[3] Regresar")

        RespuestaSubmenu = str(input("Seleccione la accion que desea realizar:"))
        if (RespuestaSubmenu) > "0" and (RespuestaSubmenu) < "3":
            return RespuestaSubmenu
        elif (RespuestaSubmenu) == "3":
            print("regresar menu" "\n")
            return menu()
        else:
            print("La respesta debe de ser un numero entre 1 y 3", "\n")

        RespuestaSubmenu = int(input("Seleccione la accion que desea realizar:"))
        if (RespuestaSubmenu) == 1:
            if int(RespuestaSubmenu) == int(1):
                n = input(
                    "indique el numero de veces que desea desplazar las letras, debe ser un numero mayor o igual a 1 y menor a 26"
                )
                if (int(n)) < 1 or int(n) > int(26):
                    print(
                        "Error, el numero de desplazamiento no califica con las normas especificadas"
                    )
                    return menu()
            if int(RespuestaSubmenu) == int(3):
                n = input("Indique la cifra que desea aplicarle a la codificacion")
                if (int(n)) < int(10):
                    print("Error, la cifra debe poseer al menos 2 digitos")
                    return menu()
        elif (RespuestaSubmenu) == int(2):
            input("Escriba la o las palabras que desea descifrar: ")
        elif (RespuestaSubmenu) == int(3):
            print("regresar menu" "\n")
            return menu()
        elif (RespuestaSubmenu) > int(3):
            print("El numero seleccionado no esta dentro de las opciones", "\n")


# ProgramaPrincipal

print(menu())

print(submenu())
