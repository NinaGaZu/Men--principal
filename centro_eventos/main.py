"""
Script principal para ejecutar el sistema CentroEventosArenasX
"""

from .vistas.ventana_principal import VentanaPrincipal


def main():
    """Función principal que ejecuta la aplicación"""
    app = VentanaPrincipal()
    app.ejecutar()


if __name__ == "__main__":
    main()