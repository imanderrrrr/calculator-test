"""Pruebas unitarias para la capa domain."""

import pytest

from domain.operations import add


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-2, 5, 3),
])
def test_add(a: int, b: int, expected: int) -> None:
    """Verifica que add retorne el resultado correcto."""
    assert add(a, b) == expected
