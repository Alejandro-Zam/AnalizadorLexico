from dataclasses import dataclass
from Categoria import *

@dataclass
class Token:
    palabra: str
    categoria: Categoria
    indice_sgte: int
