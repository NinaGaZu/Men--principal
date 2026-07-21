"""
Módulo que contiene la ventana principal de la aplicación
"""

import tkinter as tk
from .formulario_evento import FormularioEvento
from ..controladores.evento_controller import EventoController


class VentanaPrincipal:
    """Clase que representa la ventana principal de la aplicación"""
    
    def __init__(self):
        """Inicializa la ventana principal"""
        # Crear ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("CentroEventosArenasX - Gestión de Eventos")
        self.ventana.geometry("700x800")
        
        # Crear controlador
        self.controller = EventoController(self.ventana)
        
        # Crear formulario
        self.formulario = FormularioEvento(self.ventana, self.controller)
        
        # Conectar formulario con controlador
        self.controller.set_formulario(self.formulario)
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        print("Sistema de Gestión de Eventos - CentroEventosArenasX")
        print("="*60)
        print("La aplicación está lista. Complete el formulario y registre el evento.")
        print("="*60 + "\n")
        
        self.ventana.mainloop()