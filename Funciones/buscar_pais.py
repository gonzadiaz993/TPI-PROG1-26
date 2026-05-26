import csv
from Funciones.agregar_pais import *
from Funciones.en_consola import *
from Funciones.excepciones import *
PAISES = 'paises.csv'
def buscar_pais(lista):
    try:
        pais_buscar = input('Ingrese el nombre del pais a buscar: ').strip().capitalize()
        dato_vacio(pais_buscar)
    except ValueError:
        print('Dato incorrecto')
    except InputVacio as e:
        print(f'Error. {e}')
    else:
        encontrado = False
        with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            print(f'\n{'Paises':<15} | {'Poblacion':<15} | {'Superficie':<12} | {'Continente':<6}')
            print('-'*80)
            for i in lector:
                if pais_buscar == i['nombre'] or (pais_buscar in i['nombre']):
                    print(f"{i['nombre']:<15} | {i['poblacion']:<15} | {i['superficie']:<12} | {i['continente']:<6}")
                    encontrado = True
            if not encontrado:
                print(f'El pais "{Fore.RED}{pais_buscar}{Fore.RESET}" no se ha encontrado')
                print('\n ¿Quire agregarlo a la lista?')
                estilo = Style([
                    ('instruction','hidden'),
                    ('qmark','hidden'),
                    ('highlighted','bg:green fg:yellow'),
                    ('pointer','fg:green bold'),
                    ('question','fg:green bold')
                ])
                opcion = questionary.select(
                    message='',
                    choices=['SI ','NO '],
                    style = estilo,
                    pointer = '▶'
                ).ask()
                if opcion == 'SI ':
                    agregar_pais(lista)
                elif opcion == 'NO ':
                    return
    finally:
        press_continuar()
