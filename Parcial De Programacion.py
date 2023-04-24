# librería para verificar si un input es un correo
import re

# Fecha
import datetime

fecha_actual = datetime.date.today()

fecha_formateada = fecha_actual.strftime('%d/%m/%Y')

# [correo,contraseña,rol,[nombre,documento,activo o no activo]]
usuarios = [
    ["admin@email.com", "admin123", "admin", []],
    ["cajero1@email.com", "cajero1", "cajero", ["prueba", "123456789", True]],
    ["cajero2@email.com", "cajero2", "cajero", ["prueba2", "1234567891", True]],
]

#Afuera de todo el codigo
ventas_generales = []
contador_general=1

#Se debe poner estos 3 datos en la parte antes del codigo de ingresar compra
total=0
factura_temporal= [] 
Factura_unica = []

# Extras

sabores = {"1": "maracuya en agua","2":"tropical de agua","3":"chicle","4":"frutos rojos","5":"arequipe"
           ,"6":"nata","7":"crocante","8":"maracuya en leche","9":"caramelo","10":"cereza","11":"fresa"
           ,"12":"vainilla chips","13":"brownie","14":"galleta oreo","15":"leche klim"
           ,"16":"chocolate","17":"MyM","18":"queso","19":"vainilla","20":"ron con pasas","21":"nucita","22":"stracciatella",}

granizados = {"1": "frutos rojos","2":"naranja","3":"mango","4":"fresa","5":"cereza"}

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
    "1": [["Sencillo", 5500], False, " -Este producto no se encuentra disponible"],
    "2": [["Doble", 8400], True, ""],
    "3": [["Triple", 10800], True, ""],
}
cantidad_bolas_vasos = {"Sencillo":1, "Doble": 2, "Triple":3}
n_vasos=len(tamaños_vasos)+1

# 2 = Conos
tamaños_conos = {
    "1": [["Pequeño", 4200], True, ""],
    "2": [["Mediano", 5500], True, ""],
    "3": [["Doble", 8400], True, ""],
    "4": [["Super cono", 10800], True, ""],
    "5": [["Mega cono", 14000], True, ""],
}
n_conos=len(tamaños_conos)+1
cantidad_bolas_conos = {"Pequeño":1, "Mediano": 1, "Doble":2, "Super cono": 3, "Mega cono":4}

# 3 = Granizados
tamaños_granizados = {
    "1": [["Granizado 12 onz", 6400], True, ""],
    "2": [["Granizado 16 onz", 8400], True, ""],
    "3": [["Salpicon con helado", 9000], True, ""],
    "4": [["Salpicon sin helado", 6300], True, ""],
    "5": [["copa chocolate", 9000], True, ""],
}
n_granizados=len(tamaños_granizados)+1

# 4 = Copas infantiles
tamaños_copas_infantiles = {
    "1": [["Mickey", 6400], True, ""],
    "2": [["piñata", 10800], True, ""],
    "3": [["Fiesta", 8800], True, ""],
    "4": [["chips", 8800], True, ""],
}
cantidad_bolas_copa_infantil = {"Mickey":1, "piñata": 1, "Fiesta":2, "chips": 2}

n_infantil=len(tamaños_copas_infantiles)+1
# 5 = Malteadas
tamaños_malteadas = {
    "1": [["Malteada 12 onz", 10000], True, ""],
    "2": [["Malteada 16 onz", 12000], True, ""],
}
n_malteadas=len(tamaños_malteadas)+1

# 6 = Litro de helado
tamaños_litro_helado = {"1": [["Litro de helado", 27000], True, ""]}
n_litro_helado=len(tamaños_litro_helado)+1

# 7 = Ensalada de frutas
tamaños_ensalada_frutas = {
    "1": [["personal", 10800], True, ""],
    "2": [["para compartir sin helado", 10200], True, ""],
    "3": [["para compartir con helado", 14500], True, ""],
}
n_frutas=len(tamaños_ensalada_frutas)+1

# 8 = Fresas
tamaños_fresas = {
    "1": [["Fresas con crema", 11400], True, ""],
    "2": [["Fresas con helado", 8400], True, ""],
}
n_fresas=len(tamaños_fresas)+1

