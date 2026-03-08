"""Pruebas unitarias para la capa application."""

import pytest

from application.use_cases import AddNumbersUseCase


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-2, 5, 3),
])
def test_add_numbers_use_case(a: int, b: int, expected: int) -> None:
    """Verifica que AddNumbersUseCase.execute retorne el resultado correcto."""
    use_case = AddNumbersUseCase()
    assert use_case.execute(a, b) == expected
