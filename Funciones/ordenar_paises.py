import csv
from Funciones.en_consola import *
from Funciones.__fcn__ import *
PAISES = 'paises.csv'
def por_nombre(fila):
    return fila[0]

def caso_1():
    estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden'),
        ('highlighted','bg:green fg:yellow'),
        ('pointer','fg:green bold'),
        ('question','fg:green bold')
    ])
    opcion = questionary.select(
        message='En que orden lo quiere mostrar: ',
        choices=[
            '. A - Z',
            '. Z - A',
            '. Volver'
        ],
        pointer = '▶',
        style=estilo
    ).ask()
    if opcion == '. Volver':
        press_continuar()
        limpiar_consola()
        return
    with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        usar = []
        for i in lector:
            usar.append([i['nombre'],i['poblacion'],i['superficie'],i['continente']])
        if opcion == '. A - Z':
            volt = False
            az = 'A-Z'
        elif opcion == '. Z - A':
            az = 'Z-A'
            volt = True
        try:
            print(f'\n{Fore.YELLOW}Paises{Fore.RESET:<28}{Fore.RED}{az}{Fore.RESET} | {"Poblacion":<15} | {"Superficie":<12} | {"Continentes":<6}')
            print('-'*80)
            for x in sorted(usar, reverse = volt):
                print(f"{Fore.YELLOW}{x[0]:<32}{Fore.RESET} | {int(x[1]):<15,} | {int(x[2]):<12,} | {x[3]:<6}")
        except UnboundLocalError:
            print('\n Saliendo al menu principal \n')
        else:
            print()
            press_continuar()
            limpiar_consola()

def caso_2():
    estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden'),
        ('highlighted','bg:green fg:yellow'),
        ('pointer','fg:green bold'),
        ('question','fg:green bold')
    ])
    opcion = questionary.select(
        message='En que orden lo quiere mostrar: ',
        choices=[
            '. Mayor a Menor',
            '. Menor a Mayor',
            '. Volver'
        ],
        style=estilo
    ).ask()
    if opcion == '. Volver':
        press_continuar()
        limpiar_consola()
        return
    with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        usar = []
        for i in lector:
            usar.append([int(i['poblacion']),i['nombre'],i['superficie'],i['continente']])
        if opcion == '. Mayor a Menor':
            volt = True
            az = 'Mayor a Menor'
        elif opcion == '. Menor a Mayor':
            az = 'Menor a Mayor'
            volt = False
        try:
            print(f'\n{'Paises':<32} | {Fore.YELLOW}{'Poblacion'}{Fore.RESET:<15}{Fore.RED}{az}{Fore.RESET} | {'Superficie':<12} | {'Continentes':<6}')
            print('-'*100)
            for x in sorted(usar, reverse=volt):
                print(f"{x[1]:<32} | {Fore.YELLOW}{int(x[0]):<32,}{Fore.RESET} | {int(x[2]):<12,} | {x[3]:<6}")
        except UnboundLocalError:
            print('\n Saliendo al menu principal \n')
        else:
            print()
            press_continuar()
            limpiar_consola()

def caso_3():
    estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden'),
        ('highlighted','bg:green fg:yellow'),
        ('pointer','fg:green bold'),
        ('question','fg:green bold')
    ])
    opcion = questionary.select(
        message='Como quiere ordenar el Tamaño de la Superficie: ',
        choices=['. Mayor a Menor','. Menor a Mayor', '. Volver'],
        style=estilo
    ).ask()
    if opcion == '. Volver':
        press_continuar()
        limpiar_consola()
        return
    with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        usar = []
        for i in lector:
            usar.append([int(i['superficie']),i['nombre'],i['poblacion'],i['continente']])
        if opcion == '. Mayor a Menor':
            volt = True
            az = 'Mayor a Menor'
        elif opcion == '. Menor a Mayor':
            az = 'Menor a Mayor'
            volt = False
        try:
            print(f'\n{'Paises':<32} | {'Poblacion':<15} | {Fore.YELLOW}{'Superficie':<12}{Fore.RESET}{Fore.RED}{az}{Fore.RESET} | {'Continentes':<6}')
            print('-'*100)
            for x in sorted(usar, reverse=volt):
                print(f"{x[1]:<32} | {int(x[2]):<15,} | {Fore.YELLOW}{int(x[0]):<25,}{Fore.RESET} | {x[3]:<6}")
        except UnboundLocalError:
            print('\n Saliendo al menu principal \n')
        else:
            print()
            press_continuar()
            limpiar_consola()

def caso_4():
    estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden'),
        ('highlighted','bg:green fg:yellow'),
        ('pointer','fg:green bold'),
        ('question','fg:green bold')
    ])
    opcion = questionary.select(
        message='En que orden lo quiere mostrar: ',
        choices=[
            '. A - Z',
            '. Z - A',
            '. Volver'
        ],
        style=estilo
    ).ask()
    if opcion == '. Volver':
        limpiar_consola()
        press_continuar()
        return
    with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        usar = []
        for i in lector:
            usar.append([i['continente'],i['poblacion'],i['superficie'],i['nombre']])
        if opcion == '. A - Z':
            volt = False
            az = 'A-Z'
        elif opcion == '. Z - A':
            az = 'Z-A'
            volt = True
        try:
            print(f'\n{'Paises':<32} | {'Poblacion':<15} | {'Superficie':<12} | {Fore.YELLOW}{'Continentes  ':<8}{Fore.RESET}{Fore.RED}{az}{Fore.RESET}')
            print('-'*100)
            for x in sorted(usar,key=por_nombre, reverse = volt):
                print(f"{x[3]:<32} | {int(x[1]):<15,} | {int(x[2]):<12,} | {Fore.YELLOW}{x[0]:<20}{Fore.RESET}")
        except UnboundLocalError:
            print('\n Saliendo al menu principal \n')
        else:
            print()
            press_continuar()
            limpiar_consola()

def ordenar_paises(lista):
    while True:
        estilo = Style([
        ('instruction','hidden'),
        ('qmark','hidden'),
        ('highlighted','bg:green fg:yellow'),
        ('pointer','fg:green bold'),
        ('question','fg:green bold')
        ])
        opcion = questionary.select(
            message='Como quiere ordenar los datos',
            choices=[
                '. Nombres de los Paises',
                '. Tamaño de la Poblacion',
                '. Tamaño de la Superficie',
                '. Nombre de los Continentes',
                '. Volver al menu principal'
            ],
            style = estilo
        ).ask()
        match opcion:
            case '. Nombres de los Paises':
                caso_1()
            case '. Tamaño de la Poblacion':
                caso_2()  
            case '. Tamaño de la Superficie':
                caso_3()      
            case '. Nombre de los Continentes':
                caso_4()        
            case '. Volver al menu principal':
                print('Volviendo al menu principal')
                press_continuar()
                limpiar_consola()
                return