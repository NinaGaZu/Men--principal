# Módulo para gestionar el registro de empleados usando diccionarios

base_de_datos_empleados = {}

def agregar_empleado(nombre, salario, fecha_ingreso):
    """Agrega un nuevo empleado al diccionario de la base de datos."""
    base_de_datos_empleados[nombre] = {
        "salario": salario,
        "fecha_ingreso": fecha_ingreso
    }
    return base_de_datos_empleados[nombre]

def obtener_empleado(nombre):
    """Retorna la información de un empleado específico."""
    return base_de_datos_empleados.get(nombre)

