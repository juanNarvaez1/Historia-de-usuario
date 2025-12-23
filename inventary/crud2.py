import json
import os
import csv

lista = 'productos.json'
productos=[]

# ---------------------------
# LEER DATOS
# ---------------------------

def leer_productos():
    if not os.path.exists(lista):
        print('No se encuentra la ruta')

    try:
        with open(lista, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# ---------------------------
# GUARDAR DATOS
# ---------------------------

def guardar_productos(productos):
    with open(lista, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)

# ---------------------------
# CREAR PRODUCTO
# ---------------------------

def agregar_producto():#primer funcion añadir productos. 
    #agregar producto al inventario
    print('------Agrega un producto------')

    productos = leer_productos()

    while True:
        nombre = input('Ingrese el nombre del producto: ').lower()
        
        if all(c.isalnum() or c == " " for c in nombre): #Con esto podemos determinar si la palabra tienes caracter especial 
    
            if any(t in nombre for t in "áéíóú"):
                print('No se permiten tildes')
            else:
                break
        else:
            print('No se permiten caracteres especiales.')

    while True:

        try:
            precio = float(input('Ingresa el valor del producto: '))
            if precio >0:
                print('El precio fue ingresado')
                break
            else:
                print('Deben ser número positivos')
        except ValueError:
            print('Ingresa valores númericos')

    while True:
        try:
            cantidad = int(input('Ingresa la cantidad del producto: '))
            if cantidad >0:
                print('Cantidad ingresada Correctamente.')
                break
            else:
                print('Ingrese valores números positivos ')
        except ValueError:
            print('Ingrese números. ')

    nuevo_id = 1 if not productos else productos[-1]["id"] + 1

    nuevo ={
        'id': nuevo_id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad,
    }
    productos.append(nuevo)
    guardar_productos(productos)
  
    print(f'El producto {nombre} se agregó correctamente.\n')


# ---------------------------
# MOSTRAR PRODUCTO
# ---------------------------

def mostrar():

    print('------Agrega un producto------')
    productos = leer_productos()

    if not productos:
        print("\nNo hay productos registrados.\n")
        return

    print("\n LISTA DE PRODUCTOS: ")
    for pro in productos:
        print(f"ID: {pro['id']} | Nombre: {pro['nombre']} | Precio: {pro['precio']}   | Cantidad: {pro['cantidad']}")
    print()

# ---------------------------
# ACTUALIZAR PRODUCTO
# ---------------------------

def actualizar_productos():
    productos = leer_productos()
    if not productos:
        print('No hay datos para actualizar.')
        return
    
    mostrar()
    try:
        idproducto = int(input('Ingrese ID del producto que deseas actualizar: '))
    except:
        print('ID invalido.\n')

    for pro in productos:
        if pro['id'] == idproducto:
            nuevo_precio = float(input('Ingrese el nuevo precio: '))
            nueva_cantidad = int(input('Ingrese el nuevo Cantidad: '))

            if nuevo_precio:
                pro['precio'] = nuevo_precio

            if nueva_cantidad:
                if nueva_cantidad >= 0: 
                    pro['cantidad'] = nueva_cantidad
                else:
                    print('Cantidad invalida')
            productos = leer_productos()
            guardar_productos(productos)
            print('Producto actualizo correctamente\n')

   
                
# ---------------------------
# ELIMIAR PRODUCTO
# ---------------------------

def eliminar_producto():
    productos = leer_productos()

    if not productos:
        print('No hay productos por eliminar')
        return
    mostrar()
    try:
        idproducto = int(input('Ingrese el ID del producto que deseas eliminar: '))
    except:
        print('ID no encontrado')
        return
    
    nuevos = [pro for pro in productos if pro["id"] != idproducto]

    if len(nuevos) == len(productos):
        print('No existe un producto con ese ID')
        return
    
    guardar_productos(nuevos)
    print('Producto eliminado\n')

# ---------------------------
# ESTADISTICA DE PRODUCTO
# ---------------------------

def estadistica():
    productos = leer_productos()
    
    if not productos:
        print('No hay poductos que calcular')
        return
    mostrar()

    subtotal = lambda p: p["precio"] * p["cantidad"]

    # 1. Unidades totales
    unidades_totales = sum(p["cantidad"] for p in productos)

    # 2. Valor total del inventario
    valor_total = sum(subtotal(p) for p in productos)

    # 3. Producto más caro
    producto_mas_caro = max(productos, key=lambda p: p["precio"])

    # 4. Producto con mayor stock
    producto_mayor_stock = max(productos, key=lambda p: p["cantidad"])

    # Mostrar estadísticas
    print("\n ESTADÍSTICAS DEL INVENTARIO")
    print("-----------------------------------")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)\n")

# ---------------------------
# buscar DE PRODUCTO
# ---------------------------

def buscar_producto():
    print('buscar producto')

    #mostrar()
    print("\n")
    busqueda = int(input('Ingrese el ID a buscar: '))
    productos = leer_productos()
    encontrados= []
    for pro in productos:
        if busqueda == int(pro['id']):
            encontrados.append(pro)

    if encontrados:
        print('\nProductos encontrados:')
        for pro in encontrados:
            print(f"ID: {pro['id']} | Nombre: {pro['nombre']} | Precio: {pro['precio']} | Cantidad: {pro['cantidad']}")
    else:
        print('No se encontraron productos con ese ID.\n')