nombre = input("Ingrese el nombre del producto: ")

# Validación para el precio (debe ser un número decimal/float)
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
            continue
        break
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio.")

# Validación para la cantidad (debe ser un número entero/int)
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            continue
        break
    except ValueError:
        print("Error: Ingrese un número entero válido para la cantidad.")

# Bloque: Operación matemática (Task 3)
# Calculamos el costo total multiplicando las variables numéricas
costo_total = precio * cantidad

# Bloque: Mostrar resultados en consola (Task 4)
# Imprimimos el resumen de la operación con un formato claro
print("\n" + "="*30)
print(f"RESUMEN DEL REGISTRO")
print(f"Producto: {nombre} | Precio: {precio:.2f} | Cantidad: {cantidad} | Total: {costo_total:.2f}")
print("="*30)

# Bloque: Documentación general (Task 5)
"""
DESCRIPCIÓN GENERAL DEL PROGRAMA:
Este script permite registrar productos de forma individual capturando su nombre, 
precio y cantidad mediante la consola. 
Incluye un sistema de manejo de errores (try-except) para asegurar que los datos 
numéricos sean válidos antes de realizar el cálculo del costo total.
Finalmente, presenta un reporte resumido al usuario.
"""