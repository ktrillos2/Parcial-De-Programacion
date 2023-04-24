# librería para verificar si un input es un correo
import re

# [correo,contraseña,rol,[nombre,documento,activo o no activo]]
usuarios = [
    ["admin@email.com", "admin123", "admin", []],
    ["cajero1@email.com", "cajero1", "cajero", ["prueba", "123456789", True]],
    ["cajero2@email.com", "cajero2", "cajero", ["prueba2", "1234567891", True]],
]

# ----------------------------------------------------------------Productos----------------------------------------------------------------
tipos2 = {
    "1": ["Vasos", True, ""],
    "2": ["Conos", False, ""],
    "3": ["Granizados", True, ""],
    "4": ["Copas infantiles", True, ""],
    "5": ["Malteadas", True, ""],
    "6": ["Litro de helado", True, ""],
    "7": ["Ensalada de frutas", True, ""],
    "8": ["Fresas", True, ""],
    "9": ["Copas", True, ""],
    "10": ["Banana split", True, ""],
    "11": ["Brownie con helado", True, ""],
    "12": ["Nuevas Categorias", True, ""],
}


# 1 = Vasos
tamaños_vasos = {
    "1": [("Sencillo", 5500), False, " -Este producto no se encuentra disponible"],
    "2": [("Doble", 8400), True, ""],
    "3": [("Triple", 10800), True, ""],
}
cantidad_bolas_vasos = {"Sencillo": 1, "Doble": 2, "Triple": 3}

# 2 = Conos
tamaños_conos = {
    "1": [("Pequeño", 4200), True, ""],
    "2": [("Mediano", 5500), True, ""],
    "3": [("Doble", 8400), True, ""],
    "4": [("Super cono", 10800), True, ""],
    "5": [("Mega cono", 14000), True, ""],
}

cantidad_bolas_conos = {
    "Pequeño": 1,
    "Mediano": 1,
    "Doble": 2,
    "Super cono": 3,
    "Mega cono": 4,
}

# 3 = Granizados
tamaños_granizados = {
    "1": [("Granizado 12 onz", 6400), True, ""],
    "2": [("Granizado 16 onz", 8400), True, ""],
    "3": [("Salpicon con helado", 9000), True, ""],
    "4": [("Salpicon sin helado", 6300), True, ""],
    "5": [("copa chocolate", 9000), True, ""],
}

# 4 = Copas infantiles
tamaños_copas_infantiles = {
    "1": [("Mickey", 6400), True, ""],
    "2": [("piñata", 10800), True, ""],
    "3": [("Fiesta", 8800), True, ""],
    "4": [("chips", 8800), True, ""],
}
cantidad_bolas_copa_infantil = {
    "Mickey": 1, "piñata": 1, "Fiesta": 2, "chips": 2}

# 5 = Malteadas
tamaños_malteadas = {
    "1": [("Malteada 12 onz", 10000), True, ""],
    "2": [("Malteada 16 onz", 12000), True, ""],
}

# 6 = Litro de helado
tamaños_litro_helado = {"1": [("Litro de helado", 27000), True, ""]}

# 7 = Ensalada de frutas
tamaños_ensalada_frutas = {
    "1": [("personal", 10800), True, ""],
    "2": [("para compartir sin helado", 10200), True, ""],
    "3": [("para compartir con helado", 14500), True, ""],
}

# 8 = Fresas
tamaños_fresas = {
    "1": [("Fresas con crema", 11400), True, ""],
    "2": [("Fresas con helado", 8400), True, ""],
}

# 9 = Copas
tamaños_copas = {
    "1": [("Exotica", 10800), True, ""],
    "2": [("Ron o amaretto", 10800), True, ""],
    "3": [("Caramelo", 10800), True, ""],
    "4": [("Tropical", 10800), True, ""],
    "5": [("Peach melba", 10800), True, ""],
    "6": [("De la casa", 10800), True, ""],
    "7": [("Sundae", 10800), False, "a"],
}
cantidad_bolas = {
    "Exotica": 3,
    "Ron o amaretto": 3,
    "Caramelo": 3,
    "Tropical": 3,
    "Peach melba": 2,
    "De la casa": 2,
    "Sundae": 2,
}

