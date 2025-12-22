# ============================================
# Sistema básico de gestión de inventario
# ============================================

# Lista global donde se almacenarán los productos
inventario = []


def agregar_producto():
    """
    Solicita al usuario los datos de un producto
    y lo agrega al inventario como un diccionario.
    """
    print("\n--- Agregar producto ---")

    nombre = (input ("Ingrese el nombre del producto: "))

    # Validación del precio
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingrese un valor numérico válido.")

    # Validación de la cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingrese un número entero válido.")

    # Crear el producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar el producto al inventario
    inventario.append(producto)
    print("Producto agregado correctamente.")


def mostrar_inventario():
    """
    Muestra todos los productos almacenados
    en el inventario.
    """
    print("\n--- Inventario ---")

    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(
                f"Producto: {producto['nombre']} | "
                f"Precio: {producto['precio']} | "
                f"Cantidad: {producto['cantidad']}"
            )


def calcular_estadisticas():
    """
    Calcula y muestra:
    - El valor total del inventario
    - La cantidad total de productos registrados
    """
    print("\n--- Estadísticas del inventario ---")

    if not inventario:
        print("No hay productos en el inventario.")
        return

    valor_total = 0
    cantidad_total = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        cantidad_total += producto["cantidad"]

    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {cantidad_total}")


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")


# ============================================
# Programa principal
# ============================================

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")


# ============================================
# Resumen final
# ============================================
# Este programa permite gestionar un inventario
# usando listas, diccionarios, condicionales,
# bucles y funciones. El objetivo de la semana
# es practicar validación de datos, estructuras
# de control y organización del código.
