# Analizador.py
from Token import *

class Analizador:

    def __init__(self, codigoAnalizar):
        self.codigoAnalizar = codigoAnalizar
        self.listaTokens = []
    
    def analizar(self):
        # Posición de la línea desde donde empieza a analizar
        indice_linea = 0

        # Se separa el codigoAnalizar por líneas de código
        lineasCodigoAnalizar = separarLineas(self.codigoAnalizar)

        while indice_linea < len(lineasCodigoAnalizar):
            linea = lineasCodigoAnalizar[indice_linea]

            # Iterar sobre los caracteres de cada palabra
            indice_caracter = 0
            while indice_caracter < len(linea):

                #Detectar cadena
                if indice_caracter < len(linea) and linea[indice_caracter] == '"':
                    indice_caracter = self.Detectar_cadena(linea, indice_linea, indice_caracter)

                #Detectar Identificadores
                if indice_caracter < len(linea) and linea[indice_caracter] == '&':
                    indice_caracter = self.Detectar_idenficiador(linea, indice_linea, indice_caracter)
                
                #Detectar Palabras reservadas
                if indice_caracter < len(linea) and linea[indice_caracter] == '%':
                    indice_caracter = self.Detectar_Reservadas(linea, indice_linea, indice_caracter)

                #Detectar Operadores Incremento
                if indice_caracter < len(linea) and linea[indice_caracter] == '+':
                    indice_caracter = self.Detectar_Incremento(linea, indice_linea, indice_caracter)
                
                #Detectar Operadores Decremento
                if indice_caracter < len(linea) and linea[indice_caracter] == '-':
                    indice_caracter = self.Detectar_Decremento(linea, indice_linea, indice_caracter)
                
                #Detectar Operadores Aritmeticos
                if indice_caracter < len(linea) and linea[indice_caracter] in {'-', '+', '*', '/', '%', '^'}:   
                    indice_caracter = self.Detectar_Aritmeticos(linea, indice_linea, indice_caracter)

                #Dectectar Operadores de comparación
                if indice_caracter < len(linea) and linea[indice_caracter] in {'=', '!', '>', '<'}:   
                    indice_caracter = self.Detectar_Comparacion(linea, indice_linea, indice_caracter)

                # Detectar Operadores logicos
                if indice_caracter < len(linea) and linea[indice_caracter] == '_':
                    indice_caracter = self.Detectar_logicos(linea, indice_linea, indice_caracter)

                # Detectar Operadores asignacion
                if indice_caracter < len(linea) and linea[indice_caracter] == '=':
                    indice_caracter = self.Detectar_asignacion(linea, indice_linea, indice_caracter)
                
                # Detectar llaves o parentesis
                if indice_caracter < len(linea) and linea[indice_caracter] in {'(', ')', '{', '}'}:  
                    indice_caracter = self.Detectar_llaves_parentesis(linea, indice_linea, indice_caracter)

                # Detectar Hexadecimal
                if indice_caracter < len(linea) and linea[indice_caracter] == '#':
                    indice_caracter = self.Detectar_Hexa(linea, indice_linea, indice_caracter+1)

                #Detectar Numeros
                if indice_caracter < len(linea) and linea[indice_caracter].isdigit():
                    indice_caracter = self.Detectar_Reales(linea, indice_linea, indice_caracter)
                    indice_caracter = self.Detectar_Naturales(linea, indice_linea, indice_caracter)

                # Detectar comentario de linea
                if indice_caracter < len(linea) and linea[indice_caracter] == "!": 
                    indice_caracter = self.Detectar_comentario_linea(linea, indice_linea, indice_caracter)
                
                # Detectar comentario de bloque
                if indice_caracter < len(linea) and linea[indice_caracter] == "¡": 
                    indice_linea = self.detectar_comentario_bloque(linea, indice_linea, indice_caracter,lineasCodigoAnalizar)
                
                if indice_caracter < len(linea):
                    if(linea[indice_caracter]!=" "):
                        self.listaTokens.append(Token(linea[indice_caracter], Categoria.NO_RECONOCIDO, indice_linea + 1, indice_caracter ))
                
                indice_caracter += 1

            indice_linea += 1

    

    def Detectar_Hexa(self, linea, indice_linea, indice_caracter):
        indice_actual = indice_caracter
        hexa = "#"

        while indice_caracter < len(linea):
            if indice_caracter < len(linea) and linea[indice_caracter] in {'A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9'}:
                hexa+= linea[indice_caracter]
                indice_caracter+=1
            else:
                break
        if (len(hexa) > 2):
            # Añadir el token a la listaTokens
            self.listaTokens.append(Token(hexa, Categoria.HEXADECIMAL, indice_linea + 1, indice_caracter - len(hexa)))
            return indice_caracter
        else:
            return indice_actual

    # Comentario de bloque
    def detectar_comentario_bloque(self, linea, indice_linea, indice_caracter, lineasCodigoAnalizar):
        linea_actual = linea
        comentarioBloque = ""
        if linea[0] == '¡' and linea[1] == '¡':
            comentarioBloque += linea
            while indice_linea < len(lineasCodigoAnalizar):
                linea = lineasCodigoAnalizar[indice_linea+1]
                comentarioBloque += linea
                if linea[-2] == '!' and linea[-1] == '!':
                    comentarioBloque += linea
                    self.listaTokens.append(Token(comentarioBloque, Categoria.COMENTARIO_BLOQUE, indice_linea + 1, indice_caracter))
                    return indice_linea
                indice_linea+=1   
            return linea_actual
        return linea_actual
    

    def Detectar_comentario_linea(self, linea, indice_linea, indice_caracter):
        indice_anterior = indice_caracter

        if linea[0] == '!':
            indice_caracter = len(linea)
            self.listaTokens.append(Token(linea, Categoria.COMENTARIO_LINEA, indice_linea + 1, indice_caracter))
            
            return indice_caracter
        else:
            return indice_anterior
        

    # Detectar lleaves o parentesis 
    def Detectar_llaves_parentesis(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        if indice_caracter < len(linea) - 1:
            llaves_parentesis = linea[indice_caracter]
            if llaves_parentesis in {'(', ')'}:
                indice_caracter += 1
                self.listaTokens.append(Token(llaves_parentesis, Categoria.PARENTESIS, indice_linea + 1, indice_caracter - 1))
                return indice_caracter
            elif llaves_parentesis in {'{', '}'}:
                indice_caracter+1
                self.listaTokens.append(Token(llaves_parentesis, Categoria.LLAVES, indice_linea + 1, indice_caracter - 1))
                return indice_caracter
            else:
                return indice_inicial
        return indice_inicial
    
    # Detectar operadores de asignación
    def Detectar_asignacion(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        if indice_caracter < len(linea) - 1:
            operadoAsignacion = linea[indice_caracter: indice_caracter + 2]
            if operadoAsignacion in {'=+', '=-', '=/', '=%', '=*'}:
                indice_caracter += 2
                self.listaTokens.append(Token(operadoAsignacion, Categoria.OPERADOR_ASIGNACION, indice_linea + 1, indice_caracter - 2))
                return indice_caracter
            elif operadoAsignacion == '=':
                indice_caracter += 1
                self.listaTokens.append(Token(operadoAsignacion, Categoria.OPERADOR_ASIGNACION, indice_linea + 1, indice_caracter - 1))
                return indice_caracter
            else: 
                return indice_inicial
        else:
            return indice_inicial

    # Detectar operadores de comparación
    def Detectar_logicos(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

    
        if indice_caracter < len(linea) - 1:
            operadorLogico= linea[indice_caracter:indice_caracter+3]
            if operadorLogico in {"_Y_", "_N_", "_O_"}:
                indice_caracter +=3
                self.listaTokens.append(Token(operadorLogico, Categoria.OPERADOR_LOGICO, indice_linea + 1, indice_caracter - 3))
                return indice_caracter
            else:
                return indice_inicial
        else:
            return indice_inicial

    # Detectar operadores de comparacion
    def Detectar_Comparacion(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        if indice_caracter < len(linea) - 1:
            operadoComparacion = linea[indice_caracter: indice_caracter + 2]
            if operadoComparacion in {'==', '!=', '>=', '<='}:
                indice_caracter += 2
                self.listaTokens.append(Token(operadoComparacion, Categoria.OPERADOR_COMPARACION, indice_linea + 1, indice_caracter - 2))
                return indice_caracter
            else:
                operadoComparacion = linea[indice_caracter]
                if operadoComparacion in {'>', '<'}:
                    indice_caracter += 2
                    self.listaTokens.append(Token(operadoComparacion, Categoria.OPERADOR_COMPARACION, indice_linea + 1, indice_caracter - 1))
                    return indice_caracter
                else:
                    return indice_inicial
        else:
            return indice_inicial




    # Detectar operador aritmetico
    def Detectar_Aritmeticos(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        if indice_caracter < len(linea) - 1:
            operado_Aritmetico = linea[indice_caracter]

            if operado_Aritmetico in {'-', '+', '*', '/', '%', '^'}:
                indice_caracter += 1
                self.listaTokens.append(Token(operado_Aritmetico, Categoria.OPERADOR_ARITMETICO, indice_linea + 1, indice_caracter - 1))
                return indice_caracter
            else:
                return indice_inicial
        else:
            return indice_inicial


    # Detectar decremento
    def Detectar_Decremento(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        if indice_caracter < len(linea) - 1:
            operadoDecremento = linea[indice_caracter: indice_caracter + 2]

            if operadoDecremento == '--':
                indice_caracter += 2
                self.listaTokens.append(Token("--", Categoria.OPERADOR_DECREMENTO, indice_linea + 1, indice_caracter - 2))
                return indice_caracter
            else:
                return indice_inicial
        else:
            return indice_inicial

    # Detectar incremento
    def Detectar_Incremento(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        if indice_caracter < len(linea) - 1:
            operadoIncremento = linea[indice_caracter: indice_caracter + 2]

            if operadoIncremento == '++':
                indice_caracter += 2
                self.listaTokens.append(Token("++", Categoria.OPERADOR_INCREMENTO, indice_linea + 1, indice_caracter - 2))
                return indice_caracter
            else:
                return indice_inicial
        else:
            return indice_inicial
        
    # Detectar palabra reservada
    def Detectar_Reservadas(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter
        longitud_maxima_palabra_reservada = 6

        while indice_caracter < len(linea) and linea[indice_caracter] == '%':
            indice_caracter += 1
            palabra_reservada = ""
            contador = 0

            while indice_caracter < len(linea) and linea[indice_caracter].isalpha() and contador < longitud_maxima_palabra_reservada:
                palabra_reservada += linea[indice_caracter]
                indice_caracter += 1    
                contador += 1

            if palabra_reservada in ["CREATE", "DORMIR", "DELETE", "TOPPER", "NONULL", "UPDATE"]:
                palabra_completa = "%" + palabra_reservada
                self.listaTokens.append(Token(palabra_completa, Categoria.PALABRA_RESERVADA, indice_linea + 1, indice_caracter - len(palabra_completa)))
                return indice_caracter
            else:
                indice_caracter = linea.find('%', indice_caracter) + 1

        return indice_inicial

    # Detectar cadenas
    def Detectar_cadena(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter
        final_encontrado = False
        cadena = ""

        if indice_caracter < len(linea) and linea[indice_caracter] == '"':
            cadena += linea[indice_caracter]
            indice_caracter += 1
            while indice_caracter < len(linea) and not final_encontrado:
                cadena += linea[indice_caracter]
                if linea[indice_caracter] == '"':
                    final_encontrado = True
                indice_caracter += 1

            if cadena[-1] == '"':
                self.listaTokens.append(Token(cadena, Categoria.CADENA_CARACTERES, indice_linea + 1, indice_caracter - len(cadena)))
                return indice_caracter
            else:
                self.listaTokens.append(Token(cadena, Categoria.ERROR_CADENA_SIN_CERRAR, indice_linea + 1, indice_caracter - len(cadena)))
                return indice_inicial
        else:
            return indice_inicial
                        
                

    # Detectar identificadores
    def Detectar_idenficiador(self, linea, indice_linea, indice_caracter):
        indice_inicial = indice_caracter

        identificador= linea[indice_caracter:indice_caracter+9]

        if len(identificador) <= 10:
        # Verifica que el primer carácter sea "&" y el segundo sea una letra
            if identificador[0] == '&' and identificador[1].isalpha():
                # Verifica que los caracteres restantes sean letras o números
                if all(caracter.isalnum() for caracter in identificador[2:]):
                    self.listaTokens.append(Token(identificador, Categoria.IDENTIFICADOR, indice_linea + 1, indice_caracter - len(identificador)))
                    return indice_caracter
        return indice_inicial
                



    # Detectar numeros reales
    def Detectar_Reales(self, linea, indice_linea, indice_caracter):
        numero = ""
        punto_encontrado = False
        indiceInicial = indice_caracter

        while indice_caracter < len(linea):
            if linea[indice_caracter].isdigit():
                numero += linea[indice_caracter]
            elif linea[indice_caracter] == '.' and not punto_encontrado:
                numero += linea[indice_caracter]
                punto_encontrado = True
            else:
                break

            indice_caracter += 1

        if (len(numero) > 2) and punto_encontrado:
            # Añadir el token a la listaTokens
            self.listaTokens.append(Token(numero, Categoria.REALES, indice_linea + 1, indice_caracter - len(numero)))
            return indice_caracter
        else:
            return indiceInicial
        

    #Metodo para detectar números naturales 
    def Detectar_Naturales(self, linea, indice_linea, indice_caracter):
            numero = ""
            indiceInicial = indice_caracter

            while indice_caracter < len(linea) and linea[indice_caracter].isdigit():
                numero += linea[indice_caracter]
                indice_caracter += 1

            if numero:
                # Añadir el token a la listaTokens
                self.listaTokens.append(Token(numero, Categoria.NATURALES, indice_linea + 1, indice_caracter - len(numero)))
                return indice_caracter
            else:
                return indiceInicial

def separarLineas(texto):
    # Divide el texto en líneas
    lineas = texto.splitlines()

    # Retorna el arreglo con las líneas
    return lineas


codigo_a_analizar = """cl_O_ass MiClase:
"AWA"$AASshdhsd4312.10dnfdnfhey
    def __init__(self, valor):
    #AD12
        self.valor = valor
¡¡    -   -  + / 
    def imprimir_valor(self):
        print(self.valor)
    "&asddddddd-dd
    "CADENA">=<=
    %DELETE_O_ !!
!-Esto es un comentario

&gtgg1=+
objeto = MiClase(42)
3273721%UPDATEad_Y_hsdyey!%DORMIRRnsdhueerd
ajssjd+++ue0.1jdjdue%CREATE++=-
12837236261323.0
objeto.impr=/imir_valor()
"""
analizador = Analizador(codigo_a_analizar)
analizador.analizar()

# Imprime la lista de tokens generada
for token in analizador.listaTokens:
    print(token)