# 9 = Copas
tamaños_copas = {
    "1": [["Exotica", 10800], True, ""],
    "2": [["Ron o amaretto", 10800], True, ""],
    "3": [["Caramelo", 10800], True, ""],
    "4": [["Tropical", 10800], True, ""],
    "5": [["Peach melba", 10800], True, ""],
    "6": [["De la casa", 10800], True, ""],
    "7": [["Sundae", 10800], False, "a"],
}
n_copas=len(tamaños_copas)+1
cantidad_bolas = {"Exotica":3, "Ron o amaretto": 3, "Caramelo":3, "Tropical": 3
                  , "Peach melba":2, "De la casa": 2, "Sundae":2}

# 10 = Banana split
tamaños_banana_split = {"1": [["Banana split", 13200], True, ""]}
n_banana=len(tamaños_banana_split)+1

# 11 = Brownie con helado
tamaños_brownie = {"1": [["Brownie con helado", 13200], True, ""]}
n_brownie=len(tamaños_brownie)+1

#12 = Paletas
n_paletas=13

# 13 SubCategorias Nuevas

subcategorias_nuevas = {1: [
    "galletas", True, "esto no se encuentra disponible ",{
    "1": [["Exotica", 10800], False, " No se encuentra disponible"],
    "2": [["Ron o amaretto", 10800], True, ""],
}], 2: ["sancocho", True, "",{}]}

# ----------------------------------------------------------------Fin de productos----------------------------------------------------------------

def validar_opcion(num_inicio, num_fin, pregunta):
    while True:
        opcion = input(pregunta)
        if opcion.isdigit():
            opcion = int(opcion)
            if num_inicio <= opcion <= num_fin:
                return str(opcion)
        print("Por favor ingresa una opción válida entre", num_inicio, "y", num_fin)

def Sabor_helados():
    sabores = {"1": "maracuya en agua","2":"tropical de agua","3":"chicle","4":"frutos rojos","5":"arequipe"
               ,"6":"nata","7":"crocante","8":"maracuya en leche","9":"caramelo","10":"cereza","11":"fresa"
               ,"12":"vainilla chips","13":"brownie","14":"galleta oreo","15":"leche klim"
               ,"16":"chocolate","17":"MyM","18":"queso","19":"vainilla","20":"ron con pasas","21":"nucita","22":"stracciatella",}
    
    cont=1
    for i in sabores:
        h=print(cont,sabores[i])
        cont+=1
    return h

def Sabor_paletas():
    sabores = {"1": "leche klim","2":"maracuya","3":"fresas con chocolate","4":"MyM","5":"Chantilli"
               ,"6":"ron con pasas","7":"nucita","8":"frutos rojos","9":"chocomani","10":"oreo","11":"Chocolate"
               ,"12":"Queso"}
    
    cont=1
    for i in sabores:
        h=print(cont,sabores[i])
        cont+=1
    return h

def validarCorreo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, correo))

