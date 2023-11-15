# App.py
from Modelo.Analizador import *
from View.InterfazApp import *
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        # Crear instancia de Analizador
        self.analizador = Analizador()

        # Crear instancia de InterfazApp
        self.interfaz = InterfazApp(root, self.analizador)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
