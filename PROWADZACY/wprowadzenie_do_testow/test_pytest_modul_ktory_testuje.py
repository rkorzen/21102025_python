# zeby to dzialalo to trzeba zrobic pip install pytest

from modul_ktory_testuje import funkcja


def test_testowana_funkcja_dla_wartosci_ujemnych():
    result = funkcja(-1)
    expected = 0
    assert result == expected


def test_testowana_funkcja_dla_wartosci_0():
    result = funkcja(0)
    expected = 0
    assert result == expected


def test_testowana_funkcja_dla_wartosci_dodatniej():
    result = funkcja(1)
    expected = 1
    assert result == expected