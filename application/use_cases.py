"""Casos de uso: orquestan la lógica del dominio."""

from domain.operations import add


class AddNumbersUseCase:
    """Caso de uso: sumar dos números enteros."""

    def execute(self, a: int, b: int) -> int:
        """Ejecuta la suma delegando al dominio."""
        return add(a, b)
