"""
Módulo que define las clases de las entidades: Articulo y Proveedor
"""

class Articulo:
    """Clase que representa un artículo"""
    
    def __init__(self, nombre, categoria, precio, proveedor):
        """
        Inicializa un nuevo artículo.
        
        Args:
            nombre (str): Nombre del artículo
            categoria (str): Categoría del artículo
            precio (float): Precio del artículo
            proveedor (str): Nombre del proveedor asociado
        """
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.proveedor = proveedor
    
    def to_dict(self):
        """Convierte el artículo a diccionario"""
        return {
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio': self.precio,
            'proveedor': self.proveedor
        }
    
    @classmethod
    def from_dict(cls, datos):
        """Crea un artículo desde un diccionario"""
        return cls(
            nombre=datos['nombre'],
            categoria=datos['categoria'],
            precio=datos['precio'],
            proveedor=datos['proveedor']
        )
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio}"

class Proveedor:
    """Clase que representa un proveedor"""
    
    def __init__(self, nombre, ubicacion):
        """
        Inicializa un nuevo proveedor.
        
        Args:
            nombre (str): Nombre del proveedor
            ubicacion (str): Ubicación del proveedor
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
    
    def to_dict(self):
        """Convierte el proveedor a diccionario"""
        return {
            'nombre': self.nombre,
            'ubicacion': self.ubicacion
        }
    
    @classmethod
    def from_dict(cls, datos):
        """Crea un proveedor desde un diccionario"""
        return cls(
            nombre=datos['nombre'],
            ubicacion=datos['ubicacion']
        )
    
    def __str__(self):
        return f"{self.nombre} - {self.ubicacion}"