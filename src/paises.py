from archivo import guardar_csv
from validaciones import validar_texto, validar_entero, validar_confirmacion  

### ---- FUNCIONES PARA AGREGAR, ACTUALIZAR Y ELIMINAR PAÍSES ---- ###

def agregar_pais(paises):          
    print("\n=== AGREGAR NUEVO PAÍS ===")
    nombre     = validar_texto("Nombre del país: ", "nombre")
    # validación de duplicado
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        print(f"Error: el país '{nombre}' ya existe.")
        return

    poblacion  = validar_entero("Población: ", "población")
    superficie = validar_entero("Superficie (km²): ", "superficie")
    continente = validar_texto("Continente: ", "continente")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    guardar_csv(paises)
    print(f"País '{nombre}' agregado exitosamente.")  

def actualizar_pais(paises):
    print("\n=== ACTUALIZAR PAÍS ===")
    nombre = validar_texto("Ingrese el nombre del país a actualizar: ", "nombre")
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"País encontrado: {pais['nombre']}")
            nuevo_nombre   = input("Nuevo nombre (dejar en blanco para no cambiar): ").strip()
            nueva_poblacion  = validar_entero("Nueva población (dejar en blanco para no cambiar): ", "población")
            nueva_superficie = validar_entero("Nueva superficie (dejar en blanco para no cambiar): ", "superficie")
            nuevo_continente = input("Nuevo continente (dejar en blanco para no cambiar): ").strip()

            if nuevo_nombre:
                pais["nombre"] = nuevo_nombre
            if nueva_poblacion:
                pais["poblacion"] = nueva_poblacion
            if nueva_superficie:
                pais["superficie"] = nueva_superficie
            if nuevo_continente:
                pais["continente"] = nuevo_continente

            guardar_csv(paises)
            print(f"País '{pais['nombre']}' actualizado exitosamente.")
            return
    print("País no encontrado.")



def eliminar_pais(paises):
    print("\n=== ELIMINAR PAÍS ===")
    nombre = input("Ingrese el nombre del país a eliminar: ")
    for i, pais in enumerate(paises):
        if pais["nombre"].lower() == nombre.lower():
            confirmacion = validar_confirmacion(f"¿Está seguro que desea eliminar '{pais['nombre']}'? (s/n): ")
            if confirmacion == "s":
                del paises[i]
                guardar_csv(paises)   # ← debe estar acá
                print(f"País '{nombre}' eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("País no encontrado.")

def ordenar_paises(paises):
    print("\n=== ORDENAR PAÍSES ===")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    criterio = input("Seleccione criterio: ")

    if criterio == "1":
        ordenados = sorted(paises, key=lambda p: p["nombre"].lower())
        clave = "nombre"
    elif criterio == "2":
        ordenados = sorted(paises, key=lambda p: p["poblacion"])
        clave = "poblacion"
    elif criterio == "3":
        ordenados = sorted(paises, key=lambda p: p["superficie"])
        clave = "superficie"
    else:
        print("Criterio no válido.")
        return

    print(f"\n=== PAÍSES ORDENADOS POR {clave.upper()} ===")
    for pais in ordenados:
        print(
            f"Nombre: {pais['nombre']} | "
            f"Población: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} km² | "
            f"Continente: {pais['continente']}"
        )    

def estadisticas(paises):
    print("\n=== ESTADÍSTICAS ===")

    mas_poblado = max(paises, key=lambda p: p["poblacion"])
    menos_poblado = min(paises, key=lambda p: p["poblacion"])
    mayor_superficie = max(paises, key=lambda p: p["superficie"])
    menor_superficie = min(paises, key=lambda p: p["superficie"])
    poblacion_total = sum(p["poblacion"] for p in paises)
    superficie_total = sum(p["superficie"] for p in paises)
    promedio_poblacion = poblacion_total / len(paises)
    densidad_promedio = poblacion_total / superficie_total

    print(f"Total de países:       {len(paises)}")
    print(f"Población total:       {poblacion_total:,}")
    print(f"Superficie total:      {superficie_total:,.2f} km²")
    print(f"Promedio de población: {promedio_poblacion:,.0f} hab")
    print(f"Densidad promedio:     {densidad_promedio:.2f} hab/km²")
    print(f"País más poblado:      {mas_poblado['nombre']} ({mas_poblado['poblacion']:,} hab)")
    print(f"País menos poblado:    {menos_poblado['nombre']} ({menos_poblado['poblacion']:,} hab)")
    print(f"Mayor superficie:      {mayor_superficie['nombre']} ({mayor_superficie['superficie']:,.2f} km²)")
    print(f"Menor superficie:      {menor_superficie['nombre']} ({menor_superficie['superficie']:,.2f} km²)")
