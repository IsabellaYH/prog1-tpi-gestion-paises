import csv
import os

archivo_csv = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "paises.csv"
)

def cargar_csv():
    datos = []
    print("Ruta absoluta:", os.path.abspath(archivo_csv))
    print("¿Existe?", os.path.exists(archivo_csv))
    try:
        with open(archivo_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                datos.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": float(fila["superficie"]),
                    "continente": fila["continente"]
                })

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
            for pais in paises:
                escritor.writerow(pais)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def buscar_pais(nombre):
    print(f"\n=== BUSCAR PAÍS: {nombre} ===")
    print("Ingresedo nombre del país a buscar:", nombre)
    try:
        while paises := cargar_csv():
            for pais in paises:
                if pais["nombre"].lower() == nombre.lower():
                    print(f"País encontrado: {pais['nombre']}")
                    print(f"Población: {pais['poblacion']}")
                    print(f"Superficie: {pais['superficie']} km²")
                    print(f"Continente: {pais['continente']}")
                    return pais
            print("País no encontrado.")
            return None
    except Exception as e:
        print(f"Error al buscar el país: {e}")
        return TypeError("Error el valor debe ser una cadena de texto.")
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")
        return SyntaxError("Error de sintaxis en la función buscar_pais.")
    except ValueError as e:
        print(f"Error de valor: {e}")
        return ValueError("Error de valor en la función buscar_pais.")  

def filtrar_paises(paises):
    try:
        with open(archivo_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = [fila for fila in lector]
    except FileNotFoundError:
        print("Error: No se encontró el archivo de datos.")
        return
    
    print("Filtrar países por continente:")
    while True:
        continente = input("Ingrese el continente (América, Europa, Asia, África, Oceanía): ")
        paises_filtrados = [pais for pais in paises if pais['continente'].lower() == continente.lower()]
        if paises_filtrados:
            print(f"Países en {continente}:")
            for pais in paises_filtrados:
                print(f"- {pais['nombre']}")
        else:
            print(f"No se encontraron países en el continente {continente}.")