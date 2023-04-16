# librería para verificar si un input es un correo
import re

# [correo,contraseña,rol,[nombre,documento,activo o no activo]]
usuarios = [
    ["admin@email.com", "admin123", "admin", []],
    ["cajero1@email.com", "cajero1", "cajero", ["prueba", "123456789", True]],
    ["cajero2@email.com", "cajero2", "cajero", ["prueba2", "1234567891", True]],
]


def validarCorreo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, correo))


def agregarCajero():
    while True:
        usuario = input("Ingrese correo: ").strip()
        if validarCorreo(usuario) == True:
            correoValido = True
            while correoValido==True:
                existeCorreo = False
                for datos in usuarios:
                    if datos[0] == usuario:
                        existeCorreo = True
                if existeCorreo == True:
                    while True:
                        preguntaCorreoSalir = (
                            input(
                                "1. Salir al menu anterior\n2. Ingresar otro correo\nEl correo que ingresaste ya existe en nuestro sistema. Por favor, selecciona una de las siguientes opciones ingresando el número correspondiente : "
                            )
                            .strip()
                            .lower()
                        )
                        if preguntaCorreoSalir == "1":
                            return False
                        elif preguntaCorreoSalir == "2":
                            break
                        else:
                            print("Ingresa una opción valida")
                    usuario = input("Ingrese correo: ").strip()
                    if validarCorreo(usuario) == False:
                        print("Ingresa un correo valido")
                        correoValido = True
                    else:
                        correoValido = True
                else:
                    correoValido = False
                    break
            contraseña = input("Ingrese contraseña: ").strip()
            nombre = input("Ingrese nombre: ").strip()
            while True:
                existe = False
                documento = input("Ingrese documento: ").strip()
                if documento.isdigit():
                    if len(documento) < 8:
                        print("Documento muy corto")
                    elif len(documento) > 10:
                        print("Documento muy largo")
                    else:
                        for datos in usuarios:
                            for i in range(len(datos[3])):
                                if documento == datos[3][1]:
                                    existe = True
                        if existe == True:
                            while True:
                                preguntaSalir = (
                                    input(
                                        "1. Salir al menu anterior\n2. Ingresar otro documento\nEl documento que ingresaste ya existe en nuestro sistema. Por favor, selecciona una de las siguientes opciones ingresando el número correspondiente : "
                                    )
                                    .strip()
                                    .lower()
                                )
                                if preguntaSalir == "1":
                                    return False
                                elif preguntaSalir == "2":
                                    break
                                else:
                                    print("Ingresa una opción valida")
                        else:
                            usuarios.append(
                                [
                                    usuario,
                                    contraseña,
                                    "cajero",
                                    [nombre, documento, True],
                                ]
                            )
                            print("Cajero registrado exitosamente")
                            return True
                else:
                    print("Ingresa un documento valido")
        else:
            print("Ingresa un correo valido")


def eliminarCajero():
    while True:
        existe = False
        documento = input("Ingrese documento: ").strip()
        if documento.isdigit():
            if len(documento) < 8:
                print("Documento muy corto")
            elif len(documento) > 10:
                print("Documento muy largo")
            else:
                for datos in usuarios:
                    for i in range(len(datos[3])):
                        if documento == datos[3][1]:
                            existe = True
                            datos[3][2] = False
                if existe == False:
                    while True:
                        preguntaSalir = (
                            input(
                                "1. Salir al menu anterior\n2. Ingresar otro documento\nEl documento que ingresaste ya existe en nuestro sistema. Por favor, selecciona una de las siguientes opciones ingresando el número correspondiente : "
                            )
                            .strip()
                            .lower()
                        )
                        if preguntaSalir == "1":
                            return False
                        elif preguntaSalir == "2":
                            break
                        else:
                            print("Ingresa una opción valida")
                else:
                    print("Cajero eliminado satisfactoriamente")
                    return True
        else:
            print("Ingresa un documento valido")


