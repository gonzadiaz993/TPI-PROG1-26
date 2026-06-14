import csv
import questionary
from Funciones.__fcn__ import *
def filtrar_paises(lista):
    america =[]
    while True:
        estilo = Style([
            ('instruction','hidden'),
            ('qmark','hidden'),
            ('highlighted','bg:green fg:yellow'),
            ('pointer','fg:green bold'),
            ('question','fg:green bold')
        ])
        opcion = questionary.select(
            message='=== Menu para filtrar paises por ===',
            choices=['Continentes ','Poblacion ','Superficie ','Volver al Menu Principal '],
            style = estilo,
            pointer = '▶'
        ).ask()
        match opcion:
            case "Continentes ":
                filtrar_continentes(lista)
            case "Poblacion ":
                rango_poblacion(lista)
            case "Superficie ":
                rango_superficie(lista)
            case "Volver al Menu Principal ":
                print("Volviendo al menu principal.")
                return

def filtrar_continentes(lista):
    while True:
        estilo = Style([
            ('instruction','hidden'),
            ('qmark','hidden'),
            ('highlighted','bg:green fg:yellow'),
            ('pointer','fg:green bold'),
            ('question','fg:green bold')
        ])
        opcion = questionary.select(
            message='\n===========================\n   MENÚ DE CONTINENTES \n===========================',
            choices=['América ','Eruopa ','África ','Asia ','Oceanía ','Antártida ','Volver '],
            style = estilo,
            pointer = '▶'
        ).ask()
        
        match opcion:
            case 'América ':
                america =[]
                print("Paises en el continente Americano.")
                for pais in lista:
                    if pais["continente"] == "América":
                        america.append(pais["nombre"])
                    else:
                        continue
                for pais in america:
                    print("-----------------------------------------")
                    print(f"- {pais} - continente: América. ")

            case 'Eruopa ':
                europa =[]
                print("Paises en el continente Europeo.")
                for pais in lista:
                    if pais["continente"] == "Europa":
                        europa.append(pais["nombre"])
                    else:
                        continue
                for pais in europa:
                    print("-----------------------------------------")
                    print(f"- {pais} - continente: Europeo. ")
            case 'África ':
                africa =[]
                print("Paises en el continente Africano.")
                for pais in lista:
                    if pais["continente"] == "África":
                        africa.append(pais["nombre"])
                    else:
                        continue
                for pais in africa:
                    print("-----------------------------------------")
                    print(f"- {pais} - continente: Africano.")
            case 'Asia ':
                asia =[]
                print("Paises en el continente Asiatico.")
                for pais in lista:
                    if pais["continente"] == "Asia":
                        asia.append(pais["nombre"])
                    else:
                        continue
                for pais in asia:
                    print("-----------------------------------------")
                    print(f"- {pais} - continente: Asiatico.")
            case 'Oceanía ':
                oceania =[]
                print("Paises en el continente Océanico.")
                for pais in lista:
                    if pais["continente"] == "Oceanía":
                        oceania.append(pais["nombre"])
                    else:
                        continue
                for pais in oceania:
                    print("-----------------------------------------")
                    print(f"- {pais} - continente: Océanico.")
            case 'Antártida ':
                print("la Antártida no contiene países." \
                " Es un continente, pero a diferencia de cualquier otro lugar de la Tierra, " \
                "no pertenece a ningún Estado y no tiene una población nativa ni un gobierno propio.")
            case 'Volver ':
                print("Volviendo al menu continentes.")
                break
            case _:
                print("Error. Ingrese una opcion valida.")
def rango_poblacion(lista):
    while True:
        try:
            pob_min = int(input("Ingrese la población MÍNIMA: ").strip())
            pob_max = int(input("Ingrese la población MÁXIMA: ").strip())
            
            if pob_min > pob_max:
                print("Error: La población mínima no puede ser mayor que la máxima.")
                continue

        except ValueError:
            
            print("Error: Debes ingresar únicamente números enteros (sin puntos, comas ni letras).")
            continue

        print(f"\nResultados para población entre {pob_min:,} y {pob_max:,}:")
        print("--------------------------------------------------")
        
        contador_encontrados = 0
        for pais in lista:
            if pob_min <= pais["poblacion"] <= pob_max:
                print(f"- {pais['nombre']}: {pais['poblacion']:,} habitantes.")
                contador_encontrados += 1
        
        if contador_encontrados == 0:
            print("No se encontraron países en ese rango de población.")
        print("--------------------------------------------------")
        break
        
def rango_superficie(lista):
    while True:
        try:
            sup_min = int(input("Ingrese la superficie MÍNIMA: ").strip())
            sup_max = int(input("Ingrese la superficie MÁXIMA: ").strip())
            
            if sup_min > sup_max:
                print("Error: La superficie mínima no puede ser mayor que la máxima.")
                continue

        except ValueError:
            
            print("Error: Debes ingresar únicamente números enteros (sin puntos, comas ni letras).")
            continue

        print(f"\nResultados para superficie entre {sup_min:,} y {sup_max:,}:")
        print("--------------------------------------------------")
        
        contador_encontrados = 0
        for pais in lista:
            if sup_min <= pais["superficie"] <= sup_max:
                print(f"- {pais['nombre']}: {pais['superficie']:,}(km²).")
                contador_encontrados += 1
        
        if contador_encontrados == 0:
            print("No se encontraron países en ese rango de superfcie.")
        print("--------------------------------------------------")
        break