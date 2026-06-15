# ============================================================================
# PROGRAMA: Tienda de Ropa - Menú Interactivo
# DESCRIPCIÓN: Calcula descuentos mayoristas y área de cilindros
# AUTOR: Gianina Gaete
# ASIGNATURA: Programación Avanzada - IACC
# SEMANA: 2
# ============================================================================

# Constante
PI = 3.1416
PRECIO_BASE_PRENDA = 40

def calcular_descuento_mayorista(cantidad, precio_base):
    """
    Calcula el descuento por compra mayorista
    Parámetros:
        cantidad: Número de unidades del artículo
        precio_base: Precio unitario base
    Retorna:
        Tupla (total_a_pagar, porcentaje_descuento, monto_descuento)
    """
    if cantidad >= 20:
        porcentaje_descuento = 0.25  # 25%
    elif cantidad >= 10:
        porcentaje_descuento = 0.15  # 15%
    else:
        porcentaje_descuento = 0
    
    subtotal = cantidad * precio_base
    monto_descuento = subtotal * porcentaje_descuento
    total_a_pagar = subtotal - monto_descuento
    
    return total_a_pagar, porcentaje_descuento, monto_descuento

def calcular_area_cilindro(radio, altura):
    """
    Calcula el área de la superficie lateral de un cilindro
    Fórmula: area = 2 * pi * radio * altura
    Parámetros:
        radio: Radio de la base del cilindro
        altura: Altura del cilindro
    Retorna:
        area: Área de la superficie lateral
    """
    area = 2 * PI * radio * altura
    return area

def factorial(n):
    """
    Función recursiva que calcula el factorial de un número
    Parámetro:
        n: Número entero no negativo
    Retorna:
        El factorial de n
    """
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)
    
# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
# Salida: El factorial de 5 es: 120

# Definición de la función
def calcular_precio(producto, precio, impuesto):
    # 'producto', 'precio' e 'impuesto' son PARÁMETROS
    precio_total = precio * (1 + impuesto)
    return precio_total

# Llamada a la función
producto = "Camisa"
precio = 40
impuesto = 0.15
# "Camisa", 40 y 0.15 son ARGUMENTOS

print(f"resultado = {calcular_precio(producto, precio, impuesto)}")

def mostrar_menu():
    """Muestra el menú de opciones al usuario"""
    print("\n" + "=" * 60)
    print("           TIENDA DE ROPA - MENÚ PRINCIPAL")
    print("=" * 60)
    print("1. Calcular descuento por compra mayorista")
    print("2. Calcular área de la superficie lateral de un cilindro")
    print("3. Salir del programa")
    print("=" * 60)

def validar_opcion(mensaje):
    """
    Valida que el usuario ingrese una opción válida (1, 2 o 3)
    Usa recursividad para solicitar nuevamente si el valor es inválido
    """
    try:
        opcion = int(input(mensaje))
        if opcion in [1, 2, 3]:
            return opcion
        else:
            print("\n❌ ERROR: Opción no válida. Debe ingresar 1, 2 o 3.")
            return validar_opcion("Ingrese nuevamente la opción (1-3): ")
    except ValueError:
        print("\n❌ ERROR: Debe ingresar un número entero (1, 2 o 3).")
        return validar_opcion("Ingrese nuevamente la opción (1-3): ")

def main():
    """Función principal del programa"""
    print("\n" + "=" * 60)
    print("     BIENVENIDO A LA TIENDA DE ROPA")
    print("=" * 60)
    
    while True:
        mostrar_menu()
        opcion = validar_opcion("Seleccione una opción (1-3): ")
        
        if opcion == 1:
            # Opción 1: Calcular descuento mayorista
            print("\n--- CALCULAR DESCUENTO POR COMPRA MAYORISTA ---")
            print(f"Precio base por prenda: ${PRECIO_BASE_PRENDA}")
            
            try:
                cantidad = int(input("Ingrese la cantidad de unidades: "))
                
                if cantidad <= 0:
                    print("\n❌ ERROR: La cantidad debe ser mayor a 0.")
                else:
                    # Llamada a la función con argumentos
                    total, descuento, monto_desc = calcular_descuento_mayorista(
                        cantidad, PRECIO_BASE_PRENDA
                    )
                    
                    print("\n" + "-" * 60)
                    print("DETALLE DE LA COMPRA")
                    print("-" * 60)
                    print(f"Cantidad de prendas:        {cantidad}")
                    print(f"Precio unitario:            ${PRECIO_BASE_PRENDA}")
                    print(f"Subtotal:                   ${cantidad * PRECIO_BASE_PRENDA}")
                    
                    if descuento > 0:
                        print(f"Descuento aplicado:         {int(descuento * 100)}%")
                        print(f"Monto descuento:            ${monto_desc:.2f}")
                    else:
                        print("Descuento aplicado:         0% (compra minorista)")
                        print("Monto descuento:            $0")
                        print("\n💡 Para obtener descuento:")
                        print("   - 10-19 unidades: 15% de descuento")
                        print("   - 20 o más unidades: 25% de descuento")
                    
                    print("-" * 60)
                    print(f"TOTAL A PAGAR:              ${total:.2f}")
                    print("=" * 60)
                    
            except ValueError:
                print("\n❌ ERROR: Debe ingresar un número entero válido.")
        
        elif opcion == 2:
            # Opción 2: Calcular área de cilindro
            print("\n--- CALCULAR ÁREA DE SUPERFICIE LATERAL DE UN CILINDRO ---")
            print(f"Fórmula: área = 2 * π * radio * altura")
            print(f"Valor de π utilizado: {PI}")
            
            try:
                radio = float(input("\nIngrese el radio de la base del cilindro: "))
                altura = float(input("Ingrese la altura del cilindro: "))
                
                if radio <= 0 or altura <= 0:
                    print("\n❌ ERROR: El radio y la altura deben ser mayores a 0.")
                else:
                    # Llamada a la función con argumentos
                    area = calcular_area_cilindro(radio, altura)
                    
                    print("\n" + "-" * 60)
                    print("RESULTADO DEL CÁLCULO")
                    print("-" * 60)
                    print(f"Radio:                      {radio}")
                    print(f"Altura:                     {altura}")
                    print(f"Área de superficie lateral: {area:.2f}")
                    print("=" * 60)
                    
            except ValueError:
                print("\n❌ ERROR: Debe ingresar números válidos.")
        
        elif opcion == 3:
            # Opción 3: Salir del programa
            print("\n" + "=" * 60)
            print("¡Gracias por usar el sistema de la Tienda de Ropa!")
            print("¡Hasta luego!")
            print("=" * 60)
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()

