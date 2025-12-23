while True:

    print('-----MENU DE INVENTARIO-----')
    print('1. Agregar producto')
    print('2. Mostrar productos')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Estadistica de productos')
    print('6. Buscar producto')
    print('7. Agregar productos desde CSV')
    print('8. Cargar productos desde CSV')
    print('9. Salir')   

    opcion = int(input('Ingrese una opcion:\n '))

    if opcion ==1:                          #funciones del json menu:
        agregar_producto()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        actualizar_productos()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        estadistica()
    elif opcion == 6:
        buscar_producto()
    elif opcion == 7:
        Agregar_csv()
    elif opcion == 8:
        cargar_csv()
    elif opcion == 9:
        print('Saliste del programa')
        break
    else:
        print('Opcion invalida')
        break