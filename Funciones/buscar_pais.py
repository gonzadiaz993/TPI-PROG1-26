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
            nombre_largo = 0
            for x in lector:
                paises = x['nombre']
                if pais_buscar == paises[:len(pais_buscar)]:
                    if nombre_largo < len(paises):
                        nombre_largo = len(paises)
            print(f'\n{'Paises':<{nombre_largo}} | {'Poblacion':<15} | {'Superficie':<12} | {'Continente':<6}')
            print('-'*80)
            archivo.seek(0)
            lector = csv.DictReader(archivo)
            nombre_largo =0
            for i in lector:
                paises = i['nombre']
                if pais_buscar == paises[:len(pais_buscar)]:
                    corte = paises.lower().find(pais_buscar.lower())# Aca empieza el fragmento buscado
                    sin_corte = len(pais_buscar) # El largo total del fragmento/total ingresado
                    parcial = paises[:corte + sin_corte]
                    # parcial -- [: 0 + sin_corte] -- Toma de 0 hasta el fragmento/total ingresado
                    total = paises[corte + sin_corte:]
                    # total -- Toma todo lo que quede de resto si es que hay
                    coloreado = f'{Fore.GREEN}{parcial}{Fore.RESET}{total}'
                    # colorado -- Fusiona los datos ingresador anteriormente
                    espacios_relleno = " " * max(0, nombre_largo - len(paises))
                    # espacios_relleno -- Calcula cuantos espacios en blanco le tiene que agregar al ancho de fila
                    dato_total = f'{coloreado}{espacios_relleno}'
                    # dato_total -- Junta el nombre ya coloreado con los espacios de relleno
                    print(f"{dato_total:<15} | {i['poblacion']:<15} | {i['superficie']:<12} | {i['continente']:<6}")
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
