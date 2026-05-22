from Funciones.__fcn__ import *
paises = cargar_archivo()
while True:
    menu()
    opcion = input("Elija la opcion que desea ingresar: ")
    match opcion:
        case "1":
            agregar_pais(paises)
        case "2":
            modificar_datos(paises)
        case "3":
            buscar_pais(paises)
        case "4":
            filtrar_paises(paises)
        case "5":
            ordenar_paises(paises)
        case "6":
            estadisticas(paises)
        case "7":
            print("Fin del programa. Hasta luego.")
            break
        case _:
            print("Opcion incorrecta. Intente nuevamente")