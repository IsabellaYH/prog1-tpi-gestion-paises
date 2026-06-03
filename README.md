########## GESTIÓN DE PAISES ############

Trabajo Práctico Integrador (TPI) — Programación 1  
Aplicación de consola en Python para gestionar información de países mediante un archivo CSV.

---

## Estructura del proyecto

```
prog1-tpi-gestion-paises/
├── data/
│   └── paises.csv          # Base de datos de países
└── src/
    ├── main.py             # Menú principal y punto de entrada
    ├── paises.py           # Lógica de agregar, actualizar y eliminar países
    ├── archivo.py          # Operaciones sobre el archivo CSV
    └── validaciones.py     # Módulo de validaciones de entrada del usuario
```

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1      | Cargar datos desde el archivo CSV |
| 2      | Mostrar todos los países cargados |
| 3      | Agregar un nuevo país |
| 4      | Actualizar los datos de un país existente |
| 5      | Buscar un país por nombre |
| 6      | Filtrar países por continente, superficie o población |
| 7      | Ordenar países  |
| 8      | Estadísticas   |
| 9      | Eliminar país |
| 10     | Salir |

---

## Estructura del CSV

El archivo `data/paises.csv` contiene los siguientes campos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | string | Nombre del país |
| `poblacion` | entero | Cantidad de habitantes |
| `superficie` | int | Superficie en km² |
| `continente` | string | Continente al que pertenece |

---

## Cómo ejecutar

Para utilizar la aplicación de consola **Gestión de Países**, sigue estas instrucciones basadas en la documentación del proyecto:

### 1. Requisitos Previos
Antes de iniciar, asegúrate de cumplir con lo siguiente:
*   Tener instalado **Python 3.10** o una versión superior.
*   Contar con el archivo de datos `data/paises.csv` en la ubicación correcta, el cual debe contener los campos: nombre, población, superficie y continente.

### 2. Cómo Ejecutar la Aplicación
1.  Abre una terminal o consola de comandos.
2.  Dirígete a la **raíz del proyecto**.
3.  Ejecuta el programa principal con el comando: `python main.py`.

### 3. Uso del Menú Interactivo
Una vez iniciada la aplicación, verás un menú con 10 opciones. Para seleccionar una, escribe el número correspondiente y presiona *Enter*:

*   **Cargar y Visualizar:**
    *   **Opción 1:** Carga los datos existentes desde el archivo CSV a la memoria del programa.
    *   **Opción 2:** Muestra una lista de todos los países que se han cargado actualmente.
*   **Gestión de Información:**
    *   **Opción 3 (Agregar):** Permite introducir un nuevo país. El sistema validará que el nombre no esté duplicado y que los campos no estén vacíos.
    *   **Opción 4 (Actualizar):** Permite modificar los datos de un país que ya existe en la lista.
    *   **Opción 8 (Eliminar):** Borra un país de la lista. El sistema te pedirá una **confirmación** antes de realizar la eliminación definitiva.
*   **Búsqueda y Filtros:**
    *   **Opción 5:** Busca un país específico por su nombre.
    *   **Opción 6:** Filtra y muestra países pertenecientes a un continente específico ingresado por el usuario.
    *   **Opción 7:** Ordena la lista de países según los criterios del programa.
*   **Análisis y Cierre:**
    *   **Opción 9:** Muestra estadísticas generales de los datos cargados.
    *   **Opción 10:** Finaliza la ejecución de la aplicación.

### 4. Reglas de Ingreso de Datos (Validaciones)
Al agregar o editar países, ten en cuenta las siguientes reglas implementadas para mantener la integridad de los datos:
*   **Campos obligatorios:** El nombre y el continente no pueden quedar vacíos.
*   **Población:** Debe ser un número entero mayor a 0.
*   **Superficie:** Debe ser un número decimal o entero mayor a 0.
*   **Duplicados:** El sistema no permitirá ingresar un país que ya exista en el registro.


## Módulos

### `main.py`
Punto de entrada del programa. Contiene el menú principal y el bucle de control que dirige al usuario entre las distintas opciones.


### `archivo.py`
Maneja todas las operaciones de lectura y escritura sobre `paises.csv`:
- `cargar_csv()` — Lee el archivo y retorna una lista de diccionarios.
- `guardar_csv(paises)` — Sobreescribe el archivo con la lista actualizada.
- `buscar_pais(nombre)` — Busca un país por nombre y muestra sus detalles.
- `filtrar_paises(paises)` — Filtra países según el continente ingresado por el usuario.

### `paises.py`
Contiene la lógica de modificación de datos:
- `agregar_pais(paises)` — Solicita los datos de un nuevo país y lo guarda.
- `actualizar_pais(paises)` — Permite editar campos de un país existente.
- `eliminar_pais(paises)` — Elimina un país con confirmación del usuario.

##  Validaciones implementadas

- Nombre y continente no pueden estar vacíos
- Población debe ser un número entero mayor a 0
- Superficie debe ser un número mayor a 0
- No se pueden agregar países duplicados
- Confirmación antes de eliminar un país

##  Autores

|    Nombre    |   GitHub    |
|  Nuñez Lucia | lunu-gibhub |
| Yanes Leanny | IsabellaYH  |

---

## Licencia

Proyecto académico — Programación I 
