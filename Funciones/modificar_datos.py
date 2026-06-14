from questionary import Style
import questionary

def modificar_datos(lista):
    for pais in lista:
        print(f"País: {pais['nombre']:<31} | Población: {pais['poblacion']:<15} | Superficie: {pais['superficie']:<12} | Continente: {pais['continente']:<6}")
        print("="*120)
    while True:
        estilo = Style([
            ('instruction','hidden'),
            ('qmark','hidden'),
            ('highlighted','bg:green fg:yellow'),
            ('pointer','fg:green bold'),
            ('question','fg:green bold')
        ])
        opcion = questionary.select(
        message='>>>>>>>> MENU <<<<<<<<\n',
        choices=['1. Actualizar poblacion. ', '2. Actualizar superficie. ', '3. Salir '],
        style = estilo,
        pointer = '▶'
    ).ask()
        match opcion:
            case "1. Actualizar poblacion. ":
                nombre_pais = input("Elija el pais que desea actualizar: ").strip().capitalize()
                for pais in lista:
                    if pais["nombre"] == nombre_pais:
                        print(f"País: {pais['nombre']} | Población: {pais['poblacion'] }")
                        while True:
                            try:
                                actualizar_pob = int(input(f"Ingresa la poblacion nueva para {nombre_pais}: "))
                                pais["poblacion"] = actualizar_pob
                                print("Poblacion actualizada.")
                                guardar_archivo(lista)
                                break
                            except ValueError:
                                print("Error solo numeros.")
                    else:
                        print("El pais no fue encontrado.")
                        break
            case "2. Actualizar superficie. ":
                nombre_pais = input("Elija el pais que desea actualizar: ").strip().capitalize()
                for pais in lista:
                    if pais["nombre"] == nombre_pais:
                        print(f"País: {pais['nombre']} | Superficie: {pais['superficie'] }")
                        while True:
                            try:
                                actualizar_sup = int(input(f"Ingresa la Superficie nueva para {nombre_pais}: "))
                                pais["superficie"] = actualizar_sup
                                print("Superficie actualizada.")
                                guardar_archivo(lista)
                                break
                            except ValueError:
                                print("Error solo numeros.")
            case "3. Salir ":
                print("Finalizando. Volviendo al menu principal.")
                break