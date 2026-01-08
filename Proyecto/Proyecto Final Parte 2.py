import sys


# Menu
def menu():
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
            nMenu = nMenu + 1
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


# submenuCifCesar

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def submenuCifCesar(palabra, clave):
    texto_cifrado = " "
    for letra in palabra:
        suma = abc.find(letra) + clave
        div = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[div])
    return texto_cifrado


def submenuDesCesar(palabra, clave):
    texto_cifrado = " "
    for letra in palabra:
        suma = abc.find(letra) - clave
        div = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[div])
    return texto_cifrado


# submenuCifLlave
def submenuCifLlave():

    nLlav = 1
    while nLlav == int(1):
        import re

        Mensaje = input("Escriba la palabra que desea cifrar: ")
        if not re.match("[a-z]", Mensaje):
            print("Error, debe introducir una palabra conformada unicamente por letras")
            return menu()
        if not re.match("[a-z]", Mensaje):
            print("Error, debe introducir una palabra conformada unicamente por letras")
            return menu()


# submenuSustVig

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def submenuCifVig(palabra, clave):
    texto_cifrado = " "
    i = 0
    for letra in palabra:
        suma = abc.find(letra) + abc.find(clave[i % len(clave)])
        div = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[div])
        i = i + 1
    return texto_cifrado


def submenuDesVig(palabra, clave):
    texto_cifrado = " "
    i = 0
    for letra in palabra:
        suma = abc.find(letra) - abc.find(clave[i % len(clave)])
        div = int(suma) % len(abc)
        texto_cifrado = texto_cifrado + str(abc[div])
        i = i + 1
    return texto_cifrado


# submenuPalInv
def submenuPalInv():

    nInv = 1
    while nInv == int(1):
        import re

        Mensaje = input("Escriba la o las palabras que desea cifrar: ")
        if not re.match("[a-z]", Mensaje):
            print("Error, debe introducir una palabra conformada unicamente por letras")
            return menu()


# submenuCodTel
def submenuCodTel():
    if RespuestaSubmenu == "1":
        nTel = 1
        while nTel == int(1):
            import re

            Mensaje = input("Escriba la o las palabras que desea cifrar: ")
            if not re.match("[a-z]", Mensaje):
                print(
                    "Error, debe introducir una palabra conformada unicamente por letras"
                )
                return menu()
            elif RespuestaSubmenu == "2":
                nTel = 1
                while nTel == int(1):
                    import re
                Mensaje = input(
                    "Escriba los numeros que desea descifrar, estos deben ir del 1 al 9: "
                )
            if not re.match("[1-9]", Mensaje):
                print("Error, los numeros deben ir del 1 al 9 ")
                return menu()


# submenuCodBin
def submenuCodBin():
    if RespuestaSubmenu == "1":
        nBin = 1
        while nBin == int(1):
            import re

            Mensaje = input("Escriba la o las palabras que desea cifrar: ")
            if not re.match("[a-z]", Mensaje):
                print(
                    "Error, debe introducir una palabra conformada unicamente por letras"
                )
                return menu()
    elif RespuestaSubmenu == "2":
        nBin = 1
        while nBin == int(1):
            import re

            Mensaje = input(
                "Escriba los numeros que desea descifrar, estos deben ir del 0 al 1: "
            )
            if not re.match("[0-1]", Mensaje):
                print("Error, los numeros deben ir del 0 al 1 ")
                return menu()


# ProgramaPrincipal


RespuestaMenu = menu()
RespuestaSubmenu = submenu()
if RespuestaMenu == "1" and RespuestaSubmenu == "1":
    import re
    import sys

    p = str(input("palabra a cifrar: "))
    if not re.match("[A-Z]", p):
        print(
            "Error, debe introducir una palabra conformada unicamente por letras mayusculas"
        )
        sys.exit("Fin programa")
    n = int(input("clave numerica: "))
    if 1 < n > 26:
        print(
            "Error, el numero de desplazamiento no califica con las normas especificadas"
        )
        sys.exit("Fin programa")
    print(submenuCifCesar(p, n))

if RespuestaMenu == "1" and RespuestaSubmenu == "2":
    import re
    import sys

    pc = str(input("palabra a descifrar: "))
    if not re.match("[A-Z]", pc):
        print(
            "Error, debe introducir una palabra conformada unicamente por letras mayusculas"
        )
        sys.exit("Fin programa")
    pn = int(input("clave numerica: "))
    if 1 < pn > 26:
        print(
            "Error, el numero de desplazamiento no califica con las normas especificadas"
        )
        sys.exit("Fin programa")
    print(submenuDesCesar(pc, pn))

elif RespuestaMenu == "2":
    print(submenuCifLlave())

elif RespuestaMenu == "3" and RespuestaSubmenu == "1":
    import re
    import sys

    pc = str(input("palabra a cifrar: "))
    if not re.match("[A-Z]", pc):
        print(
            "Error, debe introducir una palabra conformada unicamente por letras mayusculas"
        )
        sys.exit("Fin programa")
    clave = str(input("clave: "))
    if not re.match("[A-Z]", clave):
        print(
            "Error, debe introducir una palabra conformada unicamente por letras mayusculas"
        )
        sys.exit("Fin programa")
    print(submenuCifVig(pc, clave))

elif RespuestaMenu == "3" and RespuestaSubmenu == "2":
    import re
    import sys

    pc = str(input("palabra a descifrar: "))
    if not re.match("[A-Z]", pc):
        print(
            "Error, debe introducir una palabra conformada unicamente por letras mayusculas"
        )
        sys.exit("Fin programa")
    clave = str(input("clave: "))
    if not re.match("[A-Z]", clave):
        print(
            "Error, debe introducir una palabra conformada unicamente por letras mayusculas"
        )
        sys.exit("Fin programa")
    print(submenuDesVig(pc, clave))

elif RespuestaMenu == "4":
    print(submenuPalInv())
elif RespuestaMenu == "5":
    print(submenuCodTel())
elif RespuestaMenu == "6":
    print(submenuCodBin())
