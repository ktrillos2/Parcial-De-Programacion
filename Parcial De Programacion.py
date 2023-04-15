usuarios = [
    ["admin@email.com", "admin123", "admin",[]],
    ["cajero1@email.com", "cajero1", "cajero",[]],
    ["cajero2@email.com", "cajero2", "cajero",[]],
]

def agregarCajero():
    usuario=input("Ingrese correo")
    contraseña=input("Ingrese contraseña")
    nombre=input("Ingrese nombre")
    while True:
        documento=input("Ingrese documento")
        if documento.isDigit():
            if len(documento) < 8:
                print("Documento muy corto")
            elif len(documento)>10:
                print("Documento muy largo")
            else:
                break
        else:
            print("Ingresa un numero valido")
    usuarios.append([usuario,contraseña,"cajero",[nombre,documento,True]])
    
    

def iniciarSesion(usuario, contraseña):
    encontrado = False
    for i in usuarios:
        if i[0] == usuario and i[1] == contraseña:
            encontrado = True
            if i[2] == "admin":
                while True:
                        preguntaAdmin = input("1. Cajeros\n2. Ver productos\n3. Ventas\nSelecciona una opción: ")
                        if preguntaAdmin=="1":
                            opcionesCajeros=True
                            while opcionesCajeros:
                                    preguntaCajero=input("1. Eliminar Cajeros\n2. Agregar Cajero\n3. Modificar Cajero*\n4. Regresar al menu anterior\nSelecciona una opción: ")
                                    if preguntaCajero=="1":
                                        ##Codigo de eliminar cajero
                                        break
                                    elif preguntaCajero=="2":
                                        agregarCajero()
                                        break
                                    elif preguntaCajero=="3":
                                        opcionesCajeros=False
                                        break
                                    else:
                                        print("Ingresa un numero valido")
                            break
                        elif preguntaAdmin=="2":
                            ##codigo de productos
                            break
                        elif preguntaAdmin=="3":
                            ##codigo de ventas
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
