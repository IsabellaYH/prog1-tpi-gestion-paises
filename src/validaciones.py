def validar_texto(mensaje, campo="campo"):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print(f"Error: el {campo} no puede estar vacío.")


def validar_entero(mensaje, campo="campo"):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            return None  # permite dejar en blanco (para actualizar)
        try:
            numero = int(valor)
            if numero > 0:
                return numero
            print(f"Error: el {campo} debe ser mayor a 0.")
        except ValueError:
            print(f"Error: el {campo} debe ser un número entero.")


def validar_confirmacion(mensaje):
    while True:
        valor = input(mensaje).strip().lower()
        if valor in ("s", "n"):
            return valor
        print("Error: ingrese 's' para confirmar o 'n' para cancelar.")