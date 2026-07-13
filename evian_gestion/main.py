"""
Módulo principal - Punto de entrada del sistema
"""

from .servicios.articulo_servicio import ArticuloServicio
from .servicios.proveedor_servicio import ProveedorServicio


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE PROVEEDORES Y ARTÍCULOS - EVIAN")
    print("="*60)
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar artículo")
    print("2. Agregar proveedor")
    print("3. Mostrar información")
    print("4. Salir del programa")


def ejecutar_sistema():
    """Función principal que ejecuta el sistema"""
    # Inicializar servicios
    servicio_articulos = ArticuloServicio()
    servicio_proveedores = ProveedorServicio()
    
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE PROVEEDORES Y ARTÍCULOS - EVIAN")
    print("="*60)
    
    # Menú principal
    while True:
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '1':
            servicio_articulos.agregar_articulo()
        
        elif opcion == '2':
            servicio_proveedores.agregar_proveedor()
        
        elif opcion == '3':
            servicio_articulos.mostrar_articulos()
            servicio_proveedores.mostrar_proveedores()
        
        elif opcion == '4':
            print("\n✓ Saliendo del programa. ¡Hasta luego!")
            print("="*60 + "\n")
            break
        
        else:
            print("\n✗ Opción no válida. Por favor, ingrese un número del 1 al 4.")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_sistema()