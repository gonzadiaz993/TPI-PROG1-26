class NombreYaExiste(Exception):
    pass
def nombre_existe(lista,nombre):
    pass

class ListaVacia(Exception):
    pass
def lista_vacia(lista):
    if lista is None:
        raise ListaVacia ("No hay países cargados en la lista.")
    else:
        return lista


