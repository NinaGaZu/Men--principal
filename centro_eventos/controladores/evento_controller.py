"""
Módulo que contiene el controlador de eventos
"""

from tkinter import messagebox
from ..modelos.evento import Evento
from ..utils.validaciones import Validaciones


class EventoController:
    """Controlador para gestionar los eventos"""
    
    def __init__(self, ventana):
        """
        Inicializa el controlador.
        
        Args:
            ventana: Ventana principal de Tkinter
        """
        self.ventana = ventana
        self.formulario = None
    
    def set_formulario(self, formulario):
        """
        Establece la referencia al formulario.
        
        Args:
            formulario: Instancia del formulario
        """
        self.formulario = formulario
    
    def registrar_evento(self):
        """Función para registrar el evento"""
        # Obtener datos del formulario
        datos = self.formulario.obtener_datos()
        
        # Validar datos
        if not self._validar_datos(datos):
            return
        
        # Crear objeto Evento
        evento = Evento(
            nombre=datos['nombre'],
            organizador=datos['organizador'],
            fecha=datos['fecha'],
            categoria=datos['categoria'],
            tipos_evento=datos['tipos_evento'],
            estado=datos['estado'],
            asistentes=datos['asistentes'],
            ubicacion=datos['ubicacion'],
            descripcion=datos['descripcion']
        )
        
        # Mostrar información en terminal
        evento.mostrar_info()
        
        # Mostrar mensaje de confirmación
        mensaje = f"Evento '{evento.nombre}' registrado exitosamente"
        messagebox.showinfo("Registro Exitoso", mensaje)
    
    def limpiar_formulario(self):
        """Función para limpiar todos los campos del formulario"""
        self.formulario.limpiar()
        print("Formulario limpiado correctamente")
    
    def _validar_datos(self, datos):
        """
        Valida los datos del formulario.
        
        Args:
            datos (dict): Datos del formulario
        
        Returns:
            bool: True si todos los datos son válidos
        """
        # Validar campos vacíos
        if not Validaciones.validar_campo_vacio(datos['nombre'], "Nombre del Evento"):
            return False
        if not Validaciones.validar_campo_vacio(datos['organizador'], "Organizador"):
            return False
        if not Validaciones.validar_campo_vacio(datos['fecha'], "Fecha"):
            return False
        if not Validaciones.validar_campo_vacio(datos['asistentes'], "Asistentes"):
            return False
        
        # Validar asistentes
        if not Validaciones.validar_asistentes(datos['asistentes']):
            return False
        
        # Validar categoría
        if not Validaciones.validar_categoria(datos['categoria']):
            return False
        
        # Validar estado
        if not Validaciones.validar_estado(datos['estado']):
            return False
        
        # Validar tipos de evento
        if not Validaciones.validar_tipos_evento(datos['tipos_evento']):
            return False
        
        return True