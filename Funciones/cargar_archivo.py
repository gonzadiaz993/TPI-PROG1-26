import csv
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