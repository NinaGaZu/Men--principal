import fruteria
import tienda_de_ropa as tienda
import libreria_hogwarts as hogwarts
import heladeria_frosty_delights as heladeria

def mostrar_menu():
    while True:
        print("\n" + "="*30)
        print("   MENÚ PRINCIPAL DE PROYECTOS")
        print("="*30)
        print("1. Frutería Vitalidad")
        print("2. Tienda de Ropa")
        print("3. Librería Hogwarts")
        print("4. Heladería Frosty Delights")
        print("5. Salir")
        print("="*30)
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            fruteria.main()  # Llama a la función main del archivo fruteria.py
        elif opcion == "2":
            tienda.main()    # Llama a la función main del archivo tienda_de_ropa.py
        elif opcion == "3":
            hogwarts.main()  # Llama a la función main del archivo libreria_hogwarts.py
        elif opcion == "4":
            heladeria.main() # Llama a la función main del archivo heladeria_frosty_delights.py
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu()