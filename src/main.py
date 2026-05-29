from archivo import cargar_csv
from paises import agregar_pais

#modificable ... MENU EN PROGRESO
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
    print("9. Salir")


def main():
    paises = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            paises = cargar_csv()
            print("Datos cargados exitosamente.")
            print("Cantidad de países cargados:", len(paises))
            print(paises)
        elif opcion == "2":
            if paises:
                print("\n=== LISTA DE PAISES ===")
                
                for pais in paises:
                    print(
                        f"Nombre: {pais['nombre']} | "
                        f"Población: {pais['poblacion']} | "
                        f"Superficie: {pais['superficie']} km² | "
                        f"Continente: {pais['continente']}"
                    )
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "3":
            agregar_pais(paises)
        elif opcion == "9":
            print("Saliendo del programa.")
            break

main()