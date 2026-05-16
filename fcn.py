import csv
def menu():
    print("""
1) Agregar país.
2) Actualizar datos.
3) Buscar pais por nombre.
4) Filtrar países.
5) Ordenar países.
6) Mostrar estadísticas.
7) Salir.
          """)

def agregar_pais(paises):
    if paises is None:
        paises = []
        print("No hay países cargados en la lista.")
    while True:
        print("\n--- Agregar Nuevo País (Escriba 'salir' en nombre para terminar) ---")
        try:
            nombre = ""
            while not nombre:
                entrada = input("Ingrese el nombre del país: ").strip()
                
                if entrada.lower() == 'salir':
                    return paises
                
                nombre_pais = entrada.capitalize()
                
                # Verificamos si el nombre ya existe en la lista de diccionarios
                existe = any(isinstance(p, dict) and p.get('nombre') == nombre_pais for p in paises)
                
                if existe:
                    print(f"El país '{nombre_pais}' ya se encuentra en la lista.")
                    continue
                    
                
                nombre = nombre_pais

            poblacion = -1
            while poblacion < 0:
                poblacion = int(input(f"Ingrese la población de {nombre}: "))
                if poblacion < 0:
                    print("La población debe ser un número positivo.")

            superficie = -1
            while superficie < 0:
                superficie = int(input(f"Ingrese la superficie de {nombre} (km²): "))
                if superficie < 0:
                    print("La superficie debe ser un número positivo.")

            continente = ""
            while not continente:
                continente = input(f"Ingrese el continente de {nombre}: ").strip().capitalize()
                if not continente:
                    print("El continente no puede estar vacío.")

            nuevo_pais = {
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente 
            }
            paises.append(nuevo_pais)
            guardar_archivo(paises)
            print(f"\n¡{nombre} se ha registrado correctamente!")
        except ValueError:
            print("\nError: Ingrese solo números enteros para población y superficie.")
def guardar_archivo(lista):
    try:
        with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', "continente"])
            
            writer.writeheader()
            writer.writerows(lista)
            
        print('Archivo guardado.')
    except FileNotFoundError:
        print('El archivo no existe.')
    except PermissionError:
        print('No tiene permiso de escritura.')
def cargar_archivo():
    paises = []
    try:
        with open('paises.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                paises.append({
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': (fila['continente'])
                })
        print(f'Archivo cargado con {len(paises)} países.')
        return paises
    except FileNotFoundError:
        print('El archivo no existe')
        return []
    except PermissionError:
        print('No tenes permiso de lectura.')
        return []
def modificar_datos(lista):
    for pais in lista:
        print(f"País: {pais['nombre']} | Población: {pais['poblacion'] } | Superficie: {pais['superficie'] } | Continente: {pais['continente'] }")
        print("========================================================================================")
    print("""
    Menu para actulizar poblacion, superficie de un pais de la lista.
    1) Actualizar poblacion.
    2) Actualizar superficie.
    3) Salir.
          """)
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
def filtrar_paises(lista):
    america =[]
    while True:
        print("""
===Menu para filtrar paises por: ===
1) Continente.
2) Rango de poblacion.
3) Rango de superficie.
4) Salir.
              """)

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
        