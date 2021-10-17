ventas = []
articulos = []
vendedores = [['Placeholder']]
vendedor_articulo = []
cantidad_articulo =[]
inventario_articulos = []
#agrega un articulo a la lista ventas, quita el articulo de la lista articulos
def def_art_vendido(articulo):
    ventas.append(articulo)
    if(articulo in articulos):
        articulos.remove(articulo)

#total articulos no vendidos
def print_tot_art_no_vend():
    for i in articulos:
        print("Articulos")
        print(f"{articulos[i]}")
    
#agrega articulos
def agregar_articulos(articulo):
    if articulo not in articulos:
        articulos.append(articulo)

#checa si los articulos se repiten, y agrega un contador de cuantos hay en la lista
def agrega_contador_art_repetidos(articulos):
        for i in range(len(articulos)):
            if articulos[i] in articulos[:i]:
                articulos[i] = articulos[i] + " x " + str(i)

#checa si hay articulos repetidos, los devuelve en una lista,
#el primer item es la cantidad total de repetidos
def checa_art_repetidos(articulos):
    lista_art_repetidos = []
    contador_art_repetidos = 0
    
    for i in range(len(articulos)):
            if articulos[i] in articulos[:i]:
                lista_art_repetidos.append(articulos[i])
                contador_art_repetidos += 1
    lista_art_repetidos.insert(0,"Total de articulos repetidos: " + contador_art_repetidos)
    return lista_art_repetidos



def agregar_vendedor(vendedor):
    if vendedor not in vendedores:
        vendedores.append(vendedor)

#para acceder a los pointers i, x necesitas declararlos antes, no funciona
i = 0
x = 0
def agregar_vendedor_articulo(vendedores, articulos):
    for list in vendedor_articulo:
        i = 0
        i += 1
        x = 0
        for number in list:
            x += 1
            print(vendedor_articulo[i-1][x-1])

#Agrega la cantidad, descripcion y modelo del articulo
#Si el modelo esta repetido, se actualiza la desc y la cantidad
#se necesita conocer la cantidad de articulos antes de llamar la funcion,
            #declara la cantidad antes
cantidad_articulos = 1
inventario_articulos = [['Placeholder']]
def agregar_articulo_inventario():
    for i in range(cantidad_articulos):
        modelo = input("Modelo: ")
        descripcion = input("Descripción: ")
        cantidad_existencia = input("Cantidad en existencia: ")
        
        if modelo not in inventario_articulo[i-1][:i]:
            inventario_articulo.append([modelo, descripcion, cantidad_existencia])
        elif modelo in inventario_articulo[i-1][:i]:
            inventario_articulo[i-1] = [modelo, descripcion, cantidad_existencia]
        if inventario_articulo[0][0] == 'Placeholder':
            inventario_articulo.pop(0)


#para agregar la infor de un vendedor, desde 0
#definir la cantidad de vendedores antes de llamar la función
cantidad_vendedores = 2
def agregar_info_vendedor():
    for i in range(cantidad_vendedores):
        lista_art_vendedor = []
        nombre_vendedor = input(f"Nombre del vendedor {i}: ")
        for x in range(cantidad_articulos):
            articulo = input(f"Ventas del articulo {inventario_articulos[x][0]}: ")
            lista_art_vendedor.append(articulo)
        if nombre_vendedor not in vendedores[i-1][:i]:
            vendedores.append([nombre_vendedor, lista_art_vendedor])
            
    if vendedores[0] == ['Placeholder']:
        vendedores.pop(0)
