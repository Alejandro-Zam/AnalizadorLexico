import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class InterfazApp:
    def __init__(self, root, analizador):
        self.root = root
        self.root.title("Interfaz de Análisis de Texto")
        
        # Establecer el tamaño de la ventana (ancho x alto)
        self.root.geometry("700x500")
        self.root.resizable(width=False, height=False)

        # Etiqueta y entrada de texto
        self.label = tk.Label(root, text="Ingrese una cadena de texto:", font=("Arial", 14))
        self.label.pack(pady=10)
        self.area_codigo = scrolledtext.ScrolledText(root, width=40, height=10)
        self.area_codigo.pack(pady=10)

        # Botón de análisis
        self.boton_analizar = tk.Button(root, text="Analizar", font=('Arial',12) ,width=12)
        self.boton_analizar.pack(pady=10)

        # Tabla con tres columnas
        self.tree = ttk.Treeview(root, columns=("Columna 1", "Columna 2", "Columna 3"), show="headings")
        self.tree.heading("Columna 1", text="Columna 1")
        self.tree.heading("Columna 2", text="Columna 2")
        self.tree.heading("Columna 3", text="Columna 3")
        self.tree.pack(pady=10)

    def analizar_texto(self):
        # Obtener el texto ingresado por el usuario
        texto_ingresado = self.texto_var.get()

        # Llamar a la función de análisis desde la instancia de Analizador
        resultados = self.analizador.analizar_texto(texto_ingresado)