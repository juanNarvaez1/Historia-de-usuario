inventario = []  


def agg_productos():
    """
    """
    
    nombre = input("Nombre del producto: ").strip().lower()
    cantidad = int(input("Cantidad del producto: "))
    precio = float(input("Precio del producto: "))

    
    inventario.append({
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    })


def act():
    nombre = input("Producto que desea actualizar: ").strip().lower()

    for item in inventario:
        if item["nombre"] == nombre:
            
            try:
                item["cantidad"] = int(input("Nueva cantidad: "))
                item["precio"] = float(input("Nuevo precio: "))

                print("Producto actualizado.")
            except ValueError:
                
                print("Los datos ingresados no son válidos.")
            return