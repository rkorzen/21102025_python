"""Testy jednostkowe dla modułu kalkulatora."""

import pytest

from kalkulator import OPERATIONS, add, div, get_data, mul, sub

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -10) == -11


def test_sub():
    assert sub(1, 2) == -1
    assert sub(0, 0) == 0
    assert sub(-1, 1) == -2
    assert sub(-1, -10) == 9

def test_mul():
    assert mul(1, 2) == 2
    assert mul(0, 0) == 0
    assert mul(-1, 1) == -1
    assert mul(-1, -10) == 10
    assert mul(1, 0) == 0


def test_div_by_zero_raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_div():
    assert div(1, 2) == 0.5
    assert div(0, 1) == 0
    assert div(-1, 1) == -1.0
    assert div(-1, -10) == 0.1



def test_get_data_valid(monkeypatch):
    inputs = iter(["+", "1", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    op, a, b = get_data()

    assert op == "+"
    assert a == 1
    assert b == 2


def test_get_data_invalid(monkeypatch):
    operators = {"^": add}
    inputs = iter(["+"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("kalkulator.OPERATIONS", operators)
    monkeypatch.setattr("kalkulator.operations", operators)

    with pytest.raises(ValueError, match="Podano niepoprawny operator"):
        get_data()


def test_operations_mapping():
    assert set(OPERATIONS.keys()) == {"+", "-", "*", "/"}
