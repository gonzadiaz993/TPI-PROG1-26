from fcn import*
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
            pass
        case "4":
            filtrar_paises(paises)
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Fin del programa. Hasta luego.")
            break
        case _:
            print("Opcion incorrecta. Intente nuevamente")