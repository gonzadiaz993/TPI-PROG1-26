from Funciones.__fcn__ import *
paises = cargar_archivo()
while True:
    limpiar_consola()
    estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden'),
        ('highlighted','bg:green fg:yellow'),
        ('pointer','fg:green bold'),
        ('question','fg:green bold')
    ])
    opcion = questionary.select(
    message='>>>>>>>> MENU <<<<<<<<\n',
    choices=['1. Agregar país ', '2. Actualizar datos ', '3. Buscar pais por nombre ', '4. Filtrar paises ', '5. Ordenar paises ', '6. Mostrar estadisticas ', '7. Salir '],
    style = estilo,
    pointer = '▶'
).ask()
    match opcion:
        case '1. Agregar país ':
            agregar_pais(paises)
        case '2. Actualizar datos ':
            modificar_datos(paises)
        case '3. Buscar pais por nombre ':
            buscar_pais(paises)
        case '4. Filtrar paises ':
            filtrar_paises(paises)
        case '5. Ordenar paises ':
            ordenar_paises(paises)
        case '6. Mostrar estadisticas ':
            estadisticas(paises)
        case '7. Salir ':
            limpiar_consola()
            print("Fin del programa. Hasta luego.")
            press_continuar()
            break