# Gestión de Países

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
| 6      | Filtrar países por continente |
| 7      | Ordenar países  |
| 8      | Eliminar pais   |
| 9      | Ver estadísticas |
| 10     | Salir |

---

## Estructura del CSV

El archivo `data/paises.csv` contiene los siguientes campos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | string | Nombre del país |
| `poblacion` | entero | Cantidad de habitantes |
| `superficie` | decimal | Superficie en km² |
| `continente` | string | Continente al que pertenece |

---

## Cómo ejecutar

1. Asegurarse de tener **Python 3.10+** instalado.
2. Desde la raíz del proyecto, ejecutar:

```bash
python src/main.py
```

3. Seguir las instrucciones del menú interactivo.

---

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
|              | IsabellaYH  |

---

## Licencia

Proyecto académico — Programación I 