def agregarUsuario():
    while True:
        nuevo_usuario = input("Ingresa tu correo: ").strip()
        if validarCorreo(nuevo_usuario)==True:
            break
    while True:
        documento = input("Ingrese su documento: ").strip()
        if documento.isdigit() and (len(documento) >= 8 or len(documento) <= 10):
            break
        else:
            print("Documento inválido. Debe ser un número entero de 8 o 10 dígitos.")
    nombre = input("Ingrese su nombre: ")
    while True:
        telefono = input("Ingrese su teléfono: ").strip()
        if telefono.isdigit() and (len(telefono) == 10):
            break
        else:
            print("Numero inválido. Debe ser un número entero de 10 dígitos.")
    direccion = input("Ingrese su dirección: ")
    contraseña = input("Ingrese una contraseña: ")
    usuarios.append([nuevo_usuario,contraseña, "usuario", [nombre, documento, True, telefono, direccion]])
    print("Usuario Creado exitosamente, ahora puedes iniciar sesión")

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
    while True:
        print("Opciones de productos disponibles:")
        for i, producto in enumerate(productos.values()):
            print(f"{i+1}. {producto[0][0]} - ${producto[0][1]} {producto[2]}")
        print(f"{len(productos) + 1}. Volver al menú anterior")

        seleccion = input("Ingrese el número correspondiente al producto que desea modificar: ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion >= 1 and seleccion <= len(productos):
                nombre_producto = list(productos.keys())[seleccion-1]
                print(f"Actualmente el producto '{productos[nombre_producto][0][0]}' tiene el siguiente precio:")
                print(f"Precio: {productos[nombre_producto][0][1]}")
                while True:
                    opcion = input("1. Precio\n2. Eliminar Producto\n3. Volver al menu anterior\n¿Qué deseas modificar?: ")
                    if opcion == "1":
                        while True:
                            nuevo_precio = input("Ingresa el nuevo precio del producto: ")
                            if nuevo_precio.isdigit():
                                productos[nombre_producto][0][1] = int(nuevo_precio)
                                print(f"El precio del producto '{productos[nombre_producto][0][0]}' ha sido actualizado a {nuevo_precio}.")
                                break
                            else:
                                print("Error: el precio debe ser un número entero.")
                        break
                    elif opcion == "2":
                        productos[nombre_producto][1] = False
                        productos[nombre_producto][2] = "- No se encuentra habilitado"
                        print(f"el producto '{productos[nombre_producto][0][0]}' ha sido eliminado")
                        break
                    elif opcion=="3":
                        break
                    else:
                        print("Opción inválida. Por favor, ingresa 1 o 2.")
            elif seleccion == len(productos) + 1:
                break
            else:
                print(f"El número de producto '{seleccion}' no es válido. Por favor, ingresa un número válido.")
        else:
            print(f"La opción ingresada '{seleccion}' no es válida. Por favor, ingresa una opción válida.")

def modificarProductosSubcategoria(productos):
    if len(productos) == 0:
        print("Esta subcategoría no tiene productos.")
    else:
        opcionesProductos = ""
        for i, producto in enumerate(productos.items()):
            nombreProducto = producto[1][0]
            disponibleProducto = "disponible" if producto[1][1] else "no disponible"
            opcionesProductos += f"{i+1}. {nombreProducto[0].capitalize()} - ({disponibleProducto}) - ${producto[1][0][1]}\n"
        opcionesProductos += f"{len(productos)+1}. Volver al menú anterior\n"

        while True:
            print(opcionesProductos)
            preguntaProducto = input("¿Qué producto deseas modificar? Ingresa el número correspondiente: ")
            if preguntaProducto.isdigit() and int(preguntaProducto) > 0 and int(preguntaProducto) <= len(productos):
                productoSeleccionado = list(productos.items())[int(preguntaProducto)-1]
                opcionesModificacion = "1. Cambiar precio\n2. Eliminar producto\n3. Volver al menú anterior\n"
                print(f"Seleccionaste el producto {productoSeleccionado[1][0][0].capitalize()} ({'disponible' if productoSeleccionado[1][1] else 'no disponible'})")

                while True:
                    preguntaModificacion = input(f"{opcionesModificacion}¿Qué deseas modificar? Ingresa el número correspondiente: ")
                    if preguntaModificacion == "1":
                        nuevoPrecio = input("Ingresa el nuevo precio del producto: ")
                        while not nuevoPrecio.isdigit():
                            nuevoPrecio = input("Valor inválido. Ingresa un número válido: ")
                        productoSeleccionado[1][0][1] = int(nuevoPrecio)
                        print(f"El precio del producto {productoSeleccionado[1][0][0].capitalize()} se ha actualizado a {nuevoPrecio}.")
                        break
                    elif preguntaModificacion == "2":
                        productoSeleccionado[1][1] = False
                        productoSeleccionado[1][2] = "- No se encuentra habilitado"
                        print(f"El producto {productoSeleccionado[1][0][0].capitalize()} ha sido eliminado.")
                        break
                    elif preguntaModificacion == "3":
                        break
                    else:
                        print("Opción inválida. Ingresa un número correspondiente a una opción válida.")
            elif preguntaProducto == str(len(productos)+1):
                break
            else:
                print("Opción inválida. Ingresa un número correspondiente a una opción válida.")

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
                                                
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "2":
                                                productos = tamaños_conos
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "3":
                                                productos = tamaños_granizados
                                                modificarProducto(productos)        
                                                break
                                            elif preguntaCategoria == "4":
                                                productos = tamaños_copas_infantiles
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "5":
                                                productos = tamaños_malteadas
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "6":
                                                productos = tamaños_litro_helado
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "7":
                                                productos = tamaños_ensalada_frutas
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "8":
                                                productos = tamaños_fresas
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "9":
                                                productos = tamaños_copas
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "10":
                                                productos = tamaños_banana_split
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "11":
                                                productos = tamaños_brownie
                                                modificarProducto(productos)
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
                                                            modificarProductosSubcategoria(subcategorias_nuevas[int(preguntaSubCategoria)][3])
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
                agregarUsuario()
                break
            else:
                print("Ingresa una opción valida")
