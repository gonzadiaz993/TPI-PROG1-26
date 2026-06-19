from questionary import Style
import questionary
from Funciones.guardar_archivo import*

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
                nombre_pais = input("Elija el pais que desea actualizar: ").strip().lower()
                encontrado = False
                for pais in lista:
                    if pais["nombre"].lower() == nombre_pais:
                        encontrado = True    
                        print(f"País: {pais['nombre']} | Población: {pais['poblacion'] }")
                        while True:
                            try:
                                actualizar_pob = int(input(f"Ingresa la poblacion nueva para {pais["nombre"]}: "))
                                validar_entero(actualizar_pob)
                                pais["poblacion"] = actualizar_pob
                                print("Poblacion actualizada.")
                                print(f"País: {pais['nombre']} | Población: {pais['poblacion'] }")
                                guardar_archivo(lista)
                                break
                            except ValueError:
                                print("Error solo numeros.")
                            except error_numero_negativo as e:
                                print(e)        
                if encontrado == False:
                    print("El pais no fue encontrado.")     
            case "2. Actualizar superficie. ":
                nombre_pais = input("Elija el pais que desea actualizar: ").strip().lower()
                encontrado = False
                for pais in lista:
                    if pais["nombre"].lower() == nombre_pais:
                        encontrado = True
                        print(f"País: {pais['nombre']} | Superficie: {pais['superficie'] }")
                        while True:
                            try:
                                actualizar_sup = int(input(f"Ingresa la Superficie nueva para {pais["nombre"]}: "))
                                validar_entero(actualizar_sup)
                                pais["superficie"] = actualizar_sup
                                print("Superficie actualizada.")
                                print(f"País: {pais['nombre']} | Superficie: {pais['superficie'] }")
                                guardar_archivo(lista)
                                break
                            except ValueError:
                                print("Error solo numeros.")
                            except error_numero_negativo as e:
                                print(e)
                if encontrado == False:
                    print("El pais no fue encontrado en la lista.")
                    
            case "3. Salir ":
                print("Finalizando. Volviendo al menu principal.")
                break
def validar_entero(poblacion):
    if poblacion <= 0 :
        raise error_numero_negativo("No se permiten numeros negativos o iguales a 0.")
class error_numero_negativo(Exception):
    pass