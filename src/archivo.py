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
    # Verificar la ruta del archivo CSV y si existe antes de intentar cargarlo #
    print("Ruta absoluta:", os.path.abspath(archivo_csv))
    print("¿Existe?", os.path.exists(archivo_csv))
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
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"País encontrado: {pais['nombre']}")
            print(f"Población:  {pais['poblacion']:,} hab")
            print(f"Superficie: {pais['superficie']:,.2f} km²")
            print(f"Continente: {pais['continente']}")
            return pais
    print("País no encontrado.")
    return None


def filtrar_paises(paises):
    continente = input("Ingrese el continente a filtrar: ").strip()
    filtrados = [p for p in paises if p["continente"].lower() == continente.lower()]
    if filtrados:
        print(f"\nPaíses en {continente}:")
        for pais in filtrados:
            print(f"  - {pais['nombre']}")
    else:
        print(f"No se encontraron países en {continente}.")