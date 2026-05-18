import csv
PAISES = 'paises.csv'

def buscar_pais(lista):
    try:
        pais_buscar = input('Ingrese el nombre del pais a buscar: ').strip().capitalize()
    except ValueError:
        print('Dato incorrecto')
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
                print(f'El pais "{pais_buscar}" no se ha encontrado en la lista')
                print('\n ¿Quire agregarlo a la lista?')
                opc = input('[S] Si  /  [N] No : ').upper().strip()
                while True:
                    if opc == 'S':
                        agregar_pais(lista)
                        break
                    elif opc == 'N':
                        print('Volvinedo al menu principal')
                        break
                    else:
                        print('No es una opcion valida')
