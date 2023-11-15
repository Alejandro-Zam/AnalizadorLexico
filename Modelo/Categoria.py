from enum import Enum

class Categoria(Enum):
    NO_RECONOCIDO = 0
    NATURALES = 1
    IDENTIFICADOR = 2
    PALABRA_RESERVADA = 3 #Preguntar lo de palabras reservadas
    OPERADOR_ARITMETICO = 4
    OPERADOR_COMPARACION = 5
    OPERADOR_LOGICO = 6
    OPERADOR_ASIGNACION = 7
    OPERADOR_INCREMENTO = 8
    OPERADOR_DECREMENTO = 9
    PARENTESIS = 10 # Preguntar parentesis
    LLAVES = 11 # Preguntar llaves
    TERMINAL = 12 # Preguntar
    SEPARADOR = 13 # Preguntar
    HEXADECIMAL = 14
    CADENA_CARACTERES = 15
    COMENTARIO_LINEA = 16
    COMENTARIO_BLOQUE = 17
    
    
    
    
   