def modificarCajero():
    while True:
        pregunta = input(
            "1. Correo\n2. Contraseña\n3. Nombre\n4. Documento\nPor favor, seleccione el número del campo que desea modificar: "
        ).strip()
        if pregunta == "1":
            while True:
                documentoUsuario = input(
                    "Ingrese documento del cajero: "
                ).strip()
                if documentoUsuario.isdigit():
                    if len(documentoUsuario) < 8:
                        print("documento muy corto")
                    elif len(documentoUsuario) > 10:
                        print("documento muy largo")
                    else:
                        break
                else:
                    print("Ingresa un documento valido")
            encontrado = False
            for usuario in usuarios:
                for i in range(len(usuario[3])):
                    if documentoUsuario == usuario[3][1]:
                        encontrado = True

            if encontrado == False:
                print("Documento no encontrado")
            else:
                print("Usuario Encontrado")
                while True:
                    nuevoCorreo = input("Ingresa nuevo correo: ").strip().lower()
                    if validarCorreo(nuevoCorreo) == True:
                        for usuario in usuarios:
                            for i in range(len(usuario[3])):
                                if documentoUsuario == usuario[3][1]:
                                    usuario[0] = nuevoCorreo
                                    print(
                                        "El usuario ",
                                        usuario[3][0],
                                        " con documento ",
                                        documentoUsuario,
                                        " , se le actualizo el correo, y el nuevo correo es: ",
                                        nuevoCorreo,
                                    )
                                    return True
                        break
                    else:
                        print("Ingresa un correo valido")
            break
        elif pregunta == "2":
            while True:
                documentoUsuario = input(
                    "Ingrese documento del cajero: "
                ).strip()
                if documentoUsuario.isdigit():
                    if len(documentoUsuario) < 8:
                        print("documento muy corto")
                    elif len(documentoUsuario) > 10:
                        print("documento muy largo")
                    else:
                        break
                else:
                    print("Ingresa un documento valido")
            encontrado = False
            for usuario in usuarios:
                for i in range(len(usuario[3])):
                    if documentoUsuario == usuario[3][1]:
                        encontrado = True

            if encontrado == False:
                print("Documento no encontrado")
            else:
                print("Usuario Encontrado")
                while True:
                    nuevaContraseña = input("Ingresa nueva contraseña: ").strip().lower()
                    for usuario in usuarios:
                        for i in range(len(usuario[3])):
                            if documentoUsuario == usuario[3][1]:
                                usuario[1] = nuevaContraseña
                                print(
                                    "El usuario ",
                                    usuario[3][0],
                                    " con documento ",
                                    documentoUsuario,
                                    " , se le actualizo la contraseña, y la nueva contraseña es: ",
                                    nuevaContraseña,
                                )
                                return True
                    break
            break
        elif pregunta == "3":
            while True:
                documentoUsuario = input(
                    "Ingrese documento del cajero: "
                ).strip()
                if documentoUsuario.isdigit():
                    if len(documentoUsuario) < 8:
                        print("documento muy corto")
                    elif len(documentoUsuario) > 10:
                        print("documento muy largo")
                    else:
                        break
                else:
                    print("Ingresa un documento valido")
            encontrado = False
            for usuario in usuarios:
                for i in range(len(usuario[3])):
                    if documentoUsuario == usuario[3][1]:
                        encontrado = True

            if encontrado == False:
                print("Documento no encontrado")
            else:
                print("Usuario Encontrado")
                while True:
                    nuevoNombre = input("Ingresa nuevo nombre: ").strip().lower()
                    for usuario in usuarios:
                        for i in range(len(usuario[3])):
                            if documentoUsuario == usuario[3][1]:
                                usuario[3][0] = nuevoNombre
                                print(
                                    "El usuario ",
                                    usuario[3][0],
                                    " con documento ",
                                    documentoUsuario,
                                    " , se le actualizo el nombre, y el nuevo nombre es: ",
                                    nuevoNombre,
                                )
                                return True
                    break
            break
        elif pregunta == "4":
            while True:
                documentoUsuario = input(
                    "Ingrese documento del cajero: "
                ).strip()
                if documentoUsuario.isdigit():
                    if len(documentoUsuario) < 8:
                        print("documento muy corto")
                    elif len(documentoUsuario) > 10:
                        print("documento muy largo")
                    else:
                        break
                else:
                    print("Ingresa un documento valido")
            encontrado = False
            for usuario in usuarios:
                for i in range(len(usuario[3])):
                    if documentoUsuario == usuario[3][1]:
                        encontrado = True

            if encontrado == False:
                print("Documento no encontrado")
            else:
                print("Usuario Encontrado")
                while True:
                    nuevoDocumento = input("Ingresa nuevo documento: ").strip().lower()
                    for usuario in usuarios:
                        for i in range(len(usuario[3])):
                            if documentoUsuario == usuario[3][1]:
                                usuario[3][1] = nuevoDocumento
                                print(
                                    "El usuario ",
                                    usuario[3][0],
                                    " con documento ",
                                    documentoUsuario,
                                    " , se le actualizo el documento, y el nuevo documento es: ",
                                    nuevoDocumento,
                                )
                                return True
                    break
            break
        else:
            print("Ingresa una opción valida")


def iniciarSesion(usuario, contraseña):
    encontrado = False
    for i in usuarios:
        if i[0] == usuario and i[1] == contraseña:
            encontrado = True
            if i[2] == "admin":
                while True:
                    preguntaAdmin = input(
                        "1. Cajeros\n2. Ver productos\n3. Ventas\nSelecciona una opción: "
                    ).strip()
                    if preguntaAdmin == "1":
                        while True:
                            preguntaCajero = input(
                                "1. Eliminar Cajeros\n2. Agregar Cajero\n3. Modificar Cajero\n4. Ver cajeros\n5. Regresar al menu anterior\nSelecciona una opción: "
                            ).strip()
                            if preguntaCajero == "1":
                                if eliminarCajero() == True:
                                    break
                            elif preguntaCajero == "2":
                                if agregarCajero() == True:
                                    break
                            elif preguntaCajero == "3":
                                if modificarCajero() == True:
                                    break
                            elif preguntaCajero == "4":
                                for usuario in usuarios:
                                    print(usuario)
                                break
                            elif preguntaCajero == "5":
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
            pregunta = (
                input(
                    "Lo siento, no pudimos encontrar una cuenta con los datos de inicio de sesión que proporcionaste. ¿Deseas crear una cuenta nueva? (si/no) "
                )
                .strip()
                .lower()
            )
            if pregunta == "si":
                # Aqui va codigo para agregar a una persona
                break
            elif pregunta == "no":
                print("Gracias por usar nuestro programa")
                break
            else:
                print("Ingresa una opción valida")


usuario = input("Ingrese usuario: ").strip().lower()
contraseña = input("Ingrese contraseña: ").strip().lower()
iniciarSesion(usuario, contraseña)
