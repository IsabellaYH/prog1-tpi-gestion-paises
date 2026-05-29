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