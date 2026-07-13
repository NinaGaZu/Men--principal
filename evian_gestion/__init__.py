"""
Paquete evian_gestion - Sistema de Gestión de Proveedores y Artículos
Versión 1.0
"""

__version__ = '1.0.0'
__author__ = 'Tu Gianina'

from .modelos.entidades import Articulo, Proveedor
from .almacenamiento.gestor_json import GestorJSON
from .servicios.articulo_servicio import ArticuloServicio
from .servicios.proveedor_servicio import ProveedorServicio

__all__ = [
    'Articulo',
    'Proveedor', 
    'GestorJSON',
    'ArticuloServicio',
    'ProveedorServicio'
]