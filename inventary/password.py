while True:
    contraseña_guardada = input("Cree una contraseña (mínimo 8 caracteres): ")
    
    if len(contraseña_guardada) > 8:
        print("Contraseña creada correctamente.\n")
        break
    else:
        print("Error: la contraseña debe tener más de 8 caracteres.\n")

# Número de intentos permitidos
intentos = 3

# Solicitar la contraseña nuevamente
while intentos > 0:
    contraseña_ingresada = input("Ingrese nuevamente la contraseña: ")

    if contraseña_ingresada == contraseña_guardada:
        print("Contraseña correcta. Acceso permitido.")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta.")
        print(f"Intentos restantes: {intentos}\n")

# Si se agotaron los intentos
if intentos == 0:
    print("Has superado el número máximo de intentos. Programa finalizado.")
