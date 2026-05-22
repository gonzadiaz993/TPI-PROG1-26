import csv
def filtrar_paises(lista):
    america =[]
    while True:
        print("""
===Menu para filtrar paises por: ===
1) Continente.
2) Rango de poblacion.
3) Rango de superficie.
4) Salir.\n""")
        opcion = input("Elija la opcion deseada: ")
        match opcion:
            case "1":
                filtrar_continentes(lista)
            case "2":
                rango_poblacion(lista)
            case "3":
                rango_superficie(lista)
            case "4":
                print("Volviendo al menu principal.")
                break
            case _:
                print("Error. Ingrese una opcion valida.")
def filtrar_continentes(lista):
    while True:
        print("""
======================================
          MENÚ DE CONTINENTES          
======================================
1. América.
2. Europa.
3. África.
4. Asia.
5. Oceanía.
6. Antártida.
7. Salir del programa.
======================================
""")
        opcion = input("Elija una opcion: ").strip()
        match opcion:
            case "1":
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

            case "2":
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
            case "3":
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
            case "4":
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
            case "5":
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
            case "6":
                print("la Antártida no contiene países." \
                " Es un continente, pero a diferencia de cualquier otro lugar de la Tierra, " \
                "no pertenece a ningún Estado y no tiene una población nativa ni un gobierno propio.")
            case "7":
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
                print("❌ Error: La población mínima no puede ser mayor que la máxima.")
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
                print("❌ Error: La superficie mínima no puede ser mayor que la máxima.")
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