from archivo import guardar_csv


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
    guardar_csv(paises)
    print(f"País '{nombre}' agregado exitosamente.")
    

def actualizar_pais (paises):
    print ("\n=== ACTUALIZAR PAÍS ===")
    nombre = input ("Ingrese el nombre del país a actualizar: ")
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"País encontrado: {pais['nombre']}")
            nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
            nueva_poblacion = input("Nueva población (dejar en blanco para no cambiar): ")
            nueva_superficie = input("Nueva superficie (dejar en blanco para no cambiar): ")
            nuevo_continente = input("Nuevo continente (dejar en blanco para no cambiar): ")

            if nuevo_nombre:
                pais["nombre"] = nuevo_nombre
            if nueva_poblacion:
                pais["poblacion"] = int(nueva_poblacion)
            if nueva_superficie:
                pais["superficie"] = float(nueva_superficie)
            if nuevo_continente:
                pais["continente"] = nuevo_continente

            print(f"País '{pais['nombre']}' actualizado exitosamente.")
            return
    print("País no encontrado.")

def eliminar_pais(paises):
    print("\n=== ELIMINAR PAÍS ===")
    nombre = input("Ingrese el nombre del país a eliminar: ")
    for i, pais in enumerate(paises):
        if pais["nombre"].lower() == nombre.lower():
            confirmacion = input(f"¿Está seguro que desea eliminar '{pais['nombre']}'? (s/n): ")
            if confirmacion.lower() == 's':
                del paises[i]
                print(f"País '{nombre}' eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("País no encontrado.")
    