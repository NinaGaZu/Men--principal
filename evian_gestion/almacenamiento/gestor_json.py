"""
Módulo que gestiona la lectura y escritura de archivos JSON
"""

import json
import os


class GestorJSON:
    """Clase para manejar operaciones de archivos JSON"""
    
    def __init__(self, nombre_archivo):
        """
        Inicializa el gestor JSON.
        
        Args:
            nombre_archivo (str): Nombre del archivo JSON
        """
        self.nombre_archivo = nombre_archivo
    
    def leer_datos(self):
        """
        Lee datos desde el archivo JSON.
        
        Returns:
            list: Lista de datos o lista vacía si el archivo no existe
        """
        datos = []
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no existe. Se creará automáticamente.")
        except json.JSONDecodeError:
            print(f"El archivo {self.nombre_archivo} está vacío o corrupto. Se inicializará.")
        return datos
    
    def escribir_datos(self, datos):
        """
        Escribe datos en el archivo JSON.
        
        Args:
            datos (list): Lista de datos a guardar
        """
        with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
    
    def existe_archivo(self):
        """
        Verifica si el archivo existe.
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        return os.path.exists(self.nombre_archivo)
    