# main.py
# Programa principal que importa los módulos y ejecuta el caso de prueba

from sistema_colegio import registro_empleados 
from sistema_colegio import calculos_rrhh

def main():
    print("\n--- REGISTRO DE NUEVO EMPLEADO ---")
    
    # 1. Ingreso de datos dinámicos por consola
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    
    # Convertimos a float para asegurar que sea un número (manejo básico)
    try:
        salario_empleado = int(input("Ingrese el salario: "))
    except ValueError:
        print("Error: Salario inválido. Se usará 0 como valor por defecto.")
        salario_empleado = 0
        
    fecha_ingreso_empleado = input("Ingrese la fecha de ingreso (Formato YYYY-MM-DD): ")
    
    # 2. Registro del empleado (La lógica interna no cambia)
    registro_empleados.agregar_empleado(nombre_empleado, salario_empleado, fecha_ingreso_empleado)
    datos_empleado = registro_empleados.obtener_empleado(nombre_empleado)
    
    # 3. Cálculo de antigüedad y beneficios (Los módulos trabajan igual)
    antiguedad = calculos_rrhh.calcular_antiguedad(datos_empleado["fecha_ingreso"])
    beneficios = calculos_rrhh.asignar_beneficios(antiguedad)
    
    # 4. Salida de información en pantalla
    print("\n--- INFORMACIÓN DEL EMPLEADO ---")
    print(f"Nombre: {nombre_empleado}")
    print(f"Salario: ${datos_empleado['salario']}") 
    print(f"Fecha de Ingreso (YYYY-MM-DD): {datos_empleado['fecha_ingreso']}")
    print(f"Antigüedad: {antiguedad} años")
    print(f"Beneficios Asignados: {', '.join(beneficios)}")
    print("--------------------------------\n")