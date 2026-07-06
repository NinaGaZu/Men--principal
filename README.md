# Menú Principal - Programación Avanzada IACC

## Descripción
Sistema de menú interactivo que integra programas desarrollados en Python del ramo Programación Avanzada:
- **Frutería Vitalidad**: Calcula descuentos por compra de mandarinas
- **Tienda de Ropa**: Calcula descuentos mayoristas y área de cilindros
- **Librería Hogwarts**: Administra el inventario de libros
- **Heladería Frosty Delights**: Gestiona el inventario de sabores de helado
- **Sistema de Gestión de Empleados**: Registra empleados, calcula su antigüedad y asigna beneficios mediante el uso de módulos y paquetes (Semana 5).

## Estructura del Proyecto
- `menu_principal.py` - Menú principal que integra ambos programas
- `fruteria.py` - Programa de la frutería (Semana 1)
- `tienda_de_ropa.py` - Programa de la tienda de ropa (Semana 2)
- `libreria_hogwarts.py` - Programa de la librería (Semana 3)
- `heladeria_frosty_delights.py` - Programa de la heladería (Semana 4)
- `sistema_colegio/` - Paquete para el sistema de gestión de empleados.
  - `__init__.py` - Archivo inicializador que convierte la carpeta en un paquete.
  - `main.py` - Módulo principal que ejecuta el sistema.
  - `registro_empleados.py` - Módulo reutilizable para gestionar el registro de empleados.
  - `calculos_rrhh.py` - Módulo que utiliza `datetime` para calcular antigüedad y beneficios.

## Requisitos
- Python 3.x
- Visual Studio Code

## Ejecución
```bash
python menu_principal.py
```
## Autor
Gianina Gaete Zurita
