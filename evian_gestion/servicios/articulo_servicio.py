"""
Módulo que gestiona las operaciones relacionadas con artículos
"""

from ..modelos.entidades import Articulo
from ..almacenamiento.gestor_json import GestorJSON


class ArticuloServicio:
    """Servicio para gestionar artículos"""
    
    def __init__(self, archivo='articulos.json'):
        """
        Inicializa el servicio de artículos.
        
        Args:
            archivo (str): Nombre del archivo JSON
        """
        self.gestor = GestorJSON(archivo)
    
    def agregar_articulo(self):
        """Permite al usuario ingresar un nuevo artículo"""
        print("\n--- AGREGAR ARTÍCULO ---")
        nombre = input("Ingrese el nombre del artículo: ")
        categoria = input("Ingrese la categoría: ")
        
        # Validación del precio
        while True:
            try:
                precio = float(input("Ingrese el precio: "))
                if precio < 0:
                    print("El precio no puede ser negativo. Intente nuevamente.")
                else:
                    break
            except ValueError:
                print("Ingrese un valor numérico válido para el precio.")
        
        proveedor_asociado = input("Ingrese el nombre del proveedor asociado: ")
        
        # Crear artículo
        articulo = Articulo(nombre, categoria, precio, proveedor_asociado)
        
        # Cargar artículos existentes
        articulos_data = self.gestor.leer_datos()
        
        # Agregar nuevo artículo
        articulos_data.append(articulo.to_dict())
        
        # Guardar en archivo
        self.gestor.escribir_datos(articulos_data)
        
        print(f"\n✓ Artículo '{nombre}' agregado con éxito.")
    
    def mostrar_articulos(self):
        """Muestra todos los artículos almacenados"""
        print("\n🛍️ ARTÍCULOS:")
        print("-" * 40)
        
        articulos_data = self.gestor.leer_datos()
        
        if articulos_data:
            print(json.dumps(articulos_data, indent=2, ensure_ascii=False))
        else:
            print("No hay artículos registrados.")
        
        print("-" * 40)


# Importar json para el método mostrar_articulos
import json