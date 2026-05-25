class ListaVacia(Exception):
    pass
def lista_vacia(lista):
    if lista is None:
        raise ListaVacia ("No hay países cargados en la lista.")
    else:
        return lista

class DatoRepetido(Exception):
    pass
def esta_repetido(lista,dato):
    existe = any(isinstance(p, dict) and p.get('nombre') == dato for p in lista)
    if existe:
        raise DatoRepetido(f'El pais {dato} ya existe')
