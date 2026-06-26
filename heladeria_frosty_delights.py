# ============================================================================
# PROGRAMA: Heladería "Frosty Delights" - Gestión de Inventario
# DESCRIPCIÓN: Administra el inventario de sabores de helado
# AUTOR: Gianina Gaete
# ASIGNATURA: Programación Avanzada - IACC
# SEMANA: 4
# ============================================================================

def mostrar_menu():
    """Muestra el menú de opciones al usuario"""
    print("\n" + "=" * 70)
    print("           HELADERÍA 'FROSTY DELIGHTS' - GESTIÓN DE INVENTARIO")
    print("=" * 70)
    print("1. Registrar nuevo sabor de helado")
    print("2. Mostrar todos los sabores registrados")
    print("3. Buscar sabor por nombre")
    print("4. Actualizar stock de un sabor")
    print("5. Salir del programa")
    print("=" * 70)

def registrar_sabor(inventario):
    """
    Función para registrar un nuevo sabor de helado
    Parámetro:
        inventario: Lista que contiene los diccionarios de sabores
    Retorna:
        inventario actualizado
    """
    print("\n--- REGISTRAR NUEVO SABOR DE HELADO ---")
    
    nombre = input("Ingrese el nombre del sabor: ").strip().capitalize()
    
    # Verificar si el sabor ya existe
    for sabor in inventario:
        if sabor["nombre"].lower() == nombre.lower():
            print(f"\n❌ ERROR: El sabor '{nombre}' ya está registrado en el inventario.")
            return inventario
    
    try:
        precio = float(input("Ingrese el precio del sabor: $"))
        if precio <= 0:
            print("❌ ERROR: El precio debe ser mayor a 0.")
            return inventario
        
        stock = int(input("Ingrese la cantidad en stock: "))
        if stock < 0:
            print("❌ ERROR: El stock no puede ser negativo.")
            return inventario
        
        # Crear diccionario con la información del sabor
        nuevo_sabor = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }
        
        # Agregar a la lista de inventario
        inventario.append(nuevo_sabor)
        
        print(f"\n✅ SABOR REGISTRADO EXITOSAMENTE:")
        print(f"   Nombre: {nombre}")
        print(f"   Precio: ${precio:.2f}")
        print(f"   Stock: {stock} unidades")
        
    except ValueError:
        print("\n❌ ERROR: Ingrese valores numéricos válidos para precio y stock.")
    
    return inventario

def mostrar_inventario(inventario):
    """
    Función para mostrar todos los sabores registrados
    Parámetro:
        inventario: Lista de diccionarios con los sabores
    """
    print("\n" + "=" * 70)
    print("           INVENTARIO DE SABORES DE HELADO")
    print("=" * 70)
    
    if not inventario:
        print("\n⚠️  No hay sabores registrados en el inventario.")
        print("=" * 70)
        return
    
    print(f"\n{'SABOR':<20} {'PRECIO':<15} {'STOCK':<10} {'ESTADO':<15}")
    print("-" * 70)
    
    for sabor in inventario:
        nombre = sabor["nombre"]
        precio = sabor["precio"]
        stock = sabor["stock"]
        
        # Determinar estado del stock
        if stock == 0:
            estado = "AGOTADO"
        elif stock < 20:
            estado = "STOCK BAJO"
        else:
            estado = "DISPONIBLE"
        
        print(f"{nombre:<20} ${precio:<14.2f} {stock:<10} {estado:<15}")
    
    print("=" * 70)
    print(f"Total de sabores registrados: {len(inventario)}")
    print("=" * 70)

def buscar_sabor(inventario):
    """
    Función para buscar un sabor por nombre
    Parámetro:
        inventario: Lista de diccionarios con los sabores
    """
    print("\n--- BUSCAR SABOR POR NOMBRE ---")
    nombre = input("Ingrese el nombre del sabor a buscar: ").strip().capitalize()
    
    encontrado = False
    for sabor in inventario:
        if sabor["nombre"].lower() == nombre.lower():
            print("\n" + "=" * 70)
            print("           INFORMACIÓN DEL SABOR ENCONTRADO")
            print("=" * 70)
            print(f"Nombre:  {sabor['nombre']}")
            print(f"Precio:  ${sabor['precio']:.2f}")
            print(f"Stock:   {sabor['stock']} unidades")
            
            if sabor['stock'] == 0:
                print("Estado:  ❌ AGOTADO")
            elif sabor['stock'] < 20:
                print("Estado:  ⚠️  STOCK BAJO - Reabastecer pronto")
            else:
                print("Estado:  ✅ DISPONIBLE")
            print("=" * 70)
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n❌ ERROR: El sabor '{nombre}' no se encuentra en el inventario.")

def actualizar_stock(inventario):
    """
    Función para actualizar el stock de un sabor
    Parámetro:
        inventario: Lista de diccionarios con los sabores
    Retorna:
        inventario actualizado
    """
    print("\n--- ACTUALIZAR STOCK ---")
    nombre = input("Ingrese el nombre del sabor a actualizar: ").strip().capitalize()
    
    for sabor in inventario:
        if sabor["nombre"].lower() == nombre.lower():
            print(f"\nSabor encontrado: {sabor['nombre']}")
            print(f"Stock actual: {sabor['stock']} unidades")
            
            try:
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                if nuevo_stock < 0:
                    print("❌ ERROR: El stock no puede ser negativo.")
                    return inventario
                
                sabor["stock"] = nuevo_stock
                print(f"\n✅ STOCK ACTUALIZADO EXITOSAMENTE:")
                print(f"   {nombre}: {nuevo_stock} unidades")
                
            except ValueError:
                print("\n❌ ERROR: Ingrese un número entero válido.")
            
            return inventario
    
    print(f"\n❌ ERROR: El sabor '{nombre}' no se encuentra en el inventario.")
    return inventario

def main():
    """Función principal del programa"""
    # Inicializar inventario como lista vacía
    inventario = []
    
    print("\n" + "=" * 70)
    print("     BIENVENIDO A LA HELADERÍA 'FROSTY DELIGHTS'")
    print("=" * 70)
    print("Sistema de Gestión de Inventario de Sabores de Helado")
    print("=" * 70)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            inventario = registrar_sabor(inventario)
        
        elif opcion == "2":
            mostrar_inventario(inventario)
        
        elif opcion == "3":
            buscar_sabor(inventario)
        
        elif opcion == "4":
            inventario = actualizar_stock(inventario)
        
        elif opcion == "5":
            print("\n" + "=" * 70)
            print("¡Gracias por usar el sistema de inventario de Frosty Delights!")
            print("¡Hasta pronto!")
            print("=" * 70)
            break
        
        else:
            print("\n❌ ERROR: Opción no válida. Por favor, seleccione una opción del 1 al 5.")

# Ejecutar el programa
if __name__ == "__main__":
    main()