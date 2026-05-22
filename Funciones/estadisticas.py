import csv
PAISES = 'paises.csv'

def mayor_menor_poblacion(lista):
    with open(PAISES,'r',newline='',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            print('-'*80)
            mayor = 0
            menor = 0
            total_poblacion = 0
            total_superficie = 0
            for i in lector:
                num_poblacion = i['poblacion']
                num_superficie = i['superficie']
                cant_pais = len(i['nombre'])
                if mayor < int(num_poblacion):
                    mayor = int(num_poblacion)
                    pais_may = i['nombre']
                elif menor <= mayor:
                    menor = int(num_poblacion)
                    pais_men = i['nombre']
                total_poblacion += int(num_poblacion)
                total_superficie += int(num_superficie)
            print(f'El pais con mayor poblacion es : {pais_may} con un total de : {mayor} habitantes')
            print(f'El pais con menor poblacion es : {pais_men} con un total de : {menor} habitantes')
            print('-'*80)
            print(f'El promedio de poblaicon es de : {total_poblacion // len(lista)} por pais')
            print(f'El promedio de la superficie de los paises seria: {total_superficie / len(lista)} km².')
            print('-'*80)
            print('Promedio de paises por continete es de: ')
            print(f'{len(lista) // len(i['continente'])} paises por continente')
def estadisticas(lista):
    print()
    mayor_menor_poblacion(lista)