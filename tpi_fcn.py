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

def agregar_pais (paises):
    while True:
        try:
            while True:
                nombre = input("Ingrese el nombre  del país que desea agreagar a la lista: ").strip().capitalize()
                poblacion = int(input(f"Ingrese la cantidad de poblacion para {nombre}:  "))
                superficie = int(input(f"Ingresa la superficie para {nombre}: "))
                continente = input(f"Ingrese el continente en donde se encuentra {nombre}: ").strip().capitalize()
                nuevo_pais = {
                    "nombre": nombre,
                    "poblacion": poblacion,
                    "superficie": superficie,
                    "continente": continente 
                }
                paises.append(nuevo_pais)
                guardar_archivo(paises)
                print ("Titulo cargado correctaente.")
        except ValueError:
            print("Error al ingresar los datos numericos..")
        return paises
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
        print('Archivo cargado.')
        
    except FileNotFoundError:
        print('El archivo no existe')
    except PermissionError:
        print('No tenes permiso de lectura.')
    except ValueError:
        print('La edad no es un numero.')