import csv
from Funciones.guardar_archivo import* 
def modificar_datos(lista):
    for pais in lista:
        print(f"País: {pais['nombre']} | Población: {pais['poblacion'] } | Superficie: {pais['superficie'] } | Continente: {pais['continente'] }")
        print("========================================================================================")
    print("""
    Menu para actulizar poblacion, superficie de un pais de la lista.
    1) Actualizar poblacion.
    2) Actualizar superficie.
    3) Salir.\n""")
    while True:
        opcion = input("Elija una opcion del menu: ").strip()
        match opcion:
            case "1":
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
            case "2":
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
            case "3":
                print("Finalizando. Volviendo al menu principal.")
                break
            case _:
                print("Opcion incorrecta intente nuevamente.")