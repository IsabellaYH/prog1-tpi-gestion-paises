import csv
archivo_csv = '.../data/paises.csv'

def cargar_csv():
    datos = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append({
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': float(fila['superficie']),
                    'continente': fila['continente']
                })
            
    except FileNotFoundError:
        print("Error: No se encontró el archivo paises.csv")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return datos