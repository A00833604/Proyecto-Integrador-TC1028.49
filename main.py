#solo falta ponerlo en un mega while loop, (punto 7 y 8)
nombre_vendedor = ['Pablo', 'Julieta', 'Rolando']
datos_ventas_vendedor = [[0,2,0,1,0,0,0], [1,0,0,0,0,2,3], [0,0,1,2,0,4,0]] #tener datos de los modelos vendidos
modelos = [17, 22, 80, 15, 12, 44, 32]
descripcion_modelos = ['Sentra', 'Jetta', 'Forte', 'Mustang', 'Soul', 'Yaris', 'Camaro']
cantidad_existencia = [15,10,12,5,7,9,6]
ventas_modelos = [1,2,1,1,0,6,3]

#1
#se registra la venta y el vendedor 
def registrar_venta(): #Funciona
    #print de los modelos disponibles y seleccion de modelo vendido
    print('Modelos disponibles')
    for i in range(len(modelos)):
        print(modelos[i], end=' ')
    print()
    modelo_vendido = int(input('Ingresa el modelo: '))
    
    #print de la cantidad en existencia y cantidad vendida
    print('Cantidad en existencia de cada articulo: ')
    for i in range(len(cantidad_existencia)):
        print(cantidad_existencia[i], end=' ')
    print()
    cantidad_ventas = int(input('Ingresa la cantidad vendida: '))
    
    #ingresa datos del vendedor
    for i in range(len(nombre_vendedores)):
        print(nombre_vendedor[i], end=' ')
    print()
    vendedor = int(input('Vendedor (0, 1, 2): '))
    for modelo in range(len(cantidad_existencia)):
        if modelo_vendido == modelos[modelo]:
            #checa si la cantidad vendida es mayor a la que esta en existencia
            if (cantidad_existencia[modelo] - int(cantidad_ventas)) < 0:
                print('Los datos son incorrectos')
            else:
                cantidad_existencia[modelo] = cantidad_existencia[modelo] - int(cantidad_ventas)
                ventas_modelos[modelo] = int(cantidad_ventas)
                datos_ventas_vendedor[vendedor][modelo] = int(cantidad_ventas)
        elif (cantidad_ventas < 0):
            print('Los datos son incorrectos')
            break
        
    if modelo_vendido not in modelos:
        print('Los datos son incorrectos')

#2
#se registra la llegada del modelo
def registro_llegada_articulo(): #Funciona
    print('Modelos disponibles')
    for i in range(len(modelos)):
        print(modelos[i], end=' ')
    print()
    modelo_llegada = int(input('Ingresa el modelo: '))
    
    print('Cantidad en existencia de cada articulo: ')
    for i in range(len(cantidad_existencia)):
        print(cantidad_existencia[i], end=' ')
    print()
    cantidad_llegada = int(input('Cantidad que llegó: '))
        
    for modelo in range(len(cantidad_existencia)):
        if cantidad_llegada < 0:
            resultado = 'Los datos ingresados son incorrectos'
            break
        if modelo_llegada == modelos[modelo]:
            cantidad_existencia[modelo] += cantidad_llegada
    #checa si los datos son correctos
    if modelo_llegada not in modelos:
        print('Los datos ingresados son incorrectos')

#3
def consulta_inventario_disponible(): #Funciona
    print('Modelos:', end=' ')
    for i in range(len(modelos)):
        print(modelos[i], end=' ')
    print()

    print('Descripción:', end=' ')
    for i in range(len(modelos)):
        print(descripcion_modelos[i], end=' ')
    print()

    print('Cantidad en existencia:', end=' ')
    for i in range(len(modelos)):
        print(cantidad_existencia[i], end=' ')
    print()

#4
def articulo_mas_vendido(): #Funciona
    best_seller = 0
    contador = 0
    for i in range(len(ventas_modelos)):
        if ventas_modelos[i] > best_seller:
            best_seller = ventas_modelos[i]
    for i in range(len(ventas_modelos)):
        if best_seller == ventas_modelos[i]:
            contador = i
    print(f'El modelo más vendido es: {modelos[contador]}, {descripcion_modelos[contador]}, \
con {ventas_modelos[contador]} ventas')

#5
def mejor_vendedor(): #Funciona
    best_seller = ''
    ventas_final = 0
    contador = 0
    for i in range(len(datos_ventas_vendedor)):
        ventas_temp = 0
        for x in range(len(datos_ventas_vendedor[i])):
            ventas_temp += datos_ventas_vendedor[i][x]
        if ventas_temp > ventas_final:
            ventas_final = ventas_temp
            contador = i
    print(f'El mejor vendedor fue: {nombre_vendedor[contador]}, con {ventas_final} ventas')

#6
def reporte_ventas(): #Funciona
    print('Modelo', end=' ')
    for i in range(len(modelos)):
        print(modelos[i], end=' ')
    print()

    for i in range(len(datos_ventas_vendedor)):
        print(nombre_vendedor[i], end=' ')
        for x in range(len(datos_ventas_vendedor[i])):
            print(datos_ventas_vendedor[i][x], end=' ')
        print()
