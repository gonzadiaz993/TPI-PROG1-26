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
    