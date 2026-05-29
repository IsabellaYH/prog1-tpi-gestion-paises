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
        elif opcion == "2":
            if paises:
                print("Datos de países:")
                for pais in paises:
                    print(pais)
            else:
                print("No se han cargado datos. Por favor, cargue los datos primero.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break

main()