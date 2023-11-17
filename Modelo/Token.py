from dataclasses import dataclass
from Categoria import *

@dataclass
class Token:
    palabra: str
    categoria: Categoria
    linea: int
    posicion: int
