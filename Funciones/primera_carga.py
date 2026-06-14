import csv
import time
from tqdm import tqdm
datos = 'paises.csv'
def cargar_archivo():
    paises = []
    try:
        # Abrimos el archivo y contamos las líneas para que tqdm sepa el total
        with open(datos, 'r', encoding='utf-8') as archivo:
            # Restamos 1 si el CSV tiene cabecera (header)
            total_filas = sum(1 for fila in archivo) - 1 
            
        with open(datos, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo) # O csv.reader(archivo)
            
            print("Cargando base de datos de países...")
            # Envolvemos el lector en tqdm
            for fila in tqdm(lector, total=total_filas, desc="Cargando Paises : ", bar_format="{l_bar}{bar:20}{r_bar}"):
                paises.append(fila)
                time.sleep(0.05) 
                
        return paises
    except FileNotFoundError:
        print("No se encontró el archivo CSV. Iniciando lista vacía.")
        return []