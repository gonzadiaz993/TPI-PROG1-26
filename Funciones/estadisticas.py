import csv
from Funciones.__fcn__ import *
PAISES = 'paises.csv'

def mayor_menor_poblacion(lista):
    with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            mayor = 0
            menor = 0
            total_poblacion = 0
            total_superficie = 0
            continente_unico = set()
            for i in lector:
                num_poblacion = i['poblacion']
                num_superficie = i['superficie']
                cant_pais = len(i['nombre'])
                continente_unico.add(i['continente'])
                if mayor < int(num_poblacion):
                    mayor = int(num_poblacion)
                    pais_may = i['nombre']
                elif menor <= mayor:
                    menor = int(num_poblacion)
                    pais_men = i['nombre']
                total_poblacion += int(num_poblacion)
                total_superficie += int(num_superficie)
            print('='*65)
            print('ESTADISTICAS'.center(60))
            print('='*65)
            print(f'-- Pais con MAYOR poblacion --'.center(30),'-- Pais con MENOR poblacion --')
            print(f'{Fore.YELLOW}{pais_may.center(30)}{Fore.RESET}{Fore.YELLOW}{pais_men.center(30)}{Fore.RESET}')
            print(f'-- Poblacion Total --'.center(30),'-- Poblacion Total --'.center(30))
            mayor_str = str(f'{mayor:,}')
            menor_str = str(f'{menor:,}')
            print(f'{Fore.RED}{mayor_str.center(30)}{Fore.RESET}{Fore.RED}{menor_str.center(30)}{Fore.RESET}')
            print('-'*65)
            print(f'-- Promedio de poblacion por pais --'.center(60))
            promedio_pais = str(f'{total_poblacion // len(lista):,}')
            print(f'{Fore.YELLOW}{promedio_pais.center(60)}{Fore.RESET}')
            print(f'-- Promedio de la superficie de los paises --'.center(60))
            promedio_superficie = str(f'{total_superficie / len(lista):,} km².')
            print(f'{Fore.YELLOW}{promedio_superficie.center(60)}{Fore.RESET}')
            print('-- Promedio paises por continentes --'.center(60))
            promedio_cont = str(f'{len(lista) // len(continente_unico)}')
            print(f'{Fore.YELLOW}{promedio_cont.center(60)}{Fore.RESET}')
def estadisticas(lista):
    mayor_menor_poblacion(lista)
    press_continuar()