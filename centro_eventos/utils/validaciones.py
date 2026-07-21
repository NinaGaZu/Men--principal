"""
Módulo que contiene funciones de validación para el formulario
"""


class Validaciones:
    """Clase con métodos estáticos para validar datos del formulario"""
    
    @staticmethod
    def validar_campo_vacio(valor, nombre_campo):
        """
        Valida que un campo no esté vacío.
        
        Args:
            valor (str): Valor a validar
            nombre_campo (str): Nombre del campo para el mensaje
        
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not valor or valor.strip() == "":
            print(f" El campo '{nombre_campo}' está vacío.")
            return False
        return True
    
    @staticmethod
    def validar_asistentes(asistentes):
        """
        Valida que el número de asistentes sea un número entero positivo.
        
        Args:
            asistentes (str): Número de asistentes a validar
        
        Returns:
            bool: True si es válido, False en caso contrario
        """
        try:
            num = int(asistentes)
            if num < 0:
                print("⚠ El número de asistentes no puede ser negativo.")
                return False
            return True
        except ValueError:
            print("⚠ El número de asistentes debe ser un valor numérico válido.")
            return False
    
    @staticmethod
    def validar_categoria(categoria):
        """
        Valida que se haya seleccionado una categoría.
        
        Args:
            categoria (str): Categoría seleccionada
        
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not categoria:
            print("⚠ Debe seleccionar una categoría para el evento.")
            return False
        return True
    
    @staticmethod
    def validar_estado(estado):
        """
        Valida que se haya seleccionado un estado.
        
        Args:
            estado (str): Estado seleccionado
        
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not estado:
            print("⚠ Debe seleccionar un estado para el evento.")
            return False
        return True
    
    @staticmethod
    def validar_tipos_evento(tipos_evento):
        """
        Valida que se haya seleccionado al menos un tipo de evento.
        
        Args:
            tipos_evento (list): Lista de tipos de evento seleccionados
        
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not tipos_evento:
            print("⚠ Debe seleccionar al menos un tipo de evento.")
            return False
        return True