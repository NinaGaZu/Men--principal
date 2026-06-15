# ============================================================================
# PROGRAMA: Frutería "Vitalidad"
# DESCRIPCIÓN: Calcula el monto total a pagar por kilos de mandarinas
#              aplicando descuentos según la cantidad adquirida
# AUTOR: Gianina Gaete
# ASIGNATURA: Programación Avanzada - IACC
# SEMANA: 1
# ============================================================================
def main():
    # Definición de constantes
    PRECIO_POR_KILO = 1500  # Precio en pesos chilenos (puede modificarse)

    # Mensaje de bienvenida
    print("=" * 60)
    print("FRUTERÍA 'VITALIDAD'")
    print("=" * 60)
    print("Bienvenido al sistema de cálculo de mandarinas")
    print("=" * 60)

    # Entrada de datos: Solicitar cantidad de kilos al usuario
    # Se utiliza float() para convertir el texto ingresado a número decimal
    kilos = float(input("\nIngrese la cantidad de kilos de mandarinas: "))

    # Validación inicial: Los kilos no pueden ser negativos
    if kilos < 0:
        print("\n❌ ERROR: La cantidad de kilos no puede ser negativa.")
        print("Por favor, ingrese un valor válido.")
    else:
        # Estructura condicional para determinar el descuento según la tabla
        if kilos >= 0 and kilos <= 2:
            porcentaje_descuento = 10
        elif kilos >= 2.01 and kilos <= 5:
            porcentaje_descuento = 20
        elif kilos >= 5.01 and kilos <= 10:
            porcentaje_descuento = 30
        elif kilos >= 10.01:
            porcentaje_descuento = 40
        
        # Cálculos utilizando operadores aritméticos
        subtotal = kilos * PRECIO_POR_KILO  # Multiplicación
        monto_descuento = subtotal * (porcentaje_descuento / 100)  # Cálculo del descuento
        total_a_pagar = subtotal - monto_descuento  # Resta
        
        # Salida de resultados: Mostrar información al usuario
        print("\n" + "=" * 60)
        print("DETALLE DE LA COMPRA")
        print("=" * 60)
        print(f"Precio por kilo:           ${PRECIO_POR_KILO:,.0f}")
        print(f"Cantidad de kilos:         {kilos:.2f} kg")
        print(f"Subtotal:                  ${subtotal:,.0f}")
        print(f"Descuento aplicado:        {porcentaje_descuento}%")
        print(f"Monto descuento:           ${monto_descuento:,.0f}")
        print("-" * 60)
        print(f"TOTAL A PAGAR:             ${total_a_pagar:,.0f}")
        print("=" * 60)
        print("\n¡Gracias por su compra en Frutería Vitalidad!")
        print("=" * 60)
if __name__ == "__main__":
    main()