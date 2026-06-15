import csv
from Funciones.excepciones import *
from Funciones.guardar_archivo import *
from Funciones.en_consola import *
def agregar_pais(paises):
    print("\n--- Agregar Nuevo País (Escriba 'salir' en nombre para terminar) ---") 
    while True:
        # 1. Entrada y validación del Nombre
        while True:
            entrada = input("Ingrese el nombre del país o salir para finalizar.: ").strip()
            if entrada.lower() == 'salir':
                return paises # Salimos de la funcion
            # Bloque try y except para la validacion de las entradas 
            try:     
                nombre = entrada.title()
                validar_pais(nombre,paises) 
                print("Pais añadido.")
                break
            except error_entradavacia as e:
                print(e)
            except error_sololetras as e:
                print (e)
            except error_paisexiste as e:
                print(e)
        
        while True:
            try:
                poblacion = int(input(f"Ingrese la población de {nombre}: "))
                validar_entero(poblacion)
                print("Poblacion añadida.")
                break
            except ValueError:
                print("Solo se permiten numeros enteros.")
            except error_numero_negativo as e:
                print(e)
                
        while True:
            try:
                superficie = int(input(f"Ingrese la superficie de {nombre} (km²): "))
                validar_entero(superficie)
                print("Superficie añadida.")
                break
            except ValueError:
                print("Solo se permiten numeros enteros.")
            except error_numero_negativo as e:
                print(e)
        while True:
            try:
                continente = input(f"Ingrese el continente de {nombre}: ").strip().capitalize()
                validar_continente(continente)
                print("Continente añadido.")
                break
            except error_entradavacia as e:
                print(e)
            except error_sololetras as e:
                print (e)
        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente 
        }
        #añade pais a la lista guarda el nuevo pais y vuelve a otro nombre hasta ingresar "salir".
        paises.append(nuevo_pais)
        guardar_archivo(paises)
        press_continuar()
        limpiar_consola()
# fuciones de validacion            
def validar_pais(pais,lista):
    if pais == "":
        raise error_entradavacia("El campo no puede quedar vacio.")
    if not pais.replace(" ", "").isalpha():
            raise error_sololetras("Error: El nombre del país solo puede contener letras y espacios.")
    for paises in lista:
        if paises["nombre"] == pais:
            raise error_paisexiste("El pais ya se encuetra cargado en la lista.")
def validar_entero(poblacion):
    if poblacion <= 0 :
        raise error_numero_negativo("No se permiten numeros negativos.")
def validar_continente(continente):
    if continente == "":
        raise error_entradavacia("El campo no puede quedar vacio.")
    if not continente.replace(" ", "").isalpha():
            raise error_sololetras("Error: El nombre del continente solo puede contener letras y espacios.")
# creacion de errores personalizados    
class error_entradavacia(Exception):
    pass
class error_numero_negativo(Exception):
    pass
class error_sololetras(Exception):
    pass
class error_paisexiste(Exception):
    pass