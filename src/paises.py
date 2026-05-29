def agregar_pais(paises):
    print("\n=== AGREGAR NUEVO PAÍS ===")
    nombre = input("Nombre del país: ")
    poblacion = int(input("Población: "))
    superficie = float(input("Superficie (km²): "))
    continente = input("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    print(f"País '{nombre}' agregado exitosamente.")
