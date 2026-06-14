# Funciones para que la consola quede mas limpia
import questionary
import os
import msvcrt
from colorama import Fore
from questionary import Style
def limpiar_consola():
    os.system('cls' if os.name=='nt' else 'clear')
def press_continuar():
    print()
    print('Presione cualquier tecla para continuar')
    msvcrt.getch()