# librería para verificar si un input es un correo
import re

# Librería para hacer un cronometro al momento de crear la factura
import time

# Librería para convertir una función asíncrona y poder seguir ejecutando el código
import threading

# Librería Fecha
import datetime

fecha_actual = datetime.date.today()

fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

# [correo,contraseña,rol,[nombre,documento,activo o no activo]]
usuarios = [    ["admin@email.com", "admin123", "admin", ["", "", True, "", ""]],
    ["cajero1@email.com", "cajero1", "cajero", ["prueba", "123456789", True, "", ""]],
    ["cajero2@email.com", "cajero2", "cajero", ["prueba2", "1234567891", True, "", ""]],
    ["angel@gmail.com", "contra", "usuario", ["angel", "123456789", True, "3144098545", "Mz A lote 1"], 0],
    ["keiner@gmail.com", "contra", "usuario", ["angel", "1234567893", True, "3222244572", "Mz A lote 1"], 0]
]

# Afuera de todo el código
facturas = [
    [
        1,
        "keiner@gmail.com",
        "21/03/2023",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir sin helado",
            "sabor": ["Ensalada de frutas sin helado"],
            "precio": 10200,
        },"caja",
        {"Total": 10200},
    ],
    [
        2,
        "Andres",
        "26/03/2023",
        {
            "tipo": "Fresas",
            "tamaño": "Fresas con helado",
            "sabor": ["vainilla chips"],
            "precio": 8400,
        },"caja",
        {"Total": 8400},
    ],
    [
        3,
        "Felipe",
        "21/03/2023",
        {
            "tipo": "Granizados",
            "tamaño": "Granizado 16 onz",
            "sabor": ["fresa"],
            "precio": 8400,
        },"online",
        {"Total": 8400},
    ],
    [
        4,
        "Felipe",
        "12/01/2023",
        {
            "tipo": "Banana split",
            "tamaño": "Banana split",
            "sabor": ["fresa", "ron con pasas"],
            "precio": 13200,
        },"onlinecaja",
        {"Total": 13200},
    ],
    [
        5,
        "Felipe",
        "10/04/2023",
        {
            "tipo": "Banana split",
            "tamaño": "Banana split",
            "sabor": ["fresa", "ron con pasas"],
            "precio": 13200,
        },"caja",
        {"Total": 13200},
    ],
    [
        6,
        "Andres",
        "12/08/2019",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir con helado",
            "sabor": ["vainilla chips", "tropical de agua"],
            "precio": 14500,
        },"online",
        {"Total": 14500},
    ],
    [
        7,
        "Andres",
        "12/08/2019",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir con helado",
            "sabor": ["vainilla chips", "tropical de agua"],
            "precio": 14500,
        },"caja",
        {"Total": 14500},
    ],
    [
        8,
        "Tomas",
        "12/03/2021",
        {
            "tipo": "Vasos",
            "tamaño": "Doble",
            "sabor": ["vainilla chips", "cereza"],
            "precio": 8400,
        },
        {
            "tipo": "Litro de helado",
            "tamaño": "Litro de helado",
            "sabor": ["vainilla chips"],
            "precio": 27000,
        },"caja",
        {"Total": 35400},
    ],
    [
        9,
        "Andres",
        "19/04/2022",
        {
            "tipo": "Copas infantiles",
            "tamaño": "Fiesta",
            "sabor": ["maracuya en leche", "nata"],
            "precio": 8800,
        },"online",
        {"Total": 8800},
    ],
    [
        10,
        "Felipe",
        "18/02/2023",
        {
            "tipo": " Malteadas",
            "tamaño": "Malteada 12 onz",
            "sabor": ["maracuya en leche"],
            "precio": 6400,
        },"onlinecaja",
        {"Total": 6400},
    ],
    [
        11,
        "Tomas",
        "25/03/2023",
        {
            "tipo": "Banana split",
            "tamaño": "Banana split",
            "sabor": ["frutos rojos", "chicle"],
            "precio": 13200,
        },"caja",
        {"Total": 13200},
    ],
    [
        12,
        "Tomas",
        "01/01/2021",
        {
            "tipo": "Copas infantiles",
            "tamaño": "piñata",
            "sabor": ["crocante"],
            "precio": 10800,
        },"online",
        {"Total": 10800},
    ],
    [
        13,
        "Tomas",
        "06/04/2022",
        {
            "tipo": "Granizados",
            "tamaño": "Granizado 16 onz",
            "sabor": ["fresa"],
            "precio": 8400,
        },"caja",
        {"Total": 8400},
    ],
    [
        14,
        "Felipe",
        "30/04/2022",
        {
            "tipo": "Ensalada de frutas",
            "tamaño": "para compartir con helado",
            "sabor": ["tropical de agua", "maracuya en agua"],
            "precio": 14500,
        },"online",
        {"Total": 14500},
    ],
    [
        15,
        "Andres",
        "12/02/2023",
        {
            "tipo": "Conos",
            "tamaño": "Doble",
            "sabor": ["maracuya en agua", "tropical de agua"],
            "precio": 8400,
        },"onlinecaja",
        {"Total": 8400},
    ],
]
facturasFinalizadas=[]
facturasPendientes=[]
facturasCreadas=[]

# Para indicar el numero de la factura
contador_general = len(facturas) + 1

# Se debe poner estos 3 datos en la parte antes del código de ingresar compra
total = 0
# Solo tiene los productos factura temporal
factura_temporal = []
Factura_unica = []

# Extras

sabores = {
    "1": "maracuya en agua",
    "2": "tropical de agua",
    "3": "chicle",
    "4": "frutos rojos",
    "5": "arequipe",
    "6": "nata",
    "7": "crocante",
    "8": "maracuya en leche",
    "9": "caramelo",
    "10": "cereza",
    "11": "fresa",
    "12": "vainilla chips",
    "13": "brownie",
    "14": "galleta oreo",
    "15": "leche klim",
    "16": "chocolate",
    "17": "MyM",
    "18": "queso",
    "19": "vainilla",
    "20": "ron con pasas",
    "21": "nucita",
    "22": "stracciatella",
}

granizados = {
    "1": "frutos rojos",
    "2": "naranja",
    "3": "mango",
    "4": "fresa",
    "5": "cereza",
}

tipos = {
    "1": "Vasos",
    "2": "Conos",
    "3": "Granizados",
    "4": "Copas infantiles",
    "5": " Malteadas",
    "6": "Litro de helado",
    "7": "Ensalada de frutas",
    "8": "Fresas",
    "9": "Copas",
    "10": "Banana split",
    "11": "Brownie con helado",
    "12": "Paletas",
    "13": "Nuevos productos",
}

# ----------------------------------------------------------------Productos----------------------------------------------------------------
tipos2 = {
    "1": ["Vasos", True, ""],
    "2": ["Conos", True, ""],
    "3": ["Granizados", True, ""],
    "4": ["Copas infantiles", True, ""],
    "5": ["Malteadas", True, ""],
    "6": ["Litro de helado", True, ""],
    "7": ["Ensalada de frutas", True, ""],
    "8": ["Fresas", True, ""],
    "9": ["Copas", True, ""],
    "10": ["Banana split", True, ""],
    "11": ["Brownie con helado", True, ""],
    "12": ["Paletas", True, ""],
    "13": ["Nuevas Categorias", True, ""],
}
cantidad_productos = len(tipos2) + 1

# 1 = Vasos
tamaños_vasos = {
    "1": [["Sencillo", 5500], True, ""],
    "2": [["Doble", 8400], True, ""],
    "3": [["Triple", 10800], True, ""],
}
cantidad_bolas_vasos = {"Sencillo": 1, "Doble": 2, "Triple": 3}
n_vasos = len(tamaños_vasos) + 1

# 2 = Conos
tamaños_conos = {
    "1": [["Pequeño", 4200], True, ""],
    "2": [["Mediano", 5500], True, ""],
    "3": [["Doble", 8400], True, ""],
    "4": [["Super cono", 10800], True, ""],
    "5": [["Mega cono", 14000], True, ""],
}
n_conos = len(tamaños_conos) + 1
cantidad_bolas_conos = {
    "Pequeño": 1,
    "Mediano": 1,
    "Doble": 2,
    "Super cono": 3,
    "Mega cono": 4,
}

# 3 = Granizados
tamaños_granizados = {
    "1": [["Granizado 12 onz", 6400], True, ""],
    "2": [["Granizado 16 onz", 8400], True, ""],
    "3": [["Salpicon con helado", 9000], True, ""],
    "4": [["Salpicon sin helado", 6300], True, ""],
    "5": [["copa chocolate", 9000], True, ""],
}
n_granizados = len(tamaños_granizados) + 1

# 4 = Copas infantiles
tamaños_copas_infantiles = {
    "1": [["Mickey", 6400], True, ""],
    "2": [["piñata", 10800], True, ""],
    "3": [["Fiesta", 8800], True, ""],
    "4": [["chips", 8800], True, ""],
}
cantidad_bolas_copa_infantil = {
    "Mickey": 1, "piñata": 1, "Fiesta": 2, "chips": 2}

n_infantil = len(tamaños_copas_infantiles) + 1
# 5 = Malteadas
tamaños_malteadas = {
    "1": [["Malteada 12 onz", 10000], True, ""],
    "2": [["Malteada 16 onz", 12000], True, ""],
}
n_malteadas = len(tamaños_malteadas) + 1

# 6 = Litro de helado
tamaños_litro_helado = {"1": [["Litro de helado", 27000], True, ""]}
n_litro_helado = len(tamaños_litro_helado) + 1

# 7 = Ensalada de frutas
tamaños_ensalada_frutas = {
    "1": [["personal", 10800], True, ""],
    "2": [["para compartir sin helado", 10200], True, ""],
    "3": [["para compartir con helado", 14500], True, ""],
}
n_frutas = len(tamaños_ensalada_frutas) + 1

# 8 = Fresas
tamaños_fresas = {
    "1": [["Fresas con crema", 11400], True, ""],
    "2": [["Fresas con helado", 8400], True, ""],
}
n_fresas = len(tamaños_fresas) + 1

# 9 = Copas
tamaños_copas = {
    "1": [["Exotica", 10800], True, ""],
    "2": [["Ron o amaretto", 10800], True, ""],
    "3": [["Caramelo", 10800], True, ""],
    "4": [["Tropical", 10800], True, ""],
    "5": [["Peach melba", 10800], True, ""],
    "6": [["De la casa", 10800], True, ""],
    "7": [["Sundae", 10800], True, ""],
}
n_copas = len(tamaños_copas) + 1
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
tamaños_banana_split = {"1": [["Banana split", 13200], True, ""]}
n_banana = len(tamaños_banana_split) + 1

# 11 = Brownie con helado
tamaños_brownie = {"1": [["Brownie con helado", 13200], True, ""]}
n_brownie = len(tamaños_brownie) + 1

# 12 = Paletas
sabores_paletas = {
    "1": "leche klim",
    "2": "maracuya",
    "3": "fresas con chocolate",
    "4": "MyM",
    "5": "Chantilli",
    "6": "ron con pasas",
    "7": "nucita",
    "8": "frutos rojos",
    "9": "chocomani",
    "10": "oreo",
    "11": "Chocolate",
    "12": "Queso",
}

sabores_paletas_base = {
    "1": [["leche klim", 6000], True, ""],
    "2": [["maracuya", 6000], True, ""],
    "3": [["fresas con chocolate", 6000], True, ""],
    "4": [["MyM", 6000], True, ""],
    "5": [["Chantilli", 6000], True, ""],
    "6": [["ron con pasas", 6000], True, ""],
    "7": [["nucita", 6000], True, ""],
    "8": [["frutos rojos", 6000], True, ""],
    "9": [["chocomani", 6000], True, ""],
    "10": [["oreo", 6000], True, ""],
    "11": [["chocolate", 6000], True, ""],
    "12": [["queso", 6000], True, ""],
}
n_paletas = len(sabores_paletas_base) + 1

# 13 SubCategorias Nuevas

subcategorias_nuevas = {
    1: [
        "galletas",
        True,
        "",
        {
            "1": [["Exotica", 10800], True, ""],
            "2": [["Ron o amaretto", 10800], True, ""],
        },
    ],
    2: ["sancocho", True, "", {}],
}
n_subcategorias= len(subcategorias_nuevas)+1

# ----------------------------------------------------------------Fin de productos----------------------------------------------------------------

def agregarFactura(factura):
    facturasCreadas.append(factura)
    numFactura=factura[0]
    time.sleep(5)
    print("se empezo a producir el pedido")
    for i,f in enumerate(facturasCreadas):
        if f[0]==numFactura:
            facturasPendientes.append(f)
            del facturasCreadas[i]
            break
    

def filtrar_por_mes_y_anio(facturas, mes, anio):
    facturas_filtradas = []
    for factura in facturas:
        fecha = datetime.datetime.strptime(factura[2], "%d/%m/%Y")
        mes_factura = fecha.strftime("%m")
        anio_factura = fecha.strftime("%Y")
        if mes_factura == mes and anio_factura == anio:
            facturas_filtradas.append(factura)
    return facturas_filtradas


