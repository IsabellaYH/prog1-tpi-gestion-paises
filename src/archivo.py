import csv
import os
## Ruta al archivo CSV de países, utilizando una ruta relativa para mayor portabilidad ##
archivo_csv = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "paises.csv"
)

def cargar_csv():
    datos = []
    # Cargar datos desde el archivo CSV y manejar posibles errores como archivo no encontrado o errores de formato #
    try:
        with open(archivo_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            # Cargar cada fila del archivo CSV en una lista de diccionarios #
            for fila in lector:
                datos.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    # Manejo de errores: archivo no encontrado, errores de formato o problemas de codificación #
    except FileNotFoundError:
        print(f"No se encontró: {archivo_csv}")

    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    return datos

def guardar_csv(paises):
    try:                                
        with open(archivo_csv, mode="w", encoding="utf-8", newline='') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            ## Escribir cada país de la lista en el archivo CSV, asegurándose de que los datos se guarden correctamente y manejando posibles errores durante el proceso de escritura #
            for pais in paises:
                # Proceso de escritura #
                escritor.writerow(pais)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def buscar_pais(paises, nombre):
    encontrados = []

    # Permite búsqueda exacta o parcial
    for pais in paises:
        if nombre.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    if encontrados:
        print("\n=== RESULTADOS DE LA BÚSQUEDA ===")

        for pais in encontrados:
            print(f"\nPaís encontrado: {pais['nombre']}")
            print(f"Población:  {pais['poblacion']:,} hab")
            print(f"Superficie: {pais['superficie']:,.2f} km²")
            print(f"Continente: {pais['continente']}")

        return encontrados

    print("País no encontrado.")
    return None


def filtrar_paises(paises):
    print("\n=== FILTRAR PAÍSES ===")
    print("Seleccione una opción de filtrado:")
    print("1. Por continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    opcion = input("Opción: ")

    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
    else:
        print("Opción no válida.")
        return
    
def filtrar_por_continente(paises):
    # Permite filtrar países por continente, mostrando solo aquellos que coincidan con el continente ingresado por el usuario #
    continente = input("Ingrese el continente a filtrar: ").strip()
    filtrados = [p for p in paises if p["continente"].lower() == continente.lower()]

    if filtrados:
        print(f"\nPaíses en {continente}:")
        for pais in filtrados:
            print(f"  - {pais['nombre']}")
    else:
        print(f"No se encontraron países en {continente}.")
        return
    
def filtrar_por_poblacion(paises):
    #filtro por rango de población, permitiendo al usuario ingresar un rango mínimo y máximo para mostrar solo los países cuya población se encuentre dentro de ese rango #
    while True:
        valor = input("Ingrese el rango de población (min-max): ").strip()
        if "-" in valor:
            try:
                min_poblacion, max_poblacion = map(int, valor.split("-"))
                filtrados = [p for p in paises if min_poblacion <= p["poblacion"] <= max_poblacion]
                if filtrados:
                    print(f"\nPaíses con población entre {min_poblacion} y {max_poblacion}:")
                    for pais in filtrados:
                        print(f"  - {pais['nombre']}")
                else:
                    print(f"No se encontraron países con población entre {min_poblacion} y {max_poblacion}.")
                return
            except ValueError:
                print("Rango no válido. Intente nuevamente.")
        else:
            print("Formato incorrecto. Use el formato min-max.")
            return

def filtrar_por_superficie(paises):
#filtro por rango de superficie, permitiendo al usuario ingresar un rango mínimo y máximo para mostrar solo los países cuya superficie se encuentre dentro de ese rango #
    while True:
        valor = input("Ingrese el rango de superficie (min-max): ").strip()
        if "-" in valor:
            try:
                min_superficie, max_superficie = map(float, valor.split("-"))
                filtrados = [p for p in paises if min_superficie <= p["superficie"] <= max_superficie]
                if filtrados:
                    print(f"\nPaíses con superficie entre {min_superficie} y {max_superficie} km²:")
                    for pais in filtrados:
                        print(f"  - {pais['nombre']}")
                else:
                    print(f"No se encontraron países con superficie entre {min_superficie} y {max_superficie} km².")
                return
            except ValueError:
                print("Rango no válido. Intente nuevamente.")
        else:
            print("Formato incorrecto. Use el formato min-max.")
            return
