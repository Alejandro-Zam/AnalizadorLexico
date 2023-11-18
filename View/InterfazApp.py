import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from Modelo.Analizador import Analizador as a

class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de Análisis de Texto")
        
        
        # Establecer el tamaño de la ventana (ancho x alto)
        self.root.geometry("700x500")
        self.root.resizable(width=False, height=False)

        # Etiqueta y entrada de texto
        self.label = tk.Label(root, text="Ingrese una cadena de texto:", font=("Arial", 14))
        self.label.pack(pady=10)
        self.area_codigo = scrolledtext.ScrolledText(root, width=40, height=5)
        self.area_codigo.pack(pady=10)

        # Botón de análisis
        self.boton_analizar = tk.Button(root, text="Analizar", font=('Arial',12) ,width=12, command = self.analizar_texto)
        self.boton_analizar.pack(pady=10)

        # Tabla con tres columnas
        self.tree = ttk.Treeview(root, columns=("Palabra", "Categoría", "Posición"), show="headings")
        self.tree.heading("Palabra", text="Palabra")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Posición", text="Posición")
        self.tree.pack(pady=10)

    def analizar_texto(self):
        # Obtener el texto ingresado por el usuario
        texto = self.area_codigo.get("1.0", "end-1c")


        # Llamar a la función de análisis desde la instancia de Analizador
        a.__init__(a)
        resultados = a.analizar(a,texto);

        for resultado in resultados:
            self.tree.insert("", "end", values=(resultado.palabra, resultado.categoria, resultado.posicion))

        
