usuarios = [
    ["admin@email.com", "admin123", "admin", []],
    ["cajero1@email.com", "cajero1", "cajero", ["prueba", "123456789", True]],
    ["cajero2@email.com", "cajero2", "cajero", ["prueba2", "1234567891", True]],
]


def agregarCajero():
    usuario = input("Ingrese correo: ")
    contraseña = input("Ingrese contraseña: ")
    nombre = input("Ingrese nombre: ")
    while True:
        documento = input("Ingrese documento: ")
        if documento.isdigit():
            if len(documento) < 8:
                print("Documento muy corto")
            elif len(documento) > 10:
                print("Documento muy largo")
            else:
                break
        else:
            print("Ingresa un documento valido")
    usuarios.append([usuario, contraseña, "cajero", [nombre, documento, True]])


def eliminarCajero():
    encontrado = False
    while True:
        documento = input("Ingrese documento del cajero a eliminar: ")
        if documento.isdigit():
            if len(documento) < 8:
                print("Documento muy corto")
            elif len(documento) > 10:
                print("Documento muy largo")
            else:
                break
        else:
            print("Ingresa un documento valido")

    for usuario in usuarios:
        for i in range(len(usuario[3])):
            if documento == usuario[3][1]:
                encontrado = True
                usuario[3][2] = False

    if encontrado == False:
        print("Documento no encontrado")
        return False
    else:
        print(usuarios)
        return True


def iniciarSesion(usuario, contraseña):
    encontrado = False
    for i in usuarios:
        if i[0] == usuario and i[1] == contraseña:
            encontrado = True
            if i[2] == "admin":
                while True:
                    preguntaAdmin = input(
                        "1. Cajeros\n2. Ver productos\n3. Ventas\nSelecciona una opción: "
                    )
                    if preguntaAdmin == "1":
                        while True:
                            preguntaCajero = input(
                                "1. Eliminar Cajeros\n2. Agregar Cajero\n3. Modificar Cajero\n4. Regresar al menu anterior\nSelecciona una opción: "
                            )
                            if preguntaCajero == "1":
                                if eliminarCajero() == True:
                                    break
                            elif preguntaCajero == "2":
                                agregarCajero()
                                break
                            elif preguntaCajero == "3":
                                ##codigo para modificar cajero
                                break
                            elif preguntaCajero == "4":
                                break
                            else:
                                print("Ingresa un numero valido")
                    elif preguntaAdmin == "2":
                        # codigo de productos
                        break
                    elif preguntaAdmin == "3":
                        # codigo de ventas
                        break
                    else:
                        print("Ingresa un numero valido")
            if i[2] == "cajero":
                print("Ingresaste como cajero")
            if i[2] == "usuario":
                print("Ingresaste como usuario")
    if not encontrado:
        while True:
            pregunta = input(
                "Lo siento, no pudimos encontrar una cuenta con los datos de inicio de sesión que proporcionaste. ¿Deseas crear una cuenta nueva? (si/no) "
            ).lower()
            if pregunta == "si":
                # Aqui va codigo para agregar a una persona
                break
            elif pregunta == "no":
                print("Gracias por usar nuestro programa")
                break
            else:
                print("Ingresa una opción valida")


usuario = input("Ingrese usuario: ")
contraseña = input("Ingrese contraseña: ")
iniciarSesion(usuario, contraseña)
