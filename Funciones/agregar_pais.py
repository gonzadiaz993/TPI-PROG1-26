import csv
from Funciones.excepciones import *
from Funciones.guardar_archivo import *
from Funciones.en_consola import *
def agregar_pais(paises):
    print("\n--- Agregar Nuevo País (Escriba 'salir' en nombre para terminar) ---") 
    while True:
        entrada = input("Ingrese el nombre del país: ").strip()  
        if entrada.lower() == 'salir':
            return paises
        if entrada == "":
            print("El nombre del país no puede estar vacío.")
            continue
        if not entrada.replace(" ", "").isalpha():
            print("Error: El nombre del país solo puede contener letras y espacios.")
            continue
        nombre_pais = entrada.title()
        
        # Verificamos si el nombre ya existe en la lista de diccionarios devuelve un booleano
        #any devuelve true si almenos uno de los elemtnos es true.Dentro de el se compara si un dicionario para no romper el programa. 
        existe = any(isinstance(p, dict) and p.get('nombre') == nombre_pais for p in paises)
        
        if existe:
            print(f"El país '{nombre_pais}' ya se encuentra en la lista.")
            continue

        nombre = nombre_pais
        break
    
    while True:
        try:
            poblacion = int(input(f"Ingrese la población de {nombre}: "))
            if poblacion <= 0:
                print("La población debe ser un número positivo y mayor a 0.")
            else:
                print("Poblacion añadida con exito.")
                break
            
        except ValueError:
            print("La poblacion debe ser un numero.")
    while True:
        try:
            superficie = int(input(f"Ingrese la superficie de {nombre} (km²): "))
            if superficie <= 0:
                print("La superficie debe ser un número positivo y mayor a 0.")
            else:
                print("Superficie añadida con exito.")
                break
        except ValueError:
            print("No puede contener letras.")
    while True:
        continente = input(f"Ingrese el continente de {nombre}: ").strip().capitalize()
        
        if continente == "":
            print("El continente no puede estar vacío.")
        
        elif not continente.isalpha(): 
            print("Error: El continente no puede contener números ni caracteres especiales.")
        else:
            print("Continente añadido con éxito.")
            break
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente 
    }
    paises.append(nuevo_pais)
    guardar_archivo(paises)
    limpiar_consola()
    press_continuar()
    return paises