def validar_opcion(num_inicio, num_fin, pregunta):
    while True:
        opcion = input(pregunta)
        if opcion.isdigit():
            opcion = int(opcion)
            if num_inicio <= opcion <= num_fin:
                return str(opcion)
        print("Por favor ingresa una opción válida entre",
              num_inicio, "y", num_fin)


def Sabor_helados():
    sabores = {
        "1": "maracuya en agua",
        "2": "tropical de agua",
        "3": "chicle",
        "4": "frutos rojos",
        "5": "arequipe",
        "6": "nata",
        "7": "crocante",
        "8": "maracuya en leche",
        "9": "caramelo",
        "10": "cereza",
        "11": "fresa",
        "12": "vainilla chips",
        "13": "brownie",
        "14": "galleta oreo",
        "15": "leche klim",
        "16": "chocolate",
        "17": "MyM",
        "18": "queso",
        "19": "vainilla",
        "20": "ron con pasas",
        "21": "nucita",
        "22": "stracciatella",
    }

    cont = 1
    for i in sabores:
        h = print(cont, sabores[i])
        cont += 1
    return h


def Sabor_paletas():
    sabores = {
        "1": "leche klim",
        "2": "maracuya",
        "3": "fresas con chocolate",
        "4": "MyM",
        "5": "Chantilli",
        "6": "ron con pasas",
        "7": "nucita",
        "8": "frutos rojos",
        "9": "chocomani",
        "10": "oreo",
        "11": "Chocolate",
        "12": "Queso",
    }

    cont = 1
    for i in sabores:
        h = print(cont, sabores[i])
        cont += 1
    return h


def validarCorreo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, correo))


def agregarUsuario():
    while True:
        while True:
            while True:
                nuevo_usuario = input("Ingresa tu correo: ").strip()
                if validarCorreo(nuevo_usuario) == True:
                    break
                print("Correo inválido, inténtalo de nuevo.")

            correo_existe = False
            for i in usuarios:
                if i[0] == nuevo_usuario:
                    correo_existe = True
                    break

            if correo_existe:
                print("El usuario ya existe. Por favor ingresa un correo diferente.")
                continue
            else:
                break
        nombre = input("Ingrese su nombre: ").strip()
        while True:
            documento = input("Ingrese su documento: ").strip()
            if documento.isdigit() and (len(documento) == 8 or len(documento) == 10 or len(documento) == 9):
                documento_existe = False
                for i in usuarios:
                    for j in range(len(i[3])):
                        if i[3][1] == documento:
                            documento_existe = True
                            break
                if documento_existe:
                    print(
                        "El documento ya existe. Por favor ingresa un documento diferente.")
                    continue
                else:
                    break
            else:
                print("Documento inválido. Debe ser un número entero de 8 o 10 dígitos.")
        while True:
            telefono = input("Ingrese su teléfono: ").strip()
            if telefono.isdigit() and (len(telefono) == 10):
                if telefono in [usuario_info[3][3] for usuario_info in usuarios]:
                    print("El número ya esta registrado") 
                else:   
                    break
            else:
                print("Número inválido. Debe ser un número entero de 10 dígitos.")

        direccion = input("Ingrese su dirección: ").strip()
        contraseña = input("Ingrese una contraseña: ").strip()
        usuarios.append([nuevo_usuario, contraseña, "usuario", [
                        nombre, documento, True, telefono, direccion],0])
        print("Usuario Creado exitosamente, ahora puedes iniciar sesión")
        break


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

        seleccion = input(
            "Ingrese el número correspondiente al producto que desea modificar: "
        )

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion >= 1 and seleccion <= len(productos):
                nombre_producto = list(productos.keys())[seleccion - 1]
                print(
                    f"Actualmente el producto '{productos[nombre_producto][0][0]}' tiene el siguiente precio:"
                )
                print(f"Precio: {productos[nombre_producto][0][1]}")
                while True:
                    opcion = input(
                        "1. Precio\n2. Eliminar Producto\n3. Volver al menu anterior\n¿Qué deseas modificar?: "
                    )
                    if opcion == "1":
                        while True:
                            nuevo_precio = input(
                                "Ingresa el nuevo precio del producto: "
                            )
                            if nuevo_precio.isdigit():
                                productos[nombre_producto][0][1] = int(
                                    nuevo_precio)
                                print(
                                    f"El precio del producto '{productos[nombre_producto][0][0]}' ha sido actualizado a {nuevo_precio}."
                                )
                                break
                            else:
                                print("Error: el precio debe ser un número entero.")
                        break
                    elif opcion == "2":
                        productos[nombre_producto][1] = False
                        productos[nombre_producto][2] = "- No se encuentra habilitado"
                        print(
                            f"el producto '{productos[nombre_producto][0][0]}' ha sido eliminado"
                        )
                        break
                    elif opcion == "3":
                        break
                    else:
                        print("Opción inválida. Por favor, ingresa 1 o 2.")
            elif seleccion == len(productos) + 1:
                break
            else:
                print(
                    f"El número de producto '{seleccion}' no es válido. Por favor, ingresa un número válido."
                )
        else:
            print(
                f"La opción ingresada '{seleccion}' no es válida. Por favor, ingresa una opción válida."
            )

def realizarPedidoSubcategoria(productos):
    productosSeleccionados = []

    while True:
        opcionesProductos = ""
        for i, producto in enumerate(productos.items()):
            nombreProducto = producto[1][0]
            disponibleProducto = "disponible" if producto[1][1] else "no disponible"
            opcionesProductos += f"{i+1}. {nombreProducto[0].capitalize()} - ({disponibleProducto}) - ${producto[1][0][1]}\n"
        opcionesProductos += f"{len(productos)+1}. Finalizar pedido\n"

        print(opcionesProductos)
        preguntaProducto = input(
            "¿Qué producto deseas agregar al pedido? Ingresa el número correspondiente: "
        )

        if (
            preguntaProducto.isdigit()
            and int(preguntaProducto) > 0
            and int(preguntaProducto) <= len(productos)
        ):
            productoSeleccionado = list(productos.items())[int(preguntaProducto) - 1]
            print(productoSeleccionado)
            if productoSeleccionado[1][1]:
                productosSeleccionados.append(productoSeleccionado)
                print(
                    f"Se ha agregado {productoSeleccionado[1][0][0].capitalize()} al pedido."
                )
            else:
                print("Lo siento, el producto no está disponible.")
        elif preguntaProducto == str(len(productos) + 1):
            break
        else:
            print(
                "Opción inválida. Ingresa un número correspondiente a una opción válida."
            )



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
            preguntaProducto = input(
                "¿Qué producto deseas modificar? Ingresa el número correspondiente: "
            )
            if (
                preguntaProducto.isdigit()
                and int(preguntaProducto) > 0
                and int(preguntaProducto) <= len(productos)
            ):
                productoSeleccionado = list(productos.items())[
                    int(preguntaProducto) - 1
                ]
                opcionesModificacion = "1. Cambiar precio\n2. Eliminar producto\n3. Volver al menú anterior\n"
                print(
                    f"Seleccionaste el producto {productoSeleccionado[1][0][0].capitalize()} ({'disponible' if productoSeleccionado[1][1] else 'no disponible'})"
                )

                while True:
                    preguntaModificacion = input(
                        f"{opcionesModificacion}¿Qué deseas modificar? Ingresa el número correspondiente: "
                    )
                    if preguntaModificacion == "1":
                        nuevoPrecio = input(
                            "Ingresa el nuevo precio del producto: ")
                        while not nuevoPrecio.isdigit():
                            nuevoPrecio = input(
                                "Valor inválido. Ingresa un número válido: "
                            )
                        productoSeleccionado[1][0][1] = int(nuevoPrecio)
                        print(
                            f"El precio del producto {productoSeleccionado[1][0][0].capitalize()} se ha actualizado a {nuevoPrecio}."
                        )
                        break
                    elif preguntaModificacion == "2":
                        productoSeleccionado[1][1] = False
                        productoSeleccionado[1][2] = "- No se encuentra habilitado"
                        print(
                            f"El producto {productoSeleccionado[1][0][0].capitalize()} ha sido eliminado."
                        )
                        break
                    elif preguntaModificacion == "3":
                        break
                    else:
                        print(
                            "Opción inválida. Ingresa un número correspondiente a una opción válida."
                        )
            elif preguntaProducto == str(len(productos) + 1):
                break
            else:
                print(
                    "Opción inválida. Ingresa un número correspondiente a una opción válida."
                )


