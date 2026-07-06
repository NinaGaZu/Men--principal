# calculos_rrhh.py
# Módulo que utiliza el módulo estándar datetime para cálculos de RRHH

from datetime import datetime

def calcular_antiguedad(fecha_ingreso_str):
    """Calcula la antigüedad en años completos dada una fecha en formato YYYY-MM-DD."""
    fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d")
    fecha_actual = datetime.now()
    
    # Cálculo base de años
    antiguedad = fecha_actual.year - fecha_ingreso.year
    
    # Ajuste si el mes y día actual aún no llega al aniversario de ingreso
    if (fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day):
        antiguedad -= 1
        
    return antiguedad

def asignar_beneficios(antiguedad):
    """Determina los beneficios según la antigüedad del empleado."""
    beneficios = []
    if antiguedad > 5:
        beneficios.append("Bono anual")
        beneficios.append("Días adicionales de vacaciones")
    elif antiguedad > 3:
        beneficios.append("Bono anual")
    else:
        beneficios.append("Sin beneficios adicionales por antigüedad")
    return beneficios