# 10 = Banana split
tamaños_banana_split = {"1": [("Banana split", 13200), True, ""]}

# 11 = Brownie con helado
tamaños_brownie = {"1": [("Brownie con helado", 13200), True, ""]}

# 12 SubCategorias Nuevas

subcategorias_nuevas = {1: [
    "galletas", True, "esto no se encuentra disponible ",{
    "1": [("Exotica", 10800), False, " No se encuentra disponible"],
    "2": [("Ron o amaretto", 10800), True, ""],
}], 2: ["sancocho", True, "",{}]}

# ----------------------------------------------------------------Fin de productos----------------------------------------------------------------


def validarCorreo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, correo))


def agregarCajero():
    while True:
        usuario = input("Ingrese correo: ").strip()
        if validarCorreo(usuario) == True:
            correoValido = True
            while correoValido == True:
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
                    "Ingrese documento del cajero: ").strip()
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
                    nuevoCorreo = input("Ingresa nuevo correo: ").strip()
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
                    "Ingrese documento del cajero: ").strip()
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
                    nuevaContraseña = input(
                        "Ingresa nueva contraseña: ").strip()
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
                    "Ingrese documento del cajero: ").strip()
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
                    nuevoNombre = input(
                        "Ingresa nuevo nombre: ").strip().lower()
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
                    "Ingrese documento del cajero: ").strip()
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
                    nuevoDocumento = input("Ingresa nuevo documento: ").strip()
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

def modificarProducto(productos):
    nombre_producto = input("Ingresa el nombre del producto que deseas modificar: ")
    encontrado = False
    for clave in productos.keys():
        if nombre_producto in productos[clave][0][0].lower():
            encontrado = True
            nombre_producto = clave
            break
    if encontrado:
        print(f"Actualmente el producto '{productos[nombre_producto][0][0]}' tiene el siguiente precio:")
        print(f"Precio: {productos[nombre_producto][0][1]}")
        opcion = input("¿Qué deseas modificar? (1) Precio o (2) eliminar el producto: ")
        if opcion == "1":
            nuevo_precio = input("Ingresa el nuevo precio del producto: ")
            productos[nombre_producto][1] = nuevo_precio
            print(f"El precio del producto '{productos[nombre_producto][0][0]}' ha sido actualizado a {nuevo_precio}.")
        elif opcion == "2":
            nueva_descripcion = input("Ingresa la nueva descripción del producto: ")
            productos[nombre_producto][2] = nueva_descripcion
            print(f"La descripción del producto '{nombre_producto}' ha sido actualizada a '{nueva_descripcion}'.")
        else:
            print("Opción inválida. Por favor, ingresa 1 o 2.")
    else:
        print(f"No se encontró el producto '{nombre_producto}' en la lista de productos.")