while True:
    usuario = input("Ingrese usuario: ").strip()
    contraseña = input("Ingrese contraseña: ").strip()
    encontrado = False
    habilitado=False
    for i in usuarios:
        for j in range(len(i[3])):
            if i[0] == usuario and i[1] == contraseña and i[3][2]:
                habilitado = True
    for i in usuarios:
        if i[0] == usuario and i[1] == contraseña and habilitado==True:
            encontrado = True
            correoUsuario = usuario
            if i[2] == "admin":
                while True:
                    preguntaAdmin = input(
                        "1. Cajeros\n2. Productos\n3. Ventas\n4. Salir del programa\nSelecciona una opción: "
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
                                    if usuario[2]=="cajero":
                                        print(usuario)
                                break
                            elif preguntaCajero == "5":
                                break
                            else:
                                print("Ingresa un numero valido")
                    elif preguntaAdmin == "2":
                        while True:
                            preguntaCajero = input(
                                "1. Ver Productos\n2. Modificar Productos\n3. Agregar Productos\n4. Volver al menu anterior\nSeleccione una opción: "
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
                                    opciones += (
                                        f"{len(categoriasHabilitadas)+1}. Volver al menu anterior")
                                    preguntaCategoria = input(
                                        opciones + "Elige una opción: "
                                    )
                                    if preguntaCategoria == str(len(categoriasHabilitadas)+1):
                                        break
                                    else:
                                        if preguntaCategoria.isdigit() and int(preguntaCategoria) in range(1, cont + 1):
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
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "2":
                                                    productos = tamaños_conos
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "3":
                                                    productos = tamaños_granizados
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "4":
                                                    productos = tamaños_copas_infantiles
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "5":
                                                    productos = tamaños_malteadas
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "6":
                                                    productos = tamaños_litro_helado
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "7":
                                                    productos = tamaños_ensalada_frutas
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "8":
                                                    productos = tamaños_fresas
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "9":
                                                    productos = tamaños_copas
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "10":
                                                    productos = tamaños_banana_split
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "11":
                                                    productos = tamaños_brownie
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "12":
                                                    productos = sabores_paletas_base
                                                    for i in productos:
                                                        print(
                                                            productos[i][0], productos[i][2]
                                                        )
                                                    break
                                                elif preguntaCategoria == "13":
                                                    if len(subcategorias_nuevas) == 0:
                                                        print(
                                                            "Esta categoría no tiene productos"
                                                        )
                                                    else:
                                                        contSubCategoria = 1
                                                        subcategoriasHabilitadas = []
                                                        opcionesSubcategorias = ""
                                                        for i in subcategorias_nuevas:
                                                            subcategoriasHabilitadas.append(
                                                                [
                                                                    subcategorias_nuevas[i][
                                                                        0
                                                                    ]
                                                                    + " "
                                                                    + subcategorias_nuevas[
                                                                        i
                                                                    ][2]
                                                                ]
                                                            )
                                                            contSubCategoria += 1
                                                        for i, subCategoria in enumerate(
                                                            subcategoriasHabilitadas
                                                        ):
                                                            nombreSubCategoria = (
                                                                subCategoria[0]
                                                            )
                                                            opcionesSubcategorias += f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                                        preguntaSubCategoria = input(
                                                            opcionesSubcategorias
                                                            + "Elige una opción: "
                                                        )
                                                        if (
                                                            preguntaSubCategoria.isdigit()
                                                            and int(preguntaSubCategoria)
                                                            > 0
                                                            and int(preguntaSubCategoria)
                                                            <= len(subcategoriasHabilitadas)
                                                        ):
                                                            if (
                                                                len(
                                                                    subcategorias_nuevas[
                                                                        int(
                                                                            preguntaSubCategoria
                                                                        )
                                                                    ][3]
                                                                )
                                                                == 0
                                                            ):
                                                                print(
                                                                    "Esta subcategoria no tiene productos"
                                                                )
                                                            else:
                                                                if (
                                                                    subcategorias_nuevas[
                                                                        int(
                                                                            preguntaSubCategoria
                                                                        )
                                                                    ][1]
                                                                    == True
                                                                ):
                                                                    for (
                                                                        i
                                                                    ) in subcategorias_nuevas[
                                                                        int(
                                                                            preguntaSubCategoria
                                                                        )
                                                                    ][
                                                                        3
                                                                    ]:
                                                                        print(
                                                                            subcategorias_nuevas[
                                                                                int(
                                                                                    preguntaSubCategoria
                                                                                )
                                                                            ][
                                                                                3
                                                                            ][
                                                                                i
                                                                            ][
                                                                                0
                                                                            ],
                                                                            " ",
                                                                            subcategorias_nuevas[
                                                                                int(
                                                                                    preguntaSubCategoria
                                                                                )
                                                                            ][
                                                                                3
                                                                            ][
                                                                                i
                                                                            ][
                                                                                2
                                                                            ],
                                                                        )
                                                                else:
                                                                    print(
                                                                        "Esta subcategoría se encuentra deshabilitada"
                                                                    )
                                                        else:
                                                            print(
                                                                "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                                            )

                                                    break
                                                elif preguntaCategoria == len(categoriasHabilitadas)+1:
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
                                                productos = sabores_paletas_base
                                                modificarProducto(productos)
                                                break
                                            elif preguntaCategoria == "13":
                                                if len(subcategorias_nuevas) == 0:
                                                    print(
                                                        "Esta categoría no tiene productos"
                                                    )
                                                else:
                                                    contSubCategoria = 1
                                                    subcategoriasHabilitadas = []
                                                    opcionesSubcategorias = ""
                                                    for i in subcategorias_nuevas:
                                                        subcategoriasHabilitadas.append(
                                                            [
                                                                subcategorias_nuevas[i][
                                                                    0
                                                                ]
                                                                + " "
                                                                + subcategorias_nuevas[
                                                                    i
                                                                ][2]
                                                            ]
                                                        )
                                                        contSubCategoria += 1
                                                    for i, subCategoria in enumerate(
                                                        subcategoriasHabilitadas
                                                    ):
                                                        nombreSubCategoria = (
                                                            subCategoria[0]
                                                        )
                                                        opcionesSubcategorias += f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                                    preguntaSubCategoria = input(
                                                        opcionesSubcategorias
                                                        + "Elige una opción: "
                                                    )
                                                    if (
                                                        preguntaSubCategoria.isdigit()
                                                        and int(preguntaSubCategoria)
                                                        > 0
                                                        and int(preguntaSubCategoria)
                                                        <= len(subcategoriasHabilitadas)
                                                    ):
                                                        if (
                                                            len(
                                                                subcategorias_nuevas[
                                                                    int(
                                                                        preguntaSubCategoria
                                                                    )
                                                                ][3]
                                                            )
                                                            == 0
                                                        ):
                                                            print(
                                                                "Esta subcategoria no tiene productos"
                                                            )
                                                        else:
                                                            modificarProductosSubcategoria(
                                                                subcategorias_nuevas[
                                                                    int(
                                                                        preguntaSubCategoria
                                                                    )
                                                                ][3]
                                                            )
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
                            elif preguntaCajero == "3":
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
                                    opciones += (
                                        f"{len(categoriasHabilitadas)+1}. Volver al menu anterior\n")
                                    preguntaCategoria = input(
                                        opciones + "Elige una opción: "
                                    )
                                    if preguntaCategoria == str(len(categoriasHabilitadas)+1):
                                        break
                                    else:
                                        if preguntaCategoria.isdigit() and int(preguntaCategoria) in range(1, cont + 1):
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
                                                    # productos = tamaños_vasos
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de vaso deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_vasos[str(n_vasos)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    cantidadBolas = input(
                                                        "¿Cuantas bolas de helado tendra ese tamaño?: ")
                                                    cantidad_bolas_vasos[preguntaNuevoProducto] = cantidadBolas
                                                    break
                                                elif preguntaCategoria == "2":
                                                    # productos = tamaños_conos
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de cono deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_conos[str(n_conos)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    cantidadBolas = input(
                                                        "¿Cuantas bolas de helado tendra ese tamaño?: ")
                                                    cantidad_bolas_conos[preguntaNuevoProducto] = cantidadBolas
                                                    break
                                                elif preguntaCategoria == "3":
                                                    # productos = tamaños_granizados
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de granizado deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_granizados[str(n_granizados)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "4":
                                                    # productos = tamaños_copas_infantiles
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de copa infantil deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_copas_infantiles[str(n_infantil)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    cantidadBolas = input(
                                                        "¿Cuantas bolas de helado tendra ese tamaño?: ")
                                                    cantidad_bolas_copa_infantil[preguntaNuevoProducto] = cantidadBolas
                                                    break
                                                elif preguntaCategoria == "5":
                                                    # productos = tamaños_malteadas
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de malteada deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_malteadas[str(n_malteadas)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "6":
                                                    # productos = tamaños_litro_helado
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de helado deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_litro_helado[str(n_litro_helado)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "7":
                                                    # productos = tamaños_ensalada_frutas
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de ensalada de frutas deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_ensalada_frutas[str(n_frutas)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "8":
                                                    # productos = tamaños_fresas
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de fresas deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_fresas[str(n_fresas)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "9":
                                                    # productos = tamaños_copas
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de copa deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_copas[str(n_copas)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    cantidadBolas = input(
                                                        "¿Cuantas bolas de helado tendrá ese tamaño?: ")
                                                    cantidad_bolas[preguntaNuevoProducto] = cantidadBolas
                                                    break
                                                elif preguntaCategoria == "10":
                                                    # productos = tamaños_banana_split
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tamaño de banana split deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_banana_split[str(n_banana)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "11":
                                                    # productos = tamaños_brownie
                                                    preguntaNuevoProducto = input(
                                                        "¿Que tipo de brownie deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    tamaños_brownie[str(n_brownie)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "12":
                                                    # productos = sabores_paletas_base
                                                    preguntaNuevoProducto = input(
                                                        "¿Que sabor de paleta deseas agregar?: ")
                                                    precio = input(
                                                        "Ingresa el precio del producto nuevo: ")
                                                    sabores_paletas_base[str(n_paletas)] = [
                                                        [preguntaNuevoProducto, precio], True, ""]
                                                    break
                                                elif preguntaCategoria == "13":
                                                    contSubCategoria = 1
                                                    subcategoriasHabilitadas = []
                                                    opcionesSubcategorias = ""
                                                    for i in subcategorias_nuevas:
                                                        subcategoriasHabilitadas.append(
                                                            [
                                                                subcategorias_nuevas[i][
                                                                    0
                                                                ]
                                                                + " "
                                                                + subcategorias_nuevas[
                                                                    i
                                                                ][2]
                                                            ]
                                                        )
                                                        contSubCategoria += 1
                                                    for i, subCategoria in enumerate(
                                                        subcategoriasHabilitadas
                                                    ):
                                                        nombreSubCategoria = (
                                                            subCategoria[0]
                                                        )
                                                        opcionesSubcategorias += f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                                    opcionesSubcategorias+= f"{contSubCategoria}. Crear nueva categoria\n"
                                                    opcionesSubcategorias+= f"{contSubCategoria+1}. Volver al menu anterior\n"
                                                    preguntaSubCategoria = input(
                                                        opcionesSubcategorias
                                                        + "Elige una opción: "
                                                    )
                                                    if preguntaSubCategoria.isdigit() and int(preguntaSubCategoria)==contSubCategoria+1:
                                                        break
                                                    else:
                                                        if (
                                                            preguntaSubCategoria.isdigit()
                                                            and int(preguntaSubCategoria)
                                                            > 0
                                                            and int(preguntaSubCategoria)
                                                            <= (len(subcategoriasHabilitadas)+1)
                                                        ):
                                                            if preguntaSubCategoria==str(contSubCategoria):
                                                                nuevaCategoria=input("Ingresa el nombre de la nueva categoria: ")
                                                                cont=1
                                                                productos={}
                                                                while True:
                                                                    while True:
                                                                        nuevoProducto = input(f"Ingresa el nombre del nuevo producto para la categoria {nuevaCategoria}: ")
                                                                        if nuevoProducto.strip()=="":
                                                                            print("El producto no puede estar vació")
                                                                        else:
                                                                            break
                                                                    while True:
                                                                        precioProducto = input(f"Ingresa el precio del producto {nuevoProducto}: ")
                                                                        if precioProducto.isdigit():
                                                                            break
                                                                        else:
                                                                            print("El precio ingresado debe contener solo números. Por favor, inténtalo de nuevo.")
                                                                    productos[cont] = [[nuevoProducto, int(precioProducto)], True, ""]
                                                                    cont += 1
                                                                    while True:
                                                                        preguntaNuevoProducto = input("1. Si\n2. No\n¿Quieres agregar otro producto?: ").strip()
                                                                        if preguntaNuevoProducto == "1":
                                                                            print("Producto agregado con éxito, ahora ingresa otro producto:")
                                                                            break
                                                                        elif preguntaNuevoProducto == "2":
                                                                            break
                                                                        else:
                                                                            print("Ingresa una opción válida (1 o 2)")
                                                                    if preguntaNuevoProducto == "2":
                                                                        break
                                                                subcategorias_nuevas[n_subcategorias]=[nuevaCategoria,True,"",productos]
                                                            else:
                                                                # productos=subcategorias_nuevas[int(preguntaSubCategoria)][3]
                                                                while True:
                                                                    n_productos=len(subcategorias_nuevas[int(preguntaSubCategoria)][3])+1
                                                                    while True:
                                                                        nuevoProducto=input("Ingresa el nombre del nuevo producto: ")
                                                                        if nuevoProducto.strip()=="":
                                                                            print("El producto no puede estar vació")
                                                                        else:
                                                                            break
                                                                    while True:
                                                                        precioProducto=input(f"Ingresa el precio del producto {nuevoProducto}: ")
                                                                        if precioProducto.isdigit():  # Validación de que el precio ingresado contiene solo dígitos
                                                                            break
                                                                        else:
                                                                            print("El precio ingresado debe contener solo números. Por favor, inténtalo de nuevo.")
                                                                    subcategorias_nuevas[int(preguntaSubCategoria)][3][n_productos]=[[nuevoProducto, int(precioProducto)], True, ""]
                                                                    while True:
                                                                        preguntaNuevoProducto=input("1. Si\n2. No\n¿Quieres agregar otro producto?: ").strip()
                                                                        if preguntaNuevoProducto=="1":
                                                                            print("producto agregado con éxito, ahora ingresa otro producto:")
                                                                            break
                                                                        elif preguntaNuevoProducto=="2":
                                                                            break
                                                                        else:
                                                                            print("Ingresa una opcion valida")
                                                                    if preguntaNuevoProducto=="2":
                                                                        break 
                                                        else:
                                                            print(
                                                                "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                                            )

                                                elif preguntaCategoria == len(categoriasHabilitadas)+1:
                                                    break
                                                break
                                        else:
                                            print(
                                                "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                            )
                                        break
                            elif preguntaCajero == "4":
                                break
                            else:
                                print("Ingresa un numero valido")
                    elif preguntaAdmin == "3":
                        while True:
                            imprimirFactura=input("Buenas tardes, que deseas hacer: 1. Imprimir todas las facturas; 2. Imprimir las facturas de una fecha especifica o 3. Imprimir las facturas de un cajero especifico o 4. Salir:   ")
                            while imprimirFactura not in ["1", "2", "3", "4"]:
                                    print("Valor incorrecto. Por favor, ingrese 1, 2, 3 o 4.")
                                    imprimirFactura=input("Buenas tardes, que deseas hacer: 1. Imprimir todas las facturas; 2. Imprimir las facturas de una fecha especifica o 3. Imprimir las facturas de un cajero especifico o 4. Salir: ")
                            if imprimirFactura=="1":
                                for factura in facturas:  
                                        print("N°Factura: ", factura[0])
                                        print("Nombre: ", factura[1])
                                        print("Fecha: ", factura[2])
                                        print("Detalles: ", factura[3])
                                        print("Tipo de pago: ", factura[4])
                                        print("Total: ",factura[-1]["Total"])
                                        print("--------------")

                            elif imprimirFactura=="2":
                                mesofecha=input("1.Quiere las facturas del mes o 2.Quiere las facturas de una fecha especifica o 3. Volver: ")
                                while mesofecha not in ["1", "2", "3"]:
                                    print("Valor incorrecto. Por favor, ingrese 1, 2 o 3.")
                                    mesofecha = input("1. Quiere las facturas del mes o 2. Quiere las facturas de una fecha específica o 3, Volver: ")
                                if mesofecha=="1":
                                   fecha_actual = datetime.datetime.now()
                                   r=1
                                   while r==1:
                                        mes_anio = input("Por favor, ingresa el mes y el año (mes/año): ")
                                        if '/' not in mes_anio:
                                            print("Formato incorrecto. Por favor, ingresa la fecha en el formato mes/año.")
                                            continue
                                        if mes_anio.count('/') != 1:
                                            print("Formato incorrecto. Por favor, ingresa la fecha en el formato mes/año.")
                                            continue
                                        
                                        mes, anio = mes_anio.split('/')

                                        if not mes.isdigit() or int(mes) < 1 or int(mes) > 12:
                                            print("El mes ingresado no es válido. Por favor, ingresa un mes válido (01 a 12).")
                                            continue
                                        
                                        if int(anio) > fecha_actual.year or (int(anio) == fecha_actual.year and int(mes) > fecha_actual.month):
                                            print("La fecha ingresada es futura. Por favor, ingresa una fecha válida.")
                                        else:
                                            facturas_filtradas = filtrar_por_mes_y_anio(facturas, mes, anio)

                                            if len(facturas_filtradas) > 0:
                                                print("Facturas encontradas para el mes {} y año {}: ".format(mes, anio))
                                                for factura in facturas_filtradas:
                                                    print("N°Factura: ", factura[0])
                                                    print("Nombre: ", factura[1])
                                                    print("Fecha: ", factura[2])
                                                    print("Detalles: ", factura[3])
                                                    print("Tipo de pago: ", factura[4])
                                                    print("Total: ",factura[-1]["Total"])
                                                    print("--------------")
                                                    r=2
                                            else:
                                                print("No se encontraron facturas para el mes {} y año {}.".format(mes, anio))
                                                break
                                if mesofecha=="2":
                                    while True:
                                        fecha_input = input("Por favor, ingrese una fecha en formato día/mes/año (dd/mm/yyyy): ")
                                        try:
                                            fecha = datetime.datetime.strptime(fecha_input, "%d/%m/%Y")
                                            fecha_actual = datetime.datetime.now()
                                            if fecha > fecha_actual:
                                                print("Error: La fecha ingresada es futura. Intente nuevamente.")
                                            else:
                                                break
                                        except ValueError:
                                            print("Error: Formato de fecha incorrecto. Intente nuevamente.")

                                    print(f"Facturas encontradas para la fecha {fecha_input}:")
                                    facturas_coincidentes = []
                                    for factura in facturas:
                                        if factura[2] == fecha_input:
                                            facturas_coincidentes.append(factura)
                                            print("N°Factura: ", factura[0])
                                            print("Nombre: ", factura[1])
                                            print("Fecha: ", factura[2])
                                            print("Detalles: ", factura[3])
                                            print("Tipo de pago: ", factura[4])
                                            print("Total: ",factura[-1]["Total"])
                                            print("--------------")
                                    if not facturas_coincidentes:
                                        print("No se encontraron facturas para la fecha ingresada.")
                                if mesofecha=="3":
                                    continue
                            elif imprimirFactura=="3":
                                while True:
                                    nombre = input("Ingrese el nombre del cajero a buscar: ")
                                    nombremin=nombre.lower()
                                    cajero_encontrado = False
                                    for factura in facturas:
                                        if factura[1].lower()==nombremin:
                                            cajero_encontrado = True
                                            break
                                        
                                    if cajero_encontrado == True :
                                        break
                                    else:
                                        print("Error: El nombre del cajero no se encuentra en la lista de facturas. Por favor, ingrese un nombre válido.")
                                while cajero_encontrado== True:
                                    opcion = input("¿Qué desea hacer? Ingrese una opción: 1. Imprimir todas las facturas 2. Imprimir las facturas del mes 3. Imprimir las facturas de una fecha específica o 4. Volver: ")
                                    if opcion in ["1", "2", "3", "4"]:
                                        break
                                    else:
                                        print("Opción no válida. Por favor, ingrese 1, 2, 3 o 4.")

                                if opcion == "1":
                                    print("Facturas de", nombre, ":")
                                    for factura in facturas:
                                        if factura[1].lower() == nombremin:
                                            print("N°Factura: ", factura[0])
                                            print("Nombre: ", factura[1])
                                            print("Fecha: ", factura[2])
                                            print("Detalles: ", factura[3])
                                            print("Tipo de pago: ", factura[4])
                                            print("Total: ",factura[-1]["Total"])
                                            print("--------------")
                                elif opcion == "2":
                                    while True:
                                        mes = input("Ingrese el mes en formato mm/yyyy: ")
                                        if len(mes) == 7 and mes[2] == "/" and mes[:2].isdigit() and mes[3:].isdigit() and int(mes[:2]) in range(1, 13):
                                            mes_num = int(mes[:2])
                                            ano_num = int(mes[3:])
                                            fecha_actual = datetime.datetime.now()
                                            if fecha_actual.year < ano_num or (fecha_actual.year == ano_num and fecha_actual.month < mes_num):
                                                print("Error: No se puede ingresar una fecha futura.")
                                            else:
                                                break
                                        else:
                                            print("Formato de mes inválido. Por favor, ingrese el mes en formato mm/yyyy.")
                                    print("Facturas de", nombremin, "del mes", mes, ":")
                                    for factura in facturas:
                                        if factura[1].lower() == nombremin and factura[2][3:] == mes:
                                            print("N°Factura: ", factura[0])
                                            print("Nombre: ", factura[1])
                                            print("Fecha: ", factura[2])
                                            print("Detalles: ", factura[3])
                                            print("Tipo de pago: ", factura[4])
                                            print("Total: ",factura[-1]["Total"])
                                            print("--------------")
                                elif opcion == "3":
                                    fecha_valida = False
                                    while not fecha_valida:
                                        fecha = input("Ingrese la fecha en formato dd/mm/yyyy: ")
                                        try:
                                            fecha_obj = datetime.datetime.strptime(fecha, '%d/%m/%Y')
                                            if fecha_obj > datetime.datetime.now():
                                                print("Fecha no válida. No puede ser una fecha futura.")
                                            else:
                                                fecha_valida = True
                                        except ValueError:
                                            print("Fecha no válida. Debe estar en formato dd/mm/yyyy.")

                                    print("Facturas de", nombremin, "de la fecha", fecha, ":")
                                    for factura in facturas:
                                        if factura[1].lower() == nombremin and factura[2] == fecha:
                                            print("N°Factura: ", factura[0])
                                            print("Nombre: ", factura[1])
                                            print("Fecha: ", factura[2])
                                            print("Detalles: ", factura[3])
                                            print("Tipo de pago: ", factura[4])
                                            print("Total: ",factura[-1]["Total"])
                                            print("--------------")
                                elif opcion=="4":
                                    continue
                            elif imprimirFactura=="4":
                                print("Muchas gracias")
                                break
                    elif preguntaAdmin == "4":
                        break
            elif i[2] == "cajero":
                while True:
                    preguntaCajero=input("1. Ver Pedidos Pendientes\n2. Realiza pedido\n3. Entregar Pedidos\n4. Salir\nSelecciona una opción: ")
                    if preguntaCajero=="1":
                        
                        if len(facturasPendientes)==0:
                            print("No hay pedidos pendientes")
                        else:
                            for factura in facturasPendientes:
                                print("---------------------")
                                print("N°Factura: ", factura[0])
                                print("Nombre: ", factura[1])
                                print("Fecha: ", factura[2])
                                print("Detalles: ", factura[3])
                                print("Tipo de pago: ", factura[4])
                                print("Total: ",factura[-1]["Total"])
                                print("---------------------")

                            while True:
                                preguntaPedido = input("¿Qué factura deseas finalizar? (Ingresa el número de factura o selecciona 0 para volver): ")
                                if preguntaPedido.isdigit():
                                    preguntaPedido = int(preguntaPedido)
                                    if preguntaPedido == 0:
                                        break
                                    else:
                                        encontradoPendiente=False
                                        for facturaP in facturasPendientes:
                                            if facturaP[0]==preguntaPedido:
                                                encontradoPendiente=True
                                        if encontradoPendiente==True:
                                            for i,facturaP in enumerate(facturasPendientes):
                                                if facturaP[0]==preguntaPedido:
                                                    facturasFinalizadas.append(facturasPendientes[i])
                                                    del facturasPendientes[i]
                                                    print("Pedido Completado")
                                            break
                                        else:
                                            print("No se encontró el pedido")
                                else:
                                    print("Ingresa una opción válida")
                    if preguntaCajero=="2":
                        labrando = True
                        while labrando == True:
                            print(
                                "Bienvenid@ a la heladería boquitas, que tipo de producto deseas elegir?"
                            )
                            cont = 1
                            for i in tipos2:
                                print(cont, tipos2[i][0], tipos2[i][2])
                                cont += 1
                            print(cantidad_productos, "para salir")
                            d = validar_opcion(1, cantidad_productos,
                                            "Ingrese el tipo de producto a elegir: ")
                            if d == "1":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la sección de vasos o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aquí:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_vasos:
                                                valor1, valor2 = tamaños_vasos[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_vasos[i][2]
                                                    )
                                                )
                                            print(n_vasos, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_vasos, "Que tamaño deseas elegir:  "
                                            )
                                            if tamaño_h == str(n_vasos):
                                                cent1 = False
                                            else:
                                                tamaño, precio = tamaños_vasos[tamaño_h][0]
                                                if tamaños_vasos[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ del tamaño del vaso o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aquí:  ",
                                                    )
                                                    if d2 == "1":
                                                        cent1 = True
                                                        while cent1 == True:
                                                            tamaño, precio = tamaños_vasos[
                                                                tamaño_h
                                                            ][0]
                                                            bolas = cantidad_bolas_vasos[tamaño]
                                                            sabor_elegido = []
                                                            print("Sabores de helado")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d3 = validar_opcion(
                                                                1,
                                                                3,
                                                                "estas segur@ del sabor de helado? \n1. Estoy segur@ \n2. Quiero cambiar mi sabor de helado \n3. Volver al menu \nIngrese aquí: ",
                                                            )
                                                            if d3 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent3 = False
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aquí: ",
                                                                )
                                                                if d2 == "2":
                                                                    labrando = False
                                                            elif d3 == "3":
                                                                cent1 = False

                                                else:
                                                    print(
                                                        "el siguiente tamaño no esta disponible en este momento:",
                                                        tamaño,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "2":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la sección de conos o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aquí:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_conos:
                                                valor1, valor2 = tamaños_conos[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_conos[i][2]
                                                    )
                                                )
                                            print(n_conos, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_conos, "Que tamaño deseas elegir: "
                                            )
                                            if tamaño_h == str(n_conos):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_conos[tamaño_h][0]
                                                if tamaños_conos[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ del tamaño del cono o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aquí:  ",
                                                    )
                                                    if d2 == "1":
                                                        cent1 = True
                                                        while cent1 == True:
                                                            tamaño_v, precio = tamaños_conos[
                                                                tamaño_h
                                                            ][0]
                                                            bolas = cantidad_bolas_conos[
                                                                tamaño_v
                                                            ]
                                                            sabor_elegido = []
                                                            print("Sabores de helado")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )

                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ del sabor de helado? \n1. Estoy segur@ \n2. Quiero cambiar mi sabor de helado  \nIngrese aquí: ",
                                                            )
                                                            if d3 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent3 = False
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aquí: ",
                                                                )
                                                                if d2 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño no esta disponible en este momento:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "3":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de Granizados o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_granizados:
                                                valor1, valor2 = tamaños_granizados[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_granizados[i][2],
                                                    )
                                                )
                                            print(n_granizados, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_granizados, "Que granizado deseas elegir:"
                                            )
                                            if tamaño_h == str(n_granizados):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_granizados[tamaño_h][
                                                    0
                                                ]
                                                if tamaños_granizados[tamaño_h][1] == True:
                                                    if tamaño_h == "1" or tamaño_h == "2":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "Estas segur@ de tu granizado o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:  ",
                                                        )
                                                        if d2 == "1":
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_granizados[tamaño_h][0]
                                                            sabor_elegido = []
                                                            cent3 = True
                                                            while cent3 == True:
                                                                cont = 1
                                                                for i in granizados:
                                                                    print(
                                                                        cont, granizados[i])
                                                                    cont += 1
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    5,
                                                                    "Que sabor de granizado desea agregar: ",
                                                                )
                                                                d1 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "Estas seguro del sabor de tu granizado o quieres cambiar \n1. Estoy segur@  \n2. Quiero cambiar \nIngrese aqui:  ",
                                                                )
                                                                if d1 == "1":
                                                                    sabor_elegido.append(
                                                                        granizados[sabor]
                                                                    )

                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent3 = False
                                                                    d2 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d2 == "2":
                                                                        labrando = False

                                                    elif tamaño_h == "3":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de Granizado \n1. Estoy segur@ \n2. Quiero cambiar mi granizado \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent3 = True
                                                            while cent3 == True:
                                                                (
                                                                    tamaño_v,
                                                                    precio,
                                                                ) = tamaños_granizados[
                                                                    tamaño_h
                                                                ][
                                                                    0
                                                                ]
                                                                sabor_elegido = []
                                                                print(
                                                                    "Sabores de helado")
                                                                Sabor_helados()

                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en el salpicon: ",
                                                                )
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ del helado del salpicon? \n1. Estoy segur@ \n2. Quiero cambiar mi helado del salpicon  \nIngrese aqui: ",
                                                                )
                                                                if d3 == "1":
                                                                    sabor_elegido.append(
                                                                        sabores[sabor]
                                                                    )
                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent3 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d3 == "2":
                                                                        labrando = False

                                                    elif tamaño_h == "4":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de Granizado \n1. Estoy segur@ \n2. Quiero cambiar mi granizado \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_granizados[tamaño_h][0]
                                                            salpicon_sin_helado = [
                                                                "salpicon sin helado"
                                                            ]
                                                            agregar = {
                                                                "tipo": tipos[d],
                                                                "tamaño": tamaño_v,
                                                                "sabor": salpicon_sin_helado,
                                                                "precio": precio,
                                                            }
                                                            total = total + \
                                                                agregar["precio"]
                                                            dicTotal = {}
                                                            dicTotal["Total"] = total
                                                            factura_temporal.append(
                                                                agregar)
                                                            cent1 = False

                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                            )
                                                            if d3 == "2":
                                                                labrando = False

                                                    elif tamaño_h == "5":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de malteada \n1. Estoy segur@ \n2. Quiero cambiar mi granizado \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent3 = True
                                                            while cent3 == True:
                                                                (
                                                                    tamaño_v,
                                                                    precio,
                                                                ) = tamaños_granizados[
                                                                    tamaño_h
                                                                ][
                                                                    0
                                                                ]
                                                                sabor_elegido = []
                                                                print(
                                                                    "Sabores de helado")
                                                                Sabor_helados()

                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea de acompañamiento: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                                )
                                                                if d2 == "1":
                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent3 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d3 == "2":
                                                                        labrando = False
                                                else:
                                                    print(
                                                        "El siguiente producto no esta disponible:",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "4":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de copas infantiles o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_copas_infantiles:
                                                valor1, valor2 = tamaños_copas_infantiles[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_copas_infantiles[i][2],
                                                    )
                                                )
                                            print(n_infantil, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_infantil, "Que tamaño deseas elegir: "
                                            )
                                            if tamaño_h == str(n_infantil):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_copas_infantiles[
                                                    tamaño_h
                                                ][0]
                                                if (
                                                    tamaños_copas_infantiles[tamaño_h][1]
                                                    == True
                                                ):
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas segur@ del tipo de copa infantil? \n1. Estoy segur@ \n2. Quiero cambiar mi copa infantil \nIngrese aqui: ",
                                                    )
                                                    if d2 == "1":
                                                        cent2 = True
                                                        while cent2 == True:
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_copas_infantiles[
                                                                tamaño_h
                                                            ][
                                                                0
                                                            ]
                                                            bolas = (
                                                                cantidad_bolas_copa_infantil[
                                                                    tamaño_v
                                                                ]
                                                            )
                                                            sabor_elegido = []
                                                            print("Sabores de helado")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "El siguiente tipo no se encuentra disponible:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "5":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de malteadas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_malteadas:
                                                valor1, valor2 = tamaños_malteadas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3} ".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_malteadas[i][2],
                                                    )
                                                )
                                            print(n_malteadas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1,
                                                n_malteadas,
                                                "que tamaño de malteada desea?: ",
                                            )
                                            if tamaño_h == str(n_malteadas):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_malteadas[tamaño_h][
                                                    0
                                                ]
                                                if tamaños_malteadas[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas segur@ del tamaño de la malteada\n1. Estoy segur@ \n2. Quiero cambiar el tamaño de mi malteada \nIngrese aqui: ",
                                                    )
                                                    if d2 == "1":
                                                        cent2 = True
                                                        while cent2 == True:
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_malteadas[tamaño_h][0]
                                                            sabor_elegido = []
                                                            print("sabores de helado")
                                                            Sabor_helados()

                                                            sabor = validar_opcion(
                                                                1,
                                                                22,
                                                                "Que sabor de helado desea la malteada: ",
                                                            )
                                                            sabor_elegido.append(
                                                                sabores[sabor])
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de malteada no se encuentra disponible:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "6":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de litro de helado o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_litro_helado:
                                                valor1, valor2 = tamaños_litro_helado[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_litro_helado[i][2],
                                                    )
                                                )
                                            print(n_litro_helado, "para salir")
                                            tamaño_h = validar_opcion(
                                                1,
                                                n_litro_helado,
                                                "que tamaño de litro(s) desea?:",
                                            )
                                            if tamaño_h == str(n_litro_helado):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_litro_helado[
                                                    tamaño_h
                                                ][0]
                                                if tamaños_litro_helado[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ de tu tipo de litro(s) de helado o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:  ",
                                                    )
                                                    if d2 == "1":
                                                        tamaño_v, precio = tamaños_litro_helado[
                                                            tamaño_h
                                                        ][0]
                                                        cent2 = True
                                                        while cent2 == True:
                                                            sabor_elegido = []
                                                            print("sabores de helado")
                                                            Sabor_helados()

                                                            sabor = validar_opcion(
                                                                1,
                                                                22,
                                                                "Que sabor de helado desea en el litro de helado: ",
                                                            )
                                                            sabor_elegido.append(
                                                                sabores[sabor])
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ del sabor del helado?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui: ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent2 = False
                                                                cent1 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False

                                                else:
                                                    print(
                                                        "el siguiente tamaño de litro(s) de helado no se encuentra disponible:",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "7":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de ensalada de frutas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_ensalada_frutas:
                                                valor1, valor2 = tamaños_ensalada_frutas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_ensalada_frutas[i][2],
                                                    )
                                                )
                                            print(n_frutas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1,
                                                n_frutas,
                                                "que tamaño de ensalada de frutas desea?:  ",
                                            )
                                            if tamaño_h == str(n_frutas):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_ensalada_frutas[
                                                    tamaño_h
                                                ][0]
                                                if tamaños_ensalada_frutas[tamaño_h][1] == True:
                                                    if tamaño_h == "3" or tamaño_h == "1":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de ensalada de frutas?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de ensalada \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent2 = True
                                                            while cent2 == True:
                                                                (
                                                                    tamaño_v,
                                                                    precio,
                                                                ) = tamaños_ensalada_frutas[
                                                                    tamaño_h
                                                                ][
                                                                    0
                                                                ]
                                                                sabor_elegido = []
                                                                print(
                                                                    "Sabores de helado")
                                                                Sabor_helados()
                                                                for z in range(0, 2):
                                                                    sabor = validar_opcion(
                                                                        1,
                                                                        22,
                                                                        "Que sabor de helado desea en la ensalada de frutas: ",
                                                                    )
                                                                    sabor_elegido.append(
                                                                        sabores[sabor]
                                                                    )
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                                )
                                                                if d2 == "1":
                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent2 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d3 == "2":
                                                                        labrando = False

                                                    elif tamaño_h == "2":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de ensalada de frutas?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de ensalada \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_ensalada_frutas[
                                                                tamaño_h
                                                            ][
                                                                0
                                                            ]
                                                            sabor_elegido = [
                                                                "Ensalada de frutas sin helado"
                                                            ]

                                                            agregar = {
                                                                "tipo": tipos[d],
                                                                "tamaño": tamaño_v,
                                                                "sabor": sabor_elegido,
                                                                "precio": precio,
                                                            }
                                                            total = total + \
                                                                agregar["precio"]
                                                            dicTotal = {}
                                                            dicTotal["Total"] = total
                                                            factura_temporal.append(
                                                                agregar)
                                                            cent1 = False
                                                            cent2 = False
                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                            )
                                                            if d3 == "2":
                                                                labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de ensalada de frutas no se encuentra disponible en este momento:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "8":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de fresas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            for i in tamaños_fresas:
                                                valor1, valor2 = tamaños_fresas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_fresas[i][2]
                                                    )
                                                )
                                            print(n_fresas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_fresas, "que tipo de  fresas desea?:  "
                                            )
                                            if tamaño_h == str(n_fresas):
                                                cent2 = False
                                            else:
                                                tamaño_v, precio = tamaños_fresas[tamaño_h][0]
                                                if tamaños_fresas[tamaño_h][1] == True:
                                                    sabor_elegido = []
                                                    sabor_fresas_crema = [
                                                        "Fresas con crema"]
                                                    if tamaño_h == "1":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de fresa?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de fresa \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            agregar = {
                                                                "tipo": tipos[d],
                                                                "tamaño": tamaño_v,
                                                                "sabor": sabor_fresas_crema,
                                                                "precio": precio,
                                                            }
                                                            total = total + \
                                                                agregar["precio"]
                                                            dicTotal = {}
                                                            dicTotal["Total"] = total
                                                            factura_temporal.append(
                                                                agregar)
                                                            cent = False
                                                            cent2 = False
                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                            )
                                                            if d3 == "2":
                                                                labrando = False
                                                                cent2 = False

                                                    elif tamaño_h == "2":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de fresa?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de fresa \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent3 = True
                                                            while cent3 == True:
                                                                Sabor_helados()
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en las fresas: ",
                                                                )
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ del sabor de helado??\n1. Estoy segur@ \n2. Quiero cambiar mi sabor de helado \nIngrese aqui: ",
                                                                )
                                                                if d3 == "1":
                                                                    sabor_elegido.append(
                                                                        sabores[sabor]
                                                                    )

                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent = False
                                                                    cent2 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    cent2 = False
                                                                    cent3 = False
                                                                    if d3 == "2":
                                                                        labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de fresas con crema no se encuentra disponible",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "9":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de copas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            print("Tipos de copas:")
                                            for i in tamaños_copas:
                                                valor1, valor2 = tamaños_copas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3} ".format(
                                                        i, valor1, valor2, tamaños_copas[i][2]
                                                    )
                                                )
                                            print(n_copas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_copas, "Que tipo deseas elegir: "
                                            )
                                            if tamaño_h == str(n_copas):
                                                cent2 = False
                                            else:
                                                tamaño, precio = tamaños_copas[tamaño_h][0]
                                                if tamaños_copas[tamaño_h][1] == True:
                                                    d3 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas seguro del tipo de copa o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi copa \nIngrese aqui: ",
                                                    )
                                                    if d3 == "1":
                                                        tamaño, precio = tamaños_copas[
                                                            tamaño_h
                                                        ][0]
                                                        bolas = cantidad_bolas[tamaño]
                                                        cent = True
                                                        while cent == True:
                                                            sabor_elegido = []
                                                            print("sabores de helados")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                                    cent2 = False
                                                else:
                                                    print(
                                                        "la siguiente copa no se encuentra disponible en este momento:",
                                                        tamaño,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "10":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de banana split o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            for i in tamaños_banana_split:
                                                valor1, valor2 = tamaños_banana_split[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_banana_split[i][2],
                                                    )
                                                )
                                            tamaño_h = validar_opcion(
                                                1,
                                                2,
                                                "ingrese 2 para volver: \nque tamaño de banana split desea?: ",
                                            )
                                            if tamaño_h == "2":
                                                cent2 = False
                                            else:
                                                tamaño_v, precio = tamaños_banana_split[
                                                    tamaño_h
                                                ][0]
                                                if tamaños_banana_split[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ de tu tipo de de banana split? \n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:",
                                                    )
                                                    if d2 == "1":
                                                        tamaño_v, precio = tamaños_banana_split[
                                                            tamaño_h
                                                        ][0]
                                                        cent = True
                                                        while cent == True:
                                                            print("Sabores de helados")
                                                            Sabor_helados()
                                                            sabor_elegido = []
                                                            for z in range(0, 2):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en el banana split :",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }

                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de banan split no se encuentra disponible: ",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                                    tamaños_brownie
                            elif d == "11":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de brownies o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            for i in tamaños_brownie:
                                                valor1, valor2 = tamaños_brownie[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_brownie[i][2]
                                                    )
                                                )
                                            print(n_brownie, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_brownie, "que tamaño de brownie desea?: "
                                            )
                                            if tamaño_h == str(n_brownie):
                                                cent2 = False
                                            else:
                                                tamaño_v, precio = tamaños_brownie[tamaño_h][0]
                                                if tamaños_brownie[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ de tu tipo de de banana split? \n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:",
                                                    )
                                                    if d2 == "1":
                                                        tamaño_v, precio = tamaños_brownie[
                                                            tamaño_h
                                                        ][0]
                                                        cent = True
                                                        while cent == True:
                                                            print("Sabores de helados")
                                                            Sabor_helados()
                                                            sabor_elegido = []
                                                            for z in range(0, 1):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en el banana split :",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }

                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False

                                                else:
                                                    print(
                                                        "el siguiente tamaño de banan split no se encuentra disponible: ",
                                                        tamaño_v,
                                                    )
                                                    cent2 = False

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "12":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de paletas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            print("sabores paletas: ")
                                            for i in sabores_paletas_base:
                                                valor1, valor2 = sabores_paletas_base[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        sabores_paletas_base[i][2],
                                                    )
                                                )
                                            sabor_elegido = []
                                            print(n_paletas, "para volver al menu")
                                            tamaño_h = validar_opcion(
                                                1, n_paletas, "que sabor de la paleta desea?: "
                                            )
                                            if tamaño_h != str(n_paletas):
                                                tamaño_v, precio = sabores_paletas_base[
                                                    tamaño_h
                                                ][0]
                                                sabor_elegido.append(
                                                    sabores_paletas[tamaño_h])
                                                d2 = validar_opcion(
                                                    1,
                                                    2,
                                                    "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                )
                                                if d2 == "1":
                                                    agregar = {
                                                        "tipo": tipos[d],
                                                        "tamaño": tamaño_v,
                                                        "sabor": sabor_elegido,
                                                        "precio": precio,
                                                    }

                                                    total = total + agregar["precio"]
                                                    dicTotal = {}
                                                    dicTotal["Total"] = total
                                                    factura_temporal.append(agregar)
                                                    cent = False
                                                    cent2 = False
                                                    d3 = validar_opcion(
                                                        1,
                                                        2,
                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                    )
                                                    if d3 == "2":
                                                        labrando = False
                                            else:
                                                cent2 = False
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "13":
                                if len(subcategorias_nuevas) == 0:
                                    print(
                                        "Esta categoría no tiene productos"
                                    )
                                else:
                                    contSubCategoria = 1
                                    subcategoriasHabilitadas = []
                                    opcionesSubcategorias = ""
                                    for i in subcategorias_nuevas:
                                        subcategoriasHabilitadas.append(
                                            [
                                                subcategorias_nuevas[i][
                                                    0
                                                ]
                                                + " "
                                                + subcategorias_nuevas[
                                                    i
                                                ][2]
                                            ]
                                        )
                                        contSubCategoria += 1
                                    for i, subCategoria in enumerate(
                                        subcategoriasHabilitadas
                                    ):
                                        nombreSubCategoria = (
                                            subCategoria[0]
                                        )
                                        opcionesSubcategorias += f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                    preguntaSubCategoria = input(
                                        opcionesSubcategorias
                                        + "Elige una opción: "
                                    )
                                    if (
                                        preguntaSubCategoria.isdigit()
                                        and int(preguntaSubCategoria)
                                        > 0
                                        and int(preguntaSubCategoria)
                                        <= len(subcategoriasHabilitadas)
                                    ):
                                        if (
                                            len(
                                                subcategorias_nuevas[
                                                    int(
                                                        preguntaSubCategoria
                                                    )
                                                ][3]
                                            )
                                            == 0
                                        ):
                                            print(
                                                "Esta subcategoria no tiene productos"
                                            )
                                        else:
                                            if subcategorias_nuevas[int(preguntaSubCategoria)][1] == True:
                                                contadorProductoSubcategoria=1
                                                productosHabilitados = []
                                                opcionesProductos = ""
                                                for i in subcategorias_nuevas[int(preguntaSubCategoria)][3]:
                                                    productosHabilitados.append([
                                                        subcategorias_nuevas[int(preguntaSubCategoria)][3][i][0],
                                                        " ",
                                                        subcategorias_nuevas[int(preguntaSubCategoria)][3][i][2]]
                                                    )
                                                    contadorProductoSubcategoria+=1
                                                for i,producto in enumerate(productosHabilitados):
                                                    nombreProducto = (
                                                            producto[0][0]
                                                        )
                                                    precioProducto=(producto[0][1])
                                                    opcionesProductos += f"{i+1}. {nombreProducto.capitalize()} - {precioProducto}\n"
                                                preguntaProducto = input(
                                                        opcionesProductos
                                                        + "Elige una opción: "
                                                        )
                                                if (preguntaProducto.isdigit()
                                                    and int(preguntaProducto)
                                                    > 0
                                                    and int(preguntaProducto)
                                                    <= len(productosHabilitados)):
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas seguro de tu eleccion o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi producto \nIngrese aqui:  ",
                                                    )
                                                    if d2 == "1":
                                                        agregar = {
                                                            "tipo": subcategorias_nuevas[int(preguntaSubCategoria)][0],
                                                            "tamaño": subcategorias_nuevas[int(preguntaSubCategoria)][3]["1"][0],
                                                            "sabor": subcategorias_nuevas[int(preguntaSubCategoria)][3]["1"][0],
                                                            "precio": subcategorias_nuevas[int(preguntaSubCategoria)][3]["1"][0][1],
                                                        }

                                                        total = total + agregar["precio"]
                                                        dicTotal = {}
                                                        dicTotal["Total"] = total
                                                        factura_temporal.append(agregar)
                                                        cent = False
                                                        cent2 = False
                                                        d3 = validar_opcion(
                                                            1,
                                                            2,
                                                            "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                        )
                                                        if d3 == "2":
                                                            labrando = False
                                            else:
                                                print(
                                                    "Esta subcategoría se encuentra deshabilitada"
                                                )
                                    else:
                                        print(
                                            "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                        )
                                break

                            elif d == "14":
                                labrando = False

                        if total != 0:
                            Factura_unica.append(contador_general)
                            Factura_unica.append(correoUsuario)
                            Factura_unica.append(fecha_formateada)
                            Factura_unica.append(factura_temporal)
                            Factura_unica.append("Caja")
                            Factura_unica.append(dicTotal)
                            t = threading.Thread(target=agregarFactura, args=(Factura_unica,))
                            t.start()
                            contador_general += 1
                            print(Factura_unica)
                    if preguntaCajero=="3":
                        if len(facturasFinalizadas)==0:
                            print("No hay pedidos por entregar")
                        else:
                            for factura in facturasFinalizadas:
                                print("---------------------")
                                print("N°Factura: ", factura[0])
                                print("Nombre: ", factura[1])
                                print("Fecha: ", factura[2])
                                print("Detalles: ", factura[3])
                                print("Tipo de pago: ", factura[4])
                                print("Total: ",factura[-1]["Total"])
                                print("---------------------")

                            while True:
                                preguntaPedido = input("¿Qué factura deseas finalizar? (Ingresa el número de factura o selecciona 0 para volver): ")
                                if preguntaPedido.isdigit():
                                    preguntaPedido = int(preguntaPedido)
                                    if preguntaPedido == 0:
                                        break
                                    else:
                                        encontradoPendiente=False
                                        for facturaP in facturasFinalizadas:
                                            if facturaP[0]==preguntaPedido:
                                                encontradoPendiente=True
                                        if encontradoPendiente==True:
                                            for i,facturaP in enumerate(facturasFinalizadas):
                                                if facturaP[0]==preguntaPedido:
                                                    facturas.append(facturasFinalizadas[i])
                                                    del facturasFinalizadas[i]
                                                    print("Pedido Entregado")
                                            break
                                        else:
                                            print("No se encontró el pedido")
                                else:
                                    print("Ingresa una opción válida")
                    if preguntaCajero=="4":
                        break
            elif i[2] == "usuario":
                while True:
                    modificar = input(
                        "1. Modificar Usuario \n2. Salir\n3. Realizar pedido\n4. Cancelar Pedido\nSelecciona una opción: ")
                    if modificar == "1":
                        r = 1
                        while r == 1:
                            usuarioGlobal=usuario
                            contraseñaGlobal=contraseña
                            preguntaUsuario = input("Ingrese su usuario: ").strip()
                            preguntaContraseña = input(
                                "Ingrese su contraseña: ").strip()
                            encontrado = False
                            print(usuarioGlobal,contraseñaGlobal)
                            if usuarioGlobal == preguntaUsuario and contraseñaGlobal == preguntaContraseña:
                                encontrado = True
                            if encontrado:
                                t=1
                                while t==1:
                                    quecosa = input(
                                        "Qué desea modificar: 1. Usuario, 2. Contraseña, 3. Teléfono, 4. Dirección, 5. Volver: ")
                                    if quecosa == "1":
                                        nuevousuario = input(
                                            "Ingrese su nuevo usuario: ").strip()
                                        if nuevousuario in [usuario_info[0] for usuario_info in usuarios]:
                                            print(
                                                "El usuario ya está registrado")
                                        elif "@" not in nuevousuario or ".com" not in nuevousuario:
                                            print(
                                                "El nuevo usuario debe tener el formato 'ncaracteres@ncaracteres.com'. Inténtelo nuevamente.")
                                        else:
                                            for usuario_info in usuarios:
                                                if usuario_info[0].lower() == usuario.lower():
                                                    usuario_info[0] = nuevousuario
                                                    print(usuarios)
                                                    t=2
                                                    r=2
                                                    break
                                    elif quecosa == "2":
                                        j=1
                                        while j==1:
                                            nuevacontra = input("Ingrese su nueva contraseña: ")
                                            encontrado = False
                                            for usuario_info in usuarios:
                                                if usuario_info[0].lower() == usuario.lower():
                                                    encontrado = True
                                                    if nuevacontra != usuario_info[1]:
                                                        usuario_info[1] = nuevacontra
                                                        t=2
                                                        r=2
                                                        j=2
                                                    else:
                                                        print("Ya tenía esta contraseña.")
                                    elif quecosa == "3":
                                        g=1
                                        while g==1:
                                            nuevotel = input("Ingrese su nuevo teléfono: ")
                                            if nuevotel.isdigit() and (len(nuevotel) == 10):                            
                                                if nuevotel in [usuario_info[3][3] for usuario_info in usuarios]:
                                                    print("El número ya esta registrado") 
                                                else:   
                                                    for usuario_info in usuarios:
                                                        if nuevotel != usuario_info[3][3]:
                                                            usuario_info[3][3] = nuevotel
                                                            t=2
                                                            r=2
                                                            g=2
                                                            break

                                            else:
                                                print("Número inválido. Debe ser un número entero de 10 dígitos.")
                                    elif quecosa == "4":
                                        nuevadir = input(
                                            "Ingrese su nueva dirección: ").strip()
                                        for usuario_info in usuarios:
                                            if usuario_info[0].lower() == usuario.lower():
                                                usuario_info[3][4] = nuevadir
                                                t=2
                                                r=2
                                                break
                                    elif quecosa == "5":
                                        r = 2
                                        break
                                    else:
                                        print(
                                            "Por favor ingrese un número del 1 al 5.")
                            else:
                                print("Usuario o contraseña incorrectos")
                    elif modificar == "2":
                        break
                    elif modificar == "3":
                        labrando = True
                        while labrando == True:
                            print(
                                "Bienvenid@ a la heladeria boquitas, que tipo de producto deseas elegir?"
                            )
                            cont = 1
                            for i in tipos2:
                                print(cont, tipos2[i][0], tipos2[i][2])
                                cont += 1
                            print(cantidad_productos, "para salir")
                            d = validar_opcion(
                                1, cantidad_productos, "Ingrese el tipo de producto a elegir: ")
                            if d == "1":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la sección de vasos o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_vasos:
                                                valor1, valor2 = tamaños_vasos[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_vasos[i][2]
                                                    )
                                                )
                                            print(n_vasos, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_vasos, "Que tamaño deseas elegir:  "
                                            )
                                            if tamaño_h == str(n_vasos):
                                                cent1 = False
                                            else:
                                                tamaño, precio = tamaños_vasos[tamaño_h][0]
                                                if tamaños_vasos[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ del tamaño del vaso o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:  ",
                                                    )
                                                    if d2 == "1":
                                                        cent1 = True
                                                        while cent1 == True:
                                                            tamaño, precio = tamaños_vasos[
                                                                tamaño_h
                                                            ][0]
                                                            bolas = cantidad_bolas_vasos[tamaño]
                                                            sabor_elegido = []
                                                            print(
                                                                "Sabores de helado")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d3 = validar_opcion(
                                                                1,
                                                                3,
                                                                "estas segur@ del sabor de helado? \n1. Estoy segur@ \n2. Quiero cambiar mi sabor de helado \n3. Volver al menu \nIngrese aqui: ",
                                                            )
                                                            if d3 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent3 = False
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d2 == "2":
                                                                    labrando = False
                                                            elif d3 == "3":
                                                                cent1 = False

                                                else:
                                                    print(
                                                        "el siguiente tamaño no esta disponible en este momento:",
                                                        tamaño,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "2":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de conos o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_conos:
                                                valor1, valor2 = tamaños_conos[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_conos[i][2]
                                                    )
                                                )
                                            print(n_conos, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_conos, "Que tamaño deseas elegir: "
                                            )
                                            if tamaño_h == str(n_conos):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_conos[tamaño_h][0]
                                                if tamaños_conos[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ del tamaño del cono o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:  ",
                                                    )
                                                    if d2 == "1":
                                                        cent1 = True
                                                        while cent1 == True:
                                                            tamaño_v, precio = tamaños_conos[
                                                                tamaño_h
                                                            ][0]
                                                            bolas = cantidad_bolas_conos[
                                                                tamaño_v
                                                            ]
                                                            sabor_elegido = []
                                                            print(
                                                                "Sabores de helado")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )

                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ del sabor de helado? \n1. Estoy segur@ \n2. Quiero cambiar mi sabor de helado  \nIngrese aqui: ",
                                                            )
                                                            if d3 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent3 = False
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d2 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño no esta disponible en este momento:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "3":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de Granizados o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_granizados:
                                                valor1, valor2 = tamaños_granizados[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_granizados[i][2],
                                                    )
                                                )
                                            print(n_granizados, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_granizados, "Que granizado deseas elegir:"
                                            )
                                            if tamaño_h == str(n_granizados):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_granizados[tamaño_h][
                                                    0
                                                ]
                                                if tamaños_granizados[tamaño_h][1] == True:
                                                    if tamaño_h == "1" or tamaño_h == "2":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "Estas segur@ de tu granizado o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:  ",
                                                        )
                                                        if d2 == "1":
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_granizados[tamaño_h][0]
                                                            sabor_elegido = []
                                                            cent3 = True
                                                            while cent3 == True:
                                                                cont = 1
                                                                for i in granizados:
                                                                    print(
                                                                        cont, granizados[i])
                                                                    cont += 1
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    5,
                                                                    "Que sabor de granizado desea agregar: ",
                                                                )
                                                                d1 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "Estas seguro del sabor de tu granizado o quieres cambiar \n1. Estoy segur@  \n2. Quiero cambiar \nIngrese aqui:  ",
                                                                )
                                                                if d1 == "1":
                                                                    sabor_elegido.append(
                                                                        granizados[sabor]
                                                                    )

                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent3 = False
                                                                    d2 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d2 == "2":
                                                                        labrando = False

                                                    elif tamaño_h == "3":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de Granizado \n1. Estoy segur@ \n2. Quiero cambiar mi granizado \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent3 = True
                                                            while cent3 == True:
                                                                (
                                                                    tamaño_v,
                                                                    precio,
                                                                ) = tamaños_granizados[
                                                                    tamaño_h
                                                                ][
                                                                    0
                                                                ]
                                                                sabor_elegido = []
                                                                print(
                                                                    "Sabores de helado")
                                                                Sabor_helados()

                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en el salpicon: ",
                                                                )
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ del helado del salpicon? \n1. Estoy segur@ \n2. Quiero cambiar mi helado del salpicon  \nIngrese aqui: ",
                                                                )
                                                                if d3 == "1":
                                                                    sabor_elegido.append(
                                                                        sabores[sabor]
                                                                    )
                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent3 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d3 == "2":
                                                                        labrando = False

                                                    elif tamaño_h == "4":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de Granizado \n1. Estoy segur@ \n2. Quiero cambiar mi granizado \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_granizados[tamaño_h][0]
                                                            salpicon_sin_helado = [
                                                                "salpicon sin helado"
                                                            ]
                                                            agregar = {
                                                                "tipo": tipos[d],
                                                                "tamaño": tamaño_v,
                                                                "sabor": salpicon_sin_helado,
                                                                "precio": precio,
                                                            }
                                                            total = total + \
                                                                agregar["precio"]
                                                            dicTotal = {}
                                                            dicTotal["Total"] = total
                                                            factura_temporal.append(
                                                                agregar)
                                                            cent1 = False

                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                            )
                                                            if d3 == "2":
                                                                labrando = False

                                                    elif tamaño_h == "5":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de malteada \n1. Estoy segur@ \n2. Quiero cambiar mi granizado \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent3 = True
                                                            while cent3 == True:
                                                                (
                                                                    tamaño_v,
                                                                    precio,
                                                                ) = tamaños_granizados[
                                                                    tamaño_h
                                                                ][
                                                                    0
                                                                ]
                                                                sabor_elegido = []
                                                                print(
                                                                    "Sabores de helado")
                                                                Sabor_helados()

                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea de acompañamiento: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                                )
                                                                if d2 == "1":
                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent3 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d3 == "2":
                                                                        labrando = False
                                                else:
                                                    print(
                                                        "El siguiente producto no esta disponible:",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "4":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de copas infantiles o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_copas_infantiles:
                                                valor1, valor2 = tamaños_copas_infantiles[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_copas_infantiles[i][2],
                                                    )
                                                )
                                            print(n_infantil, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_infantil, "Que tamaño deseas elegir: "
                                            )
                                            if tamaño_h == str(n_infantil):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_copas_infantiles[
                                                    tamaño_h
                                                ][0]
                                                if (
                                                    tamaños_copas_infantiles[tamaño_h][1]
                                                    == True
                                                ):
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas segur@ del tipo de copa infantil? \n1. Estoy segur@ \n2. Quiero cambiar mi copa infantil \nIngrese aqui: ",
                                                    )
                                                    if d2 == "1":
                                                        cent2 = True
                                                        while cent2 == True:
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_copas_infantiles[
                                                                tamaño_h
                                                            ][
                                                                0
                                                            ]
                                                            bolas = (
                                                                cantidad_bolas_copa_infantil[
                                                                    tamaño_v
                                                                ]
                                                            )
                                                            sabor_elegido = []
                                                            print(
                                                                "Sabores de helado")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "El siguiente tipo no se encuentra disponible:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "5":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de malteadas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_malteadas:
                                                valor1, valor2 = tamaños_malteadas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3} ".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_malteadas[i][2],
                                                    )
                                                )
                                            print(n_malteadas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1,
                                                n_malteadas,
                                                "que tamaño de malteada desea?: ",
                                            )
                                            if tamaño_h == str(n_malteadas):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_malteadas[tamaño_h][
                                                    0
                                                ]
                                                if tamaños_malteadas[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas segur@ del tamaño de la malteada\n1. Estoy segur@ \n2. Quiero cambiar el tamaño de mi malteada \nIngrese aqui: ",
                                                    )
                                                    if d2 == "1":
                                                        cent2 = True
                                                        while cent2 == True:
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_malteadas[tamaño_h][0]
                                                            sabor_elegido = []
                                                            print(
                                                                "sabores de helado")
                                                            Sabor_helados()

                                                            sabor = validar_opcion(
                                                                1,
                                                                22,
                                                                "Que sabor de helado desea la malteada: ",
                                                            )
                                                            sabor_elegido.append(
                                                                sabores[sabor])
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent1 = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de malteada no se encuentra disponible:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "6":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de litro de helado o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_litro_helado:
                                                valor1, valor2 = tamaños_litro_helado[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_litro_helado[i][2],
                                                    )
                                                )
                                            print(n_litro_helado, "para salir")
                                            tamaño_h = validar_opcion(
                                                1,
                                                n_litro_helado,
                                                "que tamaño de litro(s) desea?:",
                                            )
                                            if tamaño_h == str(n_litro_helado):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_litro_helado[
                                                    tamaño_h
                                                ][0]
                                                if tamaños_litro_helado[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ de tu tipo de litro(s) de helado o deseas cambiar??\n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:  ",
                                                    )
                                                    if d2 == "1":
                                                        tamaño_v, precio = tamaños_litro_helado[
                                                            tamaño_h
                                                        ][0]
                                                        cent2 = True
                                                        while cent2 == True:
                                                            sabor_elegido = []
                                                            print(
                                                                "sabores de helado")
                                                            Sabor_helados()

                                                            sabor = validar_opcion(
                                                                1,
                                                                22,
                                                                "Que sabor de helado desea en el litro de helado: ",
                                                            )
                                                            sabor_elegido.append(
                                                                sabores[sabor])
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas segur@ del sabor del helado?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui: ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent2 = False
                                                                cent1 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False

                                                else:
                                                    print(
                                                        "el siguiente tamaño de litro(s) de helado no se encuentra disponible:",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "7":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de ensalada de frutas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent1 = True
                                        while cent1 == True:
                                            for i in tamaños_ensalada_frutas:
                                                valor1, valor2 = tamaños_ensalada_frutas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_ensalada_frutas[i][2],
                                                    )
                                                )
                                            print(n_frutas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1,
                                                n_frutas,
                                                "que tamaño de ensalada de frutas desea?:  ",
                                            )
                                            if tamaño_h == str(n_frutas):
                                                cent1 = False
                                            else:
                                                tamaño_v, precio = tamaños_ensalada_frutas[
                                                    tamaño_h
                                                ][0]
                                                if tamaños_ensalada_frutas[tamaño_h][1] == True:
                                                    if tamaño_h == "3" or tamaño_h == "1":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de ensalada de frutas?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de ensalada \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent2 = True
                                                            while cent2 == True:
                                                                (
                                                                    tamaño_v,
                                                                    precio,
                                                                ) = tamaños_ensalada_frutas[
                                                                    tamaño_h
                                                                ][
                                                                    0
                                                                ]
                                                                sabor_elegido = []
                                                                print(
                                                                    "Sabores de helado")
                                                                Sabor_helados()
                                                                for z in range(0, 2):
                                                                    sabor = validar_opcion(
                                                                        1,
                                                                        22,
                                                                        "Que sabor de helado desea en la ensalada de frutas: ",
                                                                    )
                                                                    sabor_elegido.append(
                                                                        sabores[sabor]
                                                                    )
                                                                d2 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ de los sabores de helado?\n1. Estoy segur@ \n2. Quiero cambiar mis sabores \nIngrese aqui: ",
                                                                )
                                                                if d2 == "1":
                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent1 = False
                                                                    cent2 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    if d3 == "2":
                                                                        labrando = False

                                                    elif tamaño_h == "2":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de ensalada de frutas?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de ensalada \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            (
                                                                tamaño_v,
                                                                precio,
                                                            ) = tamaños_ensalada_frutas[
                                                                tamaño_h
                                                            ][
                                                                0
                                                            ]
                                                            sabor_elegido = [
                                                                "Ensalada de frutas sin helado"
                                                            ]

                                                            agregar = {
                                                                "tipo": tipos[d],
                                                                "tamaño": tamaño_v,
                                                                "sabor": sabor_elegido,
                                                                "precio": precio,
                                                            }
                                                            total = total + \
                                                                agregar["precio"]
                                                            dicTotal = {}
                                                            dicTotal["Total"] = total
                                                            factura_temporal.append(
                                                                agregar)
                                                            cent1 = False
                                                            cent2 = False
                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                            )
                                                            if d3 == "2":
                                                                labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de ensalada de frutas no se encuentra disponible en este momento:",
                                                        tamaño_v,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "8":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de fresas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            for i in tamaños_fresas:
                                                valor1, valor2 = tamaños_fresas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_fresas[i][2]
                                                    )
                                                )
                                            print(n_fresas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_fresas, "que tipo de  fresas desea?:  "
                                            )
                                            if tamaño_h == str(n_fresas):
                                                cent2 = False
                                            else:
                                                tamaño_v, precio = tamaños_fresas[tamaño_h][0]
                                                if tamaños_fresas[tamaño_h][1] == True:
                                                    sabor_elegido = []
                                                    sabor_fresas_crema = [
                                                        "Fresas con crema"]
                                                    if tamaño_h == "1":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de fresa?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de fresa \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            agregar = {
                                                                "tipo": tipos[d],
                                                                "tamaño": tamaño_v,
                                                                "sabor": sabor_fresas_crema,
                                                                "precio": precio,
                                                            }
                                                            total = total + \
                                                                agregar["precio"]
                                                            dicTotal = {}
                                                            dicTotal["Total"] = total
                                                            factura_temporal.append(
                                                                agregar)
                                                            cent = False
                                                            cent2 = False
                                                            d3 = validar_opcion(
                                                                1,
                                                                2,
                                                                "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                            )
                                                            if d3 == "2":
                                                                labrando = False
                                                                cent2 = False

                                                    elif tamaño_h == "2":
                                                        d2 = validar_opcion(
                                                            1,
                                                            2,
                                                            "estas segur@ del tipo de fresa?\n1. Estoy segur@ \n2. Quiero cambiar mi tipo de fresa \nIngrese aqui: ",
                                                        )
                                                        if d2 == "1":
                                                            cent3 = True
                                                            while cent3 == True:
                                                                Sabor_helados()
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en las fresas: ",
                                                                )
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "estas segur@ del sabor de helado??\n1. Estoy segur@ \n2. Quiero cambiar mi sabor de helado \nIngrese aqui: ",
                                                                )
                                                                if d3 == "1":
                                                                    sabor_elegido.append(
                                                                        sabores[sabor]
                                                                    )

                                                                    agregar = {
                                                                        "tipo": tipos[d],
                                                                        "tamaño": tamaño_v,
                                                                        "sabor": sabor_elegido,
                                                                        "precio": precio,
                                                                    }
                                                                    total = (
                                                                        total
                                                                        + agregar["precio"]
                                                                    )
                                                                    dicTotal = {}
                                                                    dicTotal["Total"] = total
                                                                    factura_temporal.append(
                                                                        agregar
                                                                    )
                                                                    cent = False
                                                                    cent2 = False
                                                                    d3 = validar_opcion(
                                                                        1,
                                                                        2,
                                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                    )
                                                                    cent2 = False
                                                                    cent3 = False
                                                                    if d3 == "2":
                                                                        labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de fresas con crema no se encuentra disponible",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "9":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de copas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            print("Tipos de copas:")
                                            for i in tamaños_copas:
                                                valor1, valor2 = tamaños_copas[i][0]
                                                print(
                                                    "{0}. {1} {2} {3} ".format(
                                                        i, valor1, valor2, tamaños_copas[i][2]
                                                    )
                                                )
                                            print(n_copas, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_copas, "Que tipo deseas elegir: "
                                            )
                                            if tamaño_h == str(n_copas):
                                                cent2 = False
                                            else:
                                                tamaño, precio = tamaños_copas[tamaño_h][0]
                                                if tamaños_copas[tamaño_h][1] == True:
                                                    d3 = validar_opcion(
                                                        1,
                                                        2,
                                                        "estas seguro del tipo de copa o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi copa \nIngrese aqui: ",
                                                    )
                                                    if d3 == "1":
                                                        tamaño, precio = tamaños_copas[
                                                            tamaño_h
                                                        ][0]
                                                        bolas = cantidad_bolas[tamaño]
                                                        cent = True
                                                        while cent == True:
                                                            sabor_elegido = []
                                                            print(
                                                                "sabores de helados")
                                                            Sabor_helados()
                                                            for z in range(0, bolas):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea agregar: ",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }
                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                                    cent2 = False
                                                else:
                                                    print(
                                                        "la siguiente copa no se encuentra disponible en este momento:",
                                                        tamaño,
                                                    )
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "10":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de banana split o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            for i in tamaños_banana_split:
                                                valor1, valor2 = tamaños_banana_split[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        tamaños_banana_split[i][2],
                                                    )
                                                )
                                            tamaño_h = validar_opcion(
                                                1,
                                                2,
                                                "ingrese 2 para volver: \nque tamaño de banana split desea?: ",
                                            )
                                            if tamaño_h == "2":
                                                cent2 = False
                                            else:
                                                tamaño_v, precio = tamaños_banana_split[
                                                    tamaño_h
                                                ][0]
                                                if tamaños_banana_split[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ de tu tipo de de banana split? \n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:",
                                                    )
                                                    if d2 == "1":
                                                        tamaño_v, precio = tamaños_banana_split[
                                                            tamaño_h
                                                        ][0]
                                                        cent = True
                                                        while cent == True:
                                                            print(
                                                                "Sabores de helados")
                                                            Sabor_helados()
                                                            sabor_elegido = []
                                                            for z in range(0, 2):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en el banana split :",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }

                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False
                                                else:
                                                    print(
                                                        "el siguiente tamaño de banan split no se encuentra disponible: ",
                                                        tamaño_v,
                                                    )

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                                    tamaños_brownie
                            elif d == "11":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de brownies o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            for i in tamaños_brownie:
                                                valor1, valor2 = tamaños_brownie[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i, valor1, valor2, tamaños_brownie[i][2]
                                                    )
                                                )
                                            print(n_brownie, "para salir")
                                            tamaño_h = validar_opcion(
                                                1, n_brownie, "que tamaño de brownie desea?: "
                                            )
                                            if tamaño_h == str(n_brownie):
                                                cent2 = False
                                            else:
                                                tamaño_v, precio = tamaños_brownie[tamaño_h][0]
                                                if tamaños_brownie[tamaño_h][1] == True:
                                                    d2 = validar_opcion(
                                                        1,
                                                        2,
                                                        "Estas segur@ de tu tipo de de banana split? \n1. Estoy segur@ \n2. Quiero cambiar \nIngrese aqui:",
                                                    )
                                                    if d2 == "1":
                                                        tamaño_v, precio = tamaños_brownie[
                                                            tamaño_h
                                                        ][0]
                                                        cent = True
                                                        while cent == True:
                                                            print(
                                                                "Sabores de helados")
                                                            Sabor_helados()
                                                            sabor_elegido = []
                                                            for z in range(0, 1):
                                                                sabor = validar_opcion(
                                                                    1,
                                                                    22,
                                                                    "Que sabor de helado desea en el banana split :",
                                                                )
                                                                sabor_elegido.append(
                                                                    sabores[sabor]
                                                                )
                                                            d2 = validar_opcion(
                                                                1,
                                                                2,
                                                                "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                            )
                                                            if d2 == "1":
                                                                agregar = {
                                                                    "tipo": tipos[d],
                                                                    "tamaño": tamaño_v,
                                                                    "sabor": sabor_elegido,
                                                                    "precio": precio,
                                                                }

                                                                total = (
                                                                    total +
                                                                    agregar["precio"]
                                                                )
                                                                dicTotal = {}
                                                                dicTotal["Total"] = total
                                                                factura_temporal.append(
                                                                    agregar)
                                                                cent = False
                                                                cent2 = False
                                                                d3 = validar_opcion(
                                                                    1,
                                                                    2,
                                                                    "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                                )
                                                                if d3 == "2":
                                                                    labrando = False

                                                else:
                                                    print(
                                                        "el siguiente tamaño de banan split no se encuentra disponible: ",
                                                        tamaño_v,
                                                    )
                                                    cent2 = False

                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )
                            elif d == "12":
                                if tipos2[d][1] == True:
                                    d1 = validar_opcion(
                                        1,
                                        2,
                                        "Deseas continuar en la seccion de paletas o regresar al menu de productos?\n1. Continuar \n2. Regresar \nIngrese aqui:  ",
                                    )
                                    if d1 == "1":
                                        cent2 = True
                                        while cent2 == True:
                                            print("sabores paletas: ")
                                            for i in sabores_paletas_base:
                                                valor1, valor2 = sabores_paletas_base[i][0]
                                                print(
                                                    "{0}. {1} {2} {3}".format(
                                                        i,
                                                        valor1,
                                                        valor2,
                                                        sabores_paletas_base[i][2],
                                                    )
                                                )
                                            sabor_elegido = []
                                            print(
                                                n_paletas, "para volver al menu")
                                            tamaño_h = validar_opcion(
                                                1, n_paletas, "que sabor de la paleta desea?: "
                                            )
                                            if tamaño_h != str(n_paletas):
                                                tamaño_v, precio = sabores_paletas_base[
                                                    tamaño_h
                                                ][0]
                                                sabor_elegido.append(
                                                    sabores_paletas[tamaño_h])
                                                d2 = validar_opcion(
                                                    1,
                                                    2,
                                                    "estas seguro de su sabor o deseas cambiar?\n1. Estoy segur@ \n2. Quiero cambiar mi sabor \nIngrese aqui:  ",
                                                )
                                                if d2 == "1":
                                                    agregar = {
                                                        "tipo": tipos[d],
                                                        "tamaño": tamaño_v,
                                                        "sabor": sabor_elegido,
                                                        "precio": precio,
                                                    }

                                                    total = total + \
                                                        agregar["precio"]
                                                    dicTotal = {}
                                                    dicTotal["Total"] = total
                                                    factura_temporal.append(
                                                        agregar)
                                                    cent = False
                                                    cent2 = False
                                                    d3 = validar_opcion(
                                                        1,
                                                        2,
                                                        "deseas hacer otro pedido o finalizar con la compra? \n1. Hacer otro pedido \n2. Finalizar con la compra \nIngrese aqui: ",
                                                    )
                                                    if d3 == "2":
                                                        labrando = False
                                            else:
                                                cent2 = False
                                else:
                                    print(
                                        "el siguiente producto no esta disponible en este momento:",
                                        tipos2[d][0],
                                    )

                            elif d == "13":
                                if len(subcategorias_nuevas) == 0:
                                    print(
                                        "Esta categoría no tiene productos"
                                    )
                                else:
                                    contSubCategoria = 1
                                    subcategoriasHabilitadas = []
                                    opcionesSubcategorias = ""
                                    for i in subcategorias_nuevas:
                                        subcategoriasHabilitadas.append(
                                            [
                                                subcategorias_nuevas[i][
                                                    0
                                                ]
                                                + " "
                                                + subcategorias_nuevas[
                                                    i
                                                ][2]
                                            ]
                                        )
                                        contSubCategoria += 1
                                    for i, subCategoria in enumerate(
                                        subcategoriasHabilitadas
                                    ):
                                        nombreSubCategoria = (
                                            subCategoria[0]
                                        )
                                        opcionesSubcategorias += f"{i+1}. {nombreSubCategoria.capitalize()}\n"
                                    preguntaSubCategoria = input(
                                        opcionesSubcategorias
                                        + "Elige una opción: "
                                    )
                                    if (
                                        preguntaSubCategoria.isdigit()
                                        and int(preguntaSubCategoria)
                                        > 0
                                        and int(preguntaSubCategoria)
                                        <= len(subcategoriasHabilitadas)
                                    ):
                                        if (
                                            len(
                                                subcategorias_nuevas[
                                                    int(
                                                        preguntaSubCategoria
                                                    )
                                                ][3]
                                            )
                                            == 0
                                        ):
                                            print(
                                                "Esta subcategoria no tiene productos"
                                            )
                                        else:
                                            if (
                                                subcategorias_nuevas[
                                                    int(
                                                        preguntaSubCategoria
                                                    )
                                                ][1]
                                                == True
                                            ):
                                                for (
                                                    i
                                                ) in subcategorias_nuevas[
                                                    int(
                                                        preguntaSubCategoria
                                                    )
                                                ][
                                                    3
                                                ]:
                                                    print(
                                                        subcategorias_nuevas[
                                                            int(
                                                                preguntaSubCategoria
                                                            )
                                                        ][
                                                            3
                                                        ][
                                                            i
                                                        ][
                                                            0
                                                        ],
                                                        " ",
                                                        subcategorias_nuevas[
                                                            int(
                                                                preguntaSubCategoria
                                                            )
                                                        ][
                                                            3
                                                        ][
                                                            i
                                                        ][
                                                            2
                                                        ],
                                                    )
                                            else:
                                                print(
                                                    "Esta subcategoría se encuentra deshabilitada"
                                                )
                                    else:
                                        print(
                                            "Opción inválida. Por favor, ingresa un número correspondiente a una opción válida."
                                        )
                                break
                            elif d == "14":
                                labrando = False
                        while True:
                            preguntaPago=input("1. Caja\n2. Online\n3. Online - Pago en caja\n4. Cancelar orden\nSelecciona una opción de pago: ")
                            if preguntaPago=="1":
                                if total != 0:
                                    Factura_unica.append(contador_general)
                                    Factura_unica.append(correoUsuario)
                                    Factura_unica.append(fecha_formateada)
                                    Factura_unica.append(factura_temporal)
                                    Factura_unica.append("Caja")
                                    Factura_unica.append(dicTotal)
                                    print(Factura_unica)
                                    t = threading.Thread(target=agregarFactura, args=(Factura_unica,))
                                    t.start()
                                    contador_general += 1
                                break
                            elif preguntaPago=="2":
                                if total != 0:
                                    Factura_unica.append(contador_general)
                                    Factura_unica.append(correoUsuario)
                                    Factura_unica.append(fecha_formateada)
                                    Factura_unica.append(factura_temporal)
                                    Factura_unica.append("Online")
                                    Factura_unica.append(dicTotal)
                                    facturas.append(Factura_unica)
                                    contador_general += 1
                                break
                            elif preguntaPago=="3":
                                if total != 0:
                                    Factura_unica.append(contador_general)
                                    Factura_unica.append(correoUsuario)
                                    Factura_unica.append(fecha_formateada)
                                    Factura_unica.append(factura_temporal)
                                    Factura_unica.append("Online - Pago en caja")
                                    Factura_unica.append(dicTotal)
                                    t = threading.Thread(target=agregarFactura, args=(Factura_unica,))
                                    t.start()
                                    contador_general += 1
                                break
                            elif preguntaPago=="4":
                                break
                            else:
                                print("Ingresa una opcion valida")
                    elif modificar == "4":
                        for factura in facturas:
                            if factura[1] == correoUsuario:
                                print("---------------------")
                                print("N°Factura: ", factura[0])
                                print("Nombre: ", factura[1])
                                print("Fecha: ", factura[2])
                                print("Detalles: ", factura[3])
                                print("Tipo de pago: ", factura[4])
                                print("Total: ",factura[-1]["Total"])
                                print("---------------------")
                        for factura in facturasCreadas:
                            if factura[1] == correoUsuario:
                                print("---------------------")
                                print("N°Factura: ", factura[0])
                                print("Nombre: ", factura[1])
                                print("Fecha: ", factura[2])
                                print("Detalles: ", factura[3])
                                print("Tipo de pago: ", factura[4])
                                print("Total: ",factura[-1]["Total"])
                                print("---------------------")
                        while True:
                            preguntaPedido = input("¿Qué pedido deseas cancelar? (Ingresa el número de factura o selecciona 0 para volver): ")
                            if preguntaPedido.isdigit():
                                preguntaPedido = int(preguntaPedido)
                                if preguntaPedido == 0:
                                    break
                                else:
                                    encontradoPendiente=False
                                    encontradoFacturas=False
                                    for facturaP in facturasCreadas:
                                        if facturaP[0]==preguntaPedido:
                                            encontradoPendiente=True
                                    for factura in facturas:
                                        if factura[0]==preguntaPedido:
                                            encontradoFacturas=True
                                            
                                    if encontradoPendiente==True:
                                        for i,facturaP in enumerate(facturasCreadas):
                                            if facturaP[0]==preguntaPedido:
                                                del facturasCreadas[i]
                                                print("Pedido cancelado")
                                    if encontradoFacturas==True:
                                        for usuarioFalla in usuarios:
                                            if usuarioFalla[0] == correoUsuario:
                                                print("Se agregó una falla")
                                                usuarioFalla[4] += 1
                                                if usuarioFalla[4] == 3:
                                                    for datos in usuarios:
                                                        datos[2] = False
                                                    print("Has sido baneado por superar el límite de cancelación de pedidos")
                                                    break
                                        for i, factura in enumerate(facturas):
                                            if factura[0]==preguntaPedido:
                                                del facturas[i]
                                                print("Pedido cancelado")
                                    if encontradoFacturas==False and encontradoPendiente==False:
                                        print("No se encontró la factura")
                            else:
                                print("Ingresa una opción válida")

                    else:
                        print("Por favor ingrese 1 o 2.")
    if not encontrado:
        while True:
            pregunta = (
                input(
                    "Lo siento, no pudimos encontrar tu cuenta. ¿Deseas crear una cuenta nueva? (si/no) "
                )
                .strip()
                .lower()
            )
            if pregunta == "si":
                agregarUsuario()
                break
            elif pregunta == "no":
                break
            else:
                print("Ingresa una opción valida")
