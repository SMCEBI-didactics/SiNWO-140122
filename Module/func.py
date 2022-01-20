from time import time as t

def f(x):
    """
    Funkcja zwracająca dla danego x wartość x^2+x+3.

    Args:
        x (num): wymagana wartość zmiennej.

    Returns:
        num: wartość wielomianu dla podanej zmiennej.
    """
    return x**2 + x + 3

def time():
    """
    Funkcja zwracająca czas jako liczbę.

    Returns:
        float: czas w sekundach .
    """
    return t()
