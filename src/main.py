from archivo import cargar_csv, buscar_pais, filtrar_paises
from paises import agregar_pais, actualizar_pais, eliminar_pais

### ---- MENU PRINCIPAL ---- ###
def menu():
    print("\n=== GESTIÓN DE PAÍSES ===")
    print("1. Cargar datos")
    print("2. Mostrar datos")
    print("3. Agregar país")
    print("4. Actualizar país")
    print("5. Buscar país")
    print("6. Filtrar países")
    print("7. Ordenar países")
    print("8.Eliminar país")
    print("9. Estadísticas")
    print("10. Salir")

### ---- FUNCION PARA INGRESAR EN OPCIONES DEL MENÚ ---- ###
def main():
    paises = []
    # El programa se ejecutará hasta que el usuario seleccione la opción de salir (10) #
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        ## Validación de la opción ingresada ##
        if opcion == "1":
            # Cargar datos desde el archivo CSV #
            paises = cargar_csv()
            print("Datos cargados exitosamente.")
            print("Cantidad de países cargados:", len(paises))
            print(paises)
        elif opcion == "2":
            # Mostrar datos cargados de la sesion #
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
            # Agregar un nuevo país a la lista y guardar en el archivo CSV #
            agregar_pais(paises)
        elif opcion == "4":
            # Actualizar un país existente en la lista y guardar los cambios en el archivo CSV #
            actualizar_pais(paises)
        elif opcion == "5":
            # Buscar un país por su nombre y mostrar sus detalles 
            nombre = input("Ingrese el nombre del país a buscar: ").strip()
            if nombre:
             buscar_pais(paises, nombre)
            else:
                print("Debe ingresar un nombre.")
            nombre = input("Ingrese el nombre del país a buscar: ")
        
        elif opcion == "6":
            # Filtrar países por continente y mostrar los resultados #
            filtrar_paises(paises)
        elif opcion == "7":
            # Ordenar países por nombre de la A-Z
            print("Funcionalidad de ordenar países en desarrollo.")
        elif opcion == "8":
            # Eliminar un país de la lista y guardar los cambios en el archivo CSV #
            eliminar_pais(paises)
        elif opcion == "9":
            # Mostrar_estadisticas (lista_paises)
            print("Funcionalidad de estadísticas en desarrollo.")
        elif opcion == "10":
            # Salida del programa #
            print("Saliendo del programa.")
            break
        else:
            try:
                # Validación de error de la opción ingresada #
                raise ValueError("Opción no válida. Por favor, seleccione una opción del 1 al 10.")
            except ValueError as e:
                print(e)

main()