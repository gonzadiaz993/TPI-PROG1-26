import csv
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