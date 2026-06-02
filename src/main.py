from archivo import cargar_csv,  filtrar_paises, buscar_pais
from paises import agregar_pais, actualizar_pais, eliminar_pais, ordenar_paises, estadisticas

def menu():
    print("\n=== GESTIÓN DE PAÍSES ===")
    print("1. Cargar datos")
    print("2. Mostrar datos")
    print("3. Agregar país")
    print("4. Actualizar país")
    print("5. Buscar país")
    print("6. Filtrar países")
    print("7. Ordenar países")
    print("8. Estadísticas")
    print("9. Eliminar país")
    print("10. Salir")

def main():
    paises = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            paises = cargar_csv()
            print("Datos cargados exitosamente.")
            print("Cantidad de países cargados:", len(paises))
        elif opcion == "2":
            if paises:
                print("\n=== LISTA DE PAÍSES ===")
                for pais in paises:
                    print(
                        f"Nombre: {pais['nombre']} | "
                        f"Población: {pais['poblacion']:,} | "
                        f"Superficie: {pais['superficie']:,.2f} km² | "
                        f"Continente: {pais['continente']}"
                    )
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "3":
            agregar_pais(paises)
        elif opcion == "4":
            if paises:
                actualizar_pais(paises) 
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "5":
            if paises:
                nombre = input("Ingrese el nombre del país a buscar: ").strip()
                buscar_pais(paises, nombre)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "6":
            if paises:
                filtrar_paises(paises)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "7":
            if paises:
                ordenar_paises(paises)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "8":
            if paises:
                estadisticas(paises)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "9":
            if paises:
                eliminar_pais(paises)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "10":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no válida. Seleccione del 1 al 10")
main()