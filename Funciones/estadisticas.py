import csv
from Funciones.__fcn__ import *

PAISES = 'paises.csv'

def mayor_menor_poblacion(lista):
    with open(PAISES, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        mayor = 0
        pais_may = ""
        
        # Inicializamos en None para capturar el primer registro fácilmente
        menor = None 
        pais_men = ""
        
        total_poblacion = 0
        total_superficie = 0
        continente_unico = set()
        contador_paises = 0  # Contamos los países reales del CSV para los promedios

        for i in lector:
            num_poblacion = int(i['poblacion'])
            num_superficie = int(i['superficie'])
            continente_unico.add(i['continente'])
            contador_paises += 1
            
            # Sumatorias
            total_poblacion += num_poblacion
            total_superficie += num_superficie
            
            # Evaluar el MAYOR
            if num_poblacion > mayor:
                mayor = num_poblacion
                pais_may = i['nombre']
                
            # Evaluar el MENOR
            if menor is None or num_poblacion < menor:
                menor = num_poblacion
                pais_men = i['nombre']

        # Evitar división por cero si el archivo está vacío
        if contador_paises == 0:
            print("El archivo está vacío.")
            return

        print('='*65)
        print('ESTADISTICAS'.center(60))
        print('='*65)
        
        # Encabezados
        print('-- Pais con MAYOR poblacion --'.center(30), '-- Pais con MENOR poblacion --'.center(30))
        print(f'{Fore.YELLOW}{pais_may.center(30)}{Fore.RESET}{Fore.YELLOW}{pais_men.center(30)}{Fore.RESET}')
        
        # Valores de población individuales
        print('-- Poblacion --'.center(30), '-- Poblacion --'.center(30))
        mayor_str = f'{mayor:,}'
        menor_str = f'{menor:,}'
        print(f'{Fore.RED}{mayor_str.center(30)}{Fore.RESET}{Fore.RED}{menor_str.center(30)}{Fore.RESET}')
        print('-'*65)
        
        # Promedios (usando contador_paises en lugar de len(lista) para asegurar precisión)
        print('-- Promedio de poblacion por pais --'.center(60))
        promedio_pais = f'{total_poblacion // contador_paises:,}'
        print(f'{Fore.YELLOW}{promedio_pais.center(60)}{Fore.RESET}')
        
        print('-- Promedio de la superficie de los paises --'.center(60))
        promedio_superficie = f'{total_superficie / contador_paises:,.2f} km².'
        print(f'{Fore.YELLOW}{promedio_superficie.center(60)}{Fore.RESET}')
        
        print('-- Promedio paises por continentes --'.center(60))
        promedio_cont = f'{contador_paises / len(continente_unico):.2f}'
        print(f'{Fore.YELLOW}{promedio_cont.center(60)}{Fore.RESET}')

def estadisticas(lista):
    mayor_menor_poblacion(lista)
    press_continuar()