"""Entrypoint CLI. Valida inputs y delega al caso de uso."""

import sys

from application.use_cases import AddNumbersUseCase


def _parse_int(value: str, name: str) -> int:
    """Convierte un string a entero; termina con error si no es posible."""
    try:
        return int(value)
    except ValueError:
        print(f"Error: '{value}' no es un entero válido para '{name}'.")
        sys.exit(1)


def main() -> None:
    """Punto de entrada principal del CLI."""
    if len(sys.argv) != 3:
        print("Uso: python -m infrastructure.cli <a> <b>")
        sys.exit(1)

    a = _parse_int(sys.argv[1], "a")
    b = _parse_int(sys.argv[2], "b")

    result = AddNumbersUseCase().execute(a, b)
    print(f"{a} + {b} = {result}")


if __name__ == "__main__":
    main()
