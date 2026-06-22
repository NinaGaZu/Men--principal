# ============================================================================
# PROGRAMA: Librería "Hogwarts" - Gestión de Inventario
# DESCRIPCIÓN: Administra el inventario de libros validando datos con excepciones
# AUTOR: Gianina Gaete
# ASIGNATURA: Programación Avanzada - IACC
# SEMANA: 3
# ============================================================================

def solicitar_cantidad_libros(mensaje):
    """
    Función que solicita una cantidad de libros y valida que sea un número entero positivo
    Parámetro:
        mensaje: Mensaje a mostrar al usuario
    Retorna:
        cantidad: Número entero positivo válido
    """
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad < 0:
                raise ValueError("❌ ERROR: La cantidad no puede ser negativa. Intente nuevamente.")
            return cantidad
        except ValueError as ve:
            if "invalid literal" in str(ve):
                print("❌ ERROR: Debe ingresar un número entero válido. Intente nuevamente.")
            else:
                print(ve)
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            exit()

def verificar_inventario(existencia, vendidos):
    """
    Función que verifica si la cantidad vendida es válida según el inventario
    Parámetros:
        existencia: Cantidad de libros en inventario
        vendidos: Cantidad de libros vendidos
    Retorna:
        True si es válido, False en caso contrario
    """
    if vendidos > existencia:
        return False
    return True

def calcular_inventario_final(existencia, vendidos):
    """
    Función que calcula el inventario final después de las ventas
    Parámetros:
        existencia: Cantidad inicial en inventario
        vendidos: Cantidad vendida
    Retorna:
        inventario_final: Cantidad restante en inventario
    """
    return existencia - vendidos

def main():
    """Función principal del programa"""
    print("\n" + "=" * 70)
    print("           LIBRERÍA 'HOGWARTS' - SISTEMA DE INVENTARIO")
    print("=" * 70)
    print("Bienvenido al sistema de gestión de inventario de libros")
    print("=" * 70)
    
    while True:
        try:
            # Solicitar cantidad actual de libros en existencia
            print("\n--- INGRESO DE DATOS DEL INVENTARIO ---")
            existencia = solicitar_cantidad_libros("\nIngrese la cantidad actual de libros en existencia: ")
            
            # Solicitar cantidad de libros vendidos
            vendidos = solicitar_cantidad_libros("Ingrese la cantidad de libros vendidos durante el día: ")
            
            # Verificar si la cantidad vendida excede el inventario
            if not verificar_inventario(existencia, vendidos):
                print("\n" + "!" * 70)
                print("❌ ERROR DE INVENTARIO:")
                print(f"   La cantidad vendida ({vendidos}) NO puede exceder la cantidad")
                print(f"   disponible en inventario ({existencia}).")
                print("!" * 70)
                print("\nPor favor, ingrese los datos nuevamente.\n")
                continue
            
            # Calcular inventario final
            inventario_final = calcular_inventario_final(existencia, vendidos)
            
            # Mostrar resultados
            print("\n" + "=" * 70)
            print("           RESUMEN DEL INVENTARIO - LIBRERÍA HOGWARTS")
            print("=" * 70)
            print(f"📚 Cantidad inicial en inventario:     {existencia} libros")
            print(f"📖 Cantidad vendida en el día:        {vendidos} libros")
            print("-" * 70)
            print(f"✅ Inventario final disponible:        {inventario_final} libros")
            print("=" * 70)
            
            # Verificar si es necesario reabastecer
            if inventario_final == 0:
                print("\n🚨 ALERTA DE STOCK AGOTADO:")
                print("   No quedan libros en inventario.")
                print("   Es urgente realizar un nuevo pedido.")
                print("=" * 70)
            elif inventario_final < 10:
                print("\n⚠️  ALERTA DE STOCK BAJO:")
                print(f"   Quedan solo {inventario_final} libros en inventario.")
                print("   Se recomienda realizar un nuevo pedido pronto.")
                print("=" * 70)
            else:
                print("\n✅ Estado del inventario: NORMAL")
                print("   El inventario está en niveles adecuados.")
                print("=" * 70)
            
            # Preguntar si desea continuar
            print("\n¿Desea realizar otra consulta de inventario?")
            continuar = input("Ingrese 'S' para continuar o cualquier tecla para salir: ").strip().upper()
            
            if continuar != 'S':
                print("\n" + "=" * 70)
                print("¡Gracias por usar el sistema de inventario de Librería Hogwarts!")
                print("¡Hasta pronto!")
                print("=" * 70)
                break
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            print("¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("Por favor, intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()