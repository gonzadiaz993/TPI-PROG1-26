import csv
from Funciones.excepciones import *
from Funciones.guardar_archivo import *
from Funciones.en_consola import *
def agregar_pais(paises):
    try:
        lista_vacia(paises)
    except ListaVacia as e:
        print(f'Error. {e}')
    while True:
        print(f'\n--- Agregar Nuevo País (Escriba {Fore.RED}salir{Fore.RESET} en nombre para terminar) ---')
        try:
            nombre = ""
            while not nombre:
                try:
                    entrada = input("Ingrese el nombre del país: ").strip()
                    if entrada.lower() == 'salir':
                        return paises
                    nombre_pais = entrada.capitalize()
                    esta_repetido(paises,nombre_pais)
                    nombre = nombre_pais
                except DatoRepetido as e:
                    print(f'Error. {e}')
            poblacion = -1
            while poblacion < 0:
                poblacion = int(input(f"Ingrese la población de {nombre}: "))
                if poblacion < 0:
                    print("La población debe ser un número positivo.")

            superficie = -1
            while superficie < 0:
                superficie = int(input(f"Ingrese la superficie de {nombre} (km²): "))
                if superficie < 0:
                    print("La superficie debe ser un número positivo.")

            continente = ""
            while not continente:
                continente = input(f"Ingrese el continente de {nombre}: ").strip().capitalize()
                if not continente:
                    print("El continente no puede estar vacío.")
            nuevo_pais = {
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente 
            }
            paises.append(nuevo_pais)
            guardar_archivo(paises)
            print(f"\n¡{nombre} se ha registrado correctamente!")
        except ValueError:
            print("\nError: Ingrese solo números enteros para población y superficie.")