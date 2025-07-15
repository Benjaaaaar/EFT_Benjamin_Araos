productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                     }

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 }


def stock_marca(marca):    
    print(' marca')
    for clave,valor in stock.items():
        print(f'{clave}           {valor[0]}    {valor[1]}     {valor[2]}') 
    

def eliminar_producto():
    nombre=input('Ingrese Nombre del producto a Eliminar: ')
    for clave,valor in productos.items():
        if valor[0]==nombre:
            productos.pop
            print('producto eliminado con exito.')
            return
    print("producto no encontrado. No se pudo eliminar.")




while True:
    print("MENU PRINCIPAL")
    print("1. stock marca")
    print("2. busqueda por ram y precio.")
    print("3. eliminar producto.")
    print("4. salir.")
    opcion= input("ingrese una opcion: ")
    if opcion=="1":
        stock_marca()
    elif opcion=="2":
        print("funcion aun no disponible")
    elif opcion=="3":
        eliminar_producto()
    elif opcion=="4":
        print("programa finaizado")
        break
    else:
        print("opcion invalida. escoga una opcion valida")


        #un 3,4 me salva, viva el estoicismo

#skibidi toilet
#skibidi dongol
#aura max sigmaboyyy