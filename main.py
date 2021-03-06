from time import sleep #se implementan sleeps despues de la muestra de datos (a partir de la linea 175)
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
    for i in range(len(nombre_vendedor)):
        print(nombre_vendedor[i], end=' ')
    print()
    vendedor = int(input('Vendedor (0, 1, 2): '))
    incorrecto = False
    for modelo in range(len(cantidad_existencia)):
        if modelo_vendido == modelos[modelo]:
            #checa si la cantidad vendida es mayor a la que esta en existencia
            if (cantidad_existencia[modelo] - int(cantidad_ventas)) < 0:
                incorrecto = True
            else:
                cantidad_existencia[modelo] = cantidad_existencia[modelo] - int(cantidad_ventas)
                ventas_modelos[modelo] = int(cantidad_ventas)
                datos_ventas_vendedor[vendedor][modelo] = int(cantidad_ventas)
        elif (cantidad_ventas < 0):
            incorrecto = True
            break
        
    if modelo_vendido not in modelos:
        incorrecto = True
    if incorrecto:
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
    cantidad_llegada = int(input('Cantidad que lleg??: '))
        
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

    print('Descripci??n:', end=' ')
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
    print(f'El modelo m??s vendido es: {modelos[contador]}, {descripcion_modelos[contador]}, \
con {ventas_modelos[contador]} ventas')

#5
def mejor_vendedor(): #Funciona
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

#7
def porcentaje_de_ventas(): #Funciona
    total_ventas = 0
    cantidad_cada_vendedor = []
    for i in range(len(nombre_vendedor)):
        cantidad_cada_vendedor.append(0)
        for j in range(len(datos_ventas_vendedor[i])):
            cantidad_cada_vendedor[i] += datos_ventas_vendedor[i][j]
            total_ventas += datos_ventas_vendedor[i][j]
    print("Los porcentajes de cu??ntos vendi?? cada vendedor")
    for i in range(len(cantidad_cada_vendedor)):
        print(f"{nombre_vendedor[i]} : {cantidad_cada_vendedor[i] / total_ventas * 100 : .2f}% ({cantidad_cada_vendedor[i]}/{total_ventas})")

opcion = 0

while opcion != 8:
    print("---------------------- Menu ----------------------")
    print("1. Registrar una venta.")
    print("2. Registrar llegada de art??culos al almac??n.")
    print("3. Consultar el inventario disponible.")
    print("4. Consultar cu??l es el modelo del art??culo m??s vendido.")
    print("5. Consultar cu??l vendedor ha vendido una cantidad mayor de art??culos.")
    print("6. Reporte de ventas de un vendedor.")
    print("7. Los porcentajes de cu??ntos vendi?? cada vendedor.")
    print("8. Salir")
    
    opcion = int(input("Elige tu opci??n: "))
    
    if opcion == 1:
        registrar_venta()
    elif opcion == 2:
        registro_llegada_articulo()
    elif opcion == 3:
        consulta_inventario_disponible()
    elif opcion == 4:
        articulo_mas_vendido()
    elif opcion == 5:
        mejor_vendedor()
    elif opcion == 6:
        reporte_ventas()
    elif opcion == 7:
        porcentaje_de_ventas()
    elif opcion != 8:
        print("Opci??n inv??lida")
    sleep(.5) #el sleep es para que el menu no vengan de inmediato
    print()
print("Gracias")
print()
sleep(0.5)
print("Equipo conformado por:")
sleep(0.5)
nombres = [['Marco Ottavio Podesta Vezzali, A00822604'], ['Won Huh, A01178010'], ['Valeria Becerra Barraza, A00833860'], ['Montserrat Ballesteros Amador, A01284844']]
for i in range(len(nombres)):
    for x in range(len(nombres[i])):
        for char in nombres[i][x]:
            sleep(0.018)
            print(char, end='')
    print()
