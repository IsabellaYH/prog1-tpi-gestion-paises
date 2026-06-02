from archivo import cargar_csv, buscar_pais, filtrar_paises
from paises import agregar_pais, actualizar_pais, eliminar_pais, ordenar_paises, estadisticas 

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
            eliminar_pais(paises)          
        elif opcion == "6":
            nombre = input("Ingrese el nombre del país a buscar: ").strip()
            if nombre:
             buscar_pais(paises, nombre)
            else:
                print("Debe ingresar un nombre.")
        elif opcion == "7":
            filtrar_paises(paises)
        elif opcion == "8":
            ordenar_paises(paises)
        elif opcion == "9":
            if paises:
                estadisticas(paises)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "10":
            print("Saliendo del programa.")
        break