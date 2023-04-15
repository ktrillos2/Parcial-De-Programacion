usuarios = [
    ["admin@email.com", "admin123", "admin"],
    ["cajero1@email.com", "cajero1", "cajero"],
    ["cajero2@email.com", "cajero2", "cajero"],
]

def iniciarSesion(usuario, contraseña):
    encontrado = False
    for i in usuarios:
        if i[0] == usuario and i[1] == contraseña:
            encontrado = True
            if i[2] == "admin":
                print("Ingresaste como admin")
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
