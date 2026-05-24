from Funciones.__fcn__ import *

paises = cargar_archivo()
while True:
    limpiar_cosola()
    estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden')
    ])
    opcion = questionary.select(
    
    message='============== MENU ================',
    choices=['1. Agregar país', '2. Actualizar datos', '3. Buscar pais por nombre', '4. Filtrar paises', '5. Ordenar paises', '6. Mostrar estadisticas', '7. Salir'],
    style = estilo
).ask()
    match opcion:
        case '1. Agregar país':
            agregar_pais(paises)
        case '2. Actualizar datos':
            modificar_datos(paises)
        case '3. Buscar pais por nombre':
            buscar_pais(paises)
        case '4. Filtrar paises':
            filtrar_paises(paises)
        case '5. Ordenar paises':
            ordenar_paises(paises)
            print()
            on_press()
        case '6. Mostrar estadisticas':
            estadisticas(paises)
        case '7. Salir':
            limpiar_cosola()
            print("Fin del programa. Hasta luego.")
            on_press()
            break