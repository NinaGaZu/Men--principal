"""
Módulo que gestiona las operaciones relacionadas con proveedores
"""

from ..modelos.entidades import Proveedor
from ..almacenamiento.gestor_json import GestorJSON
import json

class ProveedorServicio:
    """Servicio para gestionar proveedores"""
    
    def __init__(self, archivo='proveedores.json'):
        """
        Inicializa el servicio de proveedores.
        
        Args:
            archivo (str): Nombre del archivo JSON
        """
        self.gestor = GestorJSON(archivo)
    
    def agregar_proveedor(self):
        """Permite al usuario ingresar un nuevo proveedor"""
        print("\n--- AGREGAR PROVEEDOR ---")
        nombre = input("Ingrese el nombre del proveedor: ")
        ubicacion = input("Ingrese la ubicación del proveedor: ")
        
        # Crear proveedor
        proveedor = Proveedor(nombre, ubicacion)
        
        # Cargar proveedores existentes
        proveedores_data = self.gestor.leer_datos()
        
        # Agregar nuevo proveedor
        proveedores_data.append(proveedor.to_dict())
        
        # Guardar en archivo
        self.gestor.escribir_datos(proveedores_data)
        
        print(f"\n✓ Proveedor '{nombre}' agregado con éxito.")
    
    def mostrar_proveedores(self):
        """Muestra todos los proveedores almacenados"""
        print("\n📦 PROVEEDORES:")
        print("-" * 40)
        
        proveedores_data = self.gestor.leer_datos()
        
        if proveedores_data:
            print(json.dumps(proveedores_data, indent=2, ensure_ascii=False))
        else:
            print("No hay proveedores registrados.")
        
        print("-" * 40)