while True:
    usuario = input("Ingrese usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()
    encontrado = False
    for i in usuarios:
        if i[0] == usuario and i[1] == contraseña:
            encontrado = True
            correoUsuario = usuario
            if i[2] == "admin":
                while True:
                    preguntaAdmin = input(
                        "1. Cajeros\n2. Productos\n3. Ventas\nSelecciona una opción: "
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
                        while True:
                            preguntaCajero = input(
                                "1. Ver Productos\n2. Modificar Productos\nSeleccione una opción: "
                            ).strip()
                            if preguntaCajero == "1":
                                while True:
                                    cont = 1
                                    categoriasHabilitadas = []
                                    opciones = ""
                                    for i in tipos2:
                                        if tipos2[i][1] == True:
                                            categoriasHabilitadas.append(
                                                [tipos2[i][0], True]
                                            )
                                            cont += 1
                                        else:
                                            categoriasHabilitadas.append(
                                                [
                                                    tipos2[i][0] +
                                                    " (No habilitado)",
                                                    False,
                                                ]
                                            )
                                    for i, categoria in enumerate(
                                        categoriasHabilitadas
                                    ):
                                        nombreCategoria = categoria[0]
                                        opciones += (
                                            f"{i+1}. {nombreCategoria.capitalize()}\n"
                                        )
                                    preguntaCategoria = input(
                                        opciones + "Elige una opción: "
                                    )
                                    if preguntaCategoria.isdigit() and int(
                                        preguntaCategoria
                                    ) in range(1, cont + 1):
                                        opcionSeleccionada = int(
                                            preguntaCategoria)
                                        nombreCategoria = categoriasHabilitadas[
                                            opcionSeleccionada - 1
                                        ][0]
                                        estaHabilitada = categoriasHabilitadas[
                                            opcionSeleccionada - 1
                                        ][1]

                                        if not estaHabilitada:
                                            print(
                                                f"La categoría '{nombreCategoria}' está deshabilitada."
                                            )
                                        else:
                                            productos = {}
                                            if preguntaCategoria == "1":
                                                productos = tamaños_vasos
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "2":
                                                productos = tamaños_conos
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "3":
                                                productos = tamaños_granizados
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "4":
                                                productos = tamaños_copas_infantiles
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "5":
                                                productos = tamaños_malteadas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "6":
                                                productos = tamaños_litro_helado
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "7":
                                                productos = tamaños_ensalada_frutas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "8":
                                                productos = tamaños_fresas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "9":
                                                productos = tamaños_copas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "10":
                                                productos = tamaños_banana_split
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "11":
                                                productos = tamaños_brownie
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "12":
                                                if len(subcategorias_nuevas) == 0:
                                                    print(
                                                        "Esta categoría no tiene productos")
                                                else:
                                                    contSubCategoria = 1
                                                    subcategoriasHabilitadas = []
                                                    opcionesSubcategorias = ""
                                                    for i in subcategorias_nuevas:
                                                        subcategoriasHabilitadas.append(
                                                            [subcategorias_nuevas[i][0] + " " +
                                                                subcategorias_nuevas[i][2]]
                                                        )
                                                        contSubCategoria += 1
                                                    for i, subCategoria in enumerate(
                                                        subcategoriasHabilitadas
                                                    ):
                                                        nombreSubCategoria = subCategoria[0]
                                                        opcionesSubcategorias += (
                                                            f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                                        )
                                                    preguntaSubCategoria = input(
                                                        opcionesSubcategorias + "Elige una opción: "
                                                    )
                                                    if preguntaSubCategoria.isdigit() and int(preguntaSubCategoria) > 0 and int(preguntaSubCategoria) <= len(subcategoriasHabilitadas):
                                                        if len(subcategorias_nuevas[int(preguntaSubCategoria)][3])==0:
                                                            print("Esta subcategoria no tiene productos")
                                                        else:
                                                            if subcategorias_nuevas[int(preguntaSubCategoria)][1]==True:
                                                                for i in subcategorias_nuevas[int(preguntaSubCategoria)][3]:
                                                                    print(subcategorias_nuevas[int(preguntaSubCategoria)][3][i][0]," ",subcategorias_nuevas[int(preguntaSubCategoria)][3][i][2])
                                                            else:
                                                                print("Esta subcategoría se encuentra deshabilitada")
                                                    else:
                                                        print(
                                                            "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                                        )            
                                                        
                                                break
                                            break
                                    else:
                                        print(
                                            "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                        )
                                    break

                            elif preguntaCajero == "2":
                                while True:
                                    cont = 1
                                    categoriasHabilitadas = []
                                    opciones = ""
                                    for i in tipos2:
                                        if tipos2[i][1] == True:
                                            categoriasHabilitadas.append(
                                                [tipos2[i][0], True]
                                            )
                                            cont += 1
                                        else:
                                            categoriasHabilitadas.append(
                                                [
                                                    tipos2[i][0] +
                                                    " (No habilitado)",
                                                    False,
                                                ]
                                            )
                                    for i, categoria in enumerate(
                                        categoriasHabilitadas
                                    ):
                                        nombreCategoria = categoria[0]
                                        opciones += (
                                            f"{i+1}. {nombreCategoria.capitalize()}\n"
                                        )
                                    preguntaCategoria = input(
                                        opciones + "Elige una opción: "
                                    )
                                    if preguntaCategoria.isdigit() and int(
                                        preguntaCategoria
                                    ) in range(1, cont + 1):
                                        opcionSeleccionada = int(
                                            preguntaCategoria)
                                        nombreCategoria = categoriasHabilitadas[
                                            opcionSeleccionada - 1
                                        ][0]
                                        estaHabilitada = categoriasHabilitadas[
                                            opcionSeleccionada - 1
                                        ][1]

                                        if not estaHabilitada:
                                            print(
                                                f"La categoría '{nombreCategoria}' está deshabilitada."
                                            )
                                        else:
                                            productos = {}
                                            if preguntaCategoria == "1":
                                                productos = tamaños_vasos
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "2":
                                                productos = tamaños_conos
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "3":
                                                productos = tamaños_granizados
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "4":
                                                productos = tamaños_copas_infantiles
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "5":
                                                productos = tamaños_malteadas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "6":
                                                productos = tamaños_litro_helado
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "7":
                                                productos = tamaños_ensalada_frutas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "8":
                                                productos = tamaños_fresas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "9":
                                                productos = tamaños_copas
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "10":
                                                productos = tamaños_banana_split
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "11":
                                                productos = tamaños_brownie
                                                for i in productos:
                                                    print(
                                                        productos[i][0], productos[i][2])
                                                break
                                            elif preguntaCategoria == "12":
                                                if len(subcategorias_nuevas) == 0:
                                                    print(
                                                        "Esta categoría no tiene productos")
                                                else:
                                                    contSubCategoria = 1
                                                    subcategoriasHabilitadas = []
                                                    opcionesSubcategorias = ""
                                                    for i in subcategorias_nuevas:
                                                        subcategoriasHabilitadas.append(
                                                            [subcategorias_nuevas[i][0] + " " +
                                                                subcategorias_nuevas[i][2]]
                                                        )
                                                        contSubCategoria += 1
                                                    for i, subCategoria in enumerate(
                                                        subcategoriasHabilitadas
                                                    ):
                                                        nombreSubCategoria = subCategoria[0]
                                                        opcionesSubcategorias += (
                                                            f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                                        )
                                                    preguntaSubCategoria = input(
                                                        opcionesSubcategorias + "Elige una opción: "
                                                    )
                                                    if preguntaSubCategoria.isdigit() and int(preguntaSubCategoria) > 0 and int(preguntaSubCategoria) <= len(subcategoriasHabilitadas):
                                                        if len(subcategorias_nuevas[int(preguntaSubCategoria)][3])==0:
                                                            print("Esta subcategoria no tiene productos")
                                                        else:
                                                            if subcategorias_nuevas[int(preguntaSubCategoria)][1]==True:
                                                                for i in subcategorias_nuevas[int(preguntaSubCategoria)][3]:
                                                                    print(subcategorias_nuevas[int(preguntaSubCategoria)][3][i][0]," ",subcategorias_nuevas[int(preguntaSubCategoria)][3][i][2])
                                                            else:
                                                                print("Esta subcategoría se encuentra deshabilitada")
                                                    else:
                                                        print(
                                                            "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                                        )            
                                                        
                                                break
                                            break
                                    else:
                                        print(
                                            "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                        )
                                    break
                            else:
                                print("Ingresa un numero valido")
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
