import csv
PAISES = 'paises.csv'
def menu_5():
    print('¿Como quiere ordenar la lista?')
    print('''
1. Nombre paises
2. Tamaño de la poblacion
3. Tamaño de la superficie
4. Nombre continente\n''')

def por_nombre(fila):
    return fila[0]

def caso_1(lista):
    print('\nComo lo quiere ordenar?')
    print('\n1.(A-Z) || 2.(Z-A) || Otro - Salir\n')
    try:
        opcion = int(input('>> '))
    except ValueError:
        print('Saliendo')
        return
    else:
        with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            usar = []
            for i in lector:
                usar.append([i['nombre'],i['poblacion'],i['superficie'],i['continente']])
            if opcion == 1:
                volt = False
                az = 'A-Z'
            elif opcion == 2:
                az = 'Z-A'
                volt = True
            try:
                print(f'\n{'Paises':<29}{az} | {'Poblacion':<15} | {'Superficie':<12} | {'Continentes':<6}')
                print('-'*80)
                for x in sorted(usar, reverse = volt):
                    print(f"{x[0]:<32} | {x[1]:<15} | {x[2]:<12} | {x[3]:<6}")
            except UnboundLocalError:
                print('\n Saliendo al menu principal \n')

def caso_2(lista):
    print('\nComo lo quiere ordenar?')
    print('\n1.(Mayor a Menor) || 2.(Menor a Mayor) || Otro - Salir\n')
    try:
        opcion = int(input('>> '))
    except ValueError:
        print('Saliendo')
        return
    else:
        with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            usar = []
            for i in lector:
                usar.append([int(i['poblacion']),i['nombre'],i['superficie'],i['continente']])
            if opcion == 1:
                volt = True
                az = 'Mayor a Menor'
            elif opcion == 2:
                az = 'Menor a Mayor'
                volt = False
            try:
                print(f'\n{'Paises':<15} | {'Poblacion':<16}{az} | {'Superficie':<12} | {'Continentes':<6}')
                print('-'*80)
                for x in sorted(usar, reverse=volt):
                    print(f"{x[1]:<15} | {x[0]:<29} | {x[2]:<12} | {x[3]:<6}")
            except UnboundLocalError:
                print('\n Saliendo al menu principal \n')

def caso_3(lista):
    print('\nComo lo quiere ordenar?')
    print('\n1.(Mayor a Menor) || 2.(Menor a Mayor) || Otro - Salir \n')
    try:
        opcion = int(input('>> '))
    except ValueError:
        print('Saliendo')
        return
    else:
        with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            usar = []
            for i in lector:
                usar.append([int(i['superficie']),i['nombre'],i['poblacion'],i['continente']])
            if opcion == 1:
                volt = True
                az = 'Mayor a Menor'
            elif opcion == 2:
                az = 'Menor a Mayor'
                volt = False
            try:
                print(f'\n{'Paises':<15} | {'Poblacion':<15} | {'Superficie':<12}{az} | {'Continentes':<6}')
                print('-'*80)
                for x in sorted(usar, reverse=volt):
                    print(f"{x[1]:<15} | {x[2]:<15} | {x[0]:<25} | {x[3]:<6}")
            except UnboundLocalError:
                print('\n Saliendo al menu principal \n')

def caso_4(lista):
    print('\nComo lo quiere ordenar?')
    print('\n1.(A-Z) || 2.(Z-A) || Otro - Salir\n')
    try:
        opcion = int(input('>> '))
    except ValueError:
        print('Saliendo')
        return
    else:
        with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            usar = []
            for i in lector:
                usar.append([i['continente'],i['poblacion'],i['superficie'],i['nombre']])
            if opcion == 1:
                volt = False
                az = 'A-Z'
            elif opcion == 2:
                az = 'Z-A'
                volt = True
            try:
                print(f'\n{'Paises':<15} | {'Poblacion':<15} | {'Superficie':<12} | {'Continentes  ':<8}{az}')
                print('-'*80)
                for x in sorted(usar,key=por_nombre, reverse = volt):
                    print(f"{x[3]:<15} | {x[1]:<15} | {x[2]:<12} | {x[0]:<6}")
            except UnboundLocalError:
                print('\n Saliendo al menu principal \n')


def ordenar_paises(lista):
        menu_5()
        try: 
            opcion = int(input('>>'))
        except ValueError:
            print('No se ha seleccionado una opcion valida')
            return
        match opcion:
            case 1:
                caso_1(lista)
            case 2:
                caso_2(lista)  
            case 3:
                caso_3(lista)      
            case 4:
                caso_4(lista)        
            case _:
                print('No se ha seleccionado una opcion valida')