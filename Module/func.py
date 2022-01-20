from time import time as t

def f(x):
    """ Funkcja obliczająca x^2 + x+3.

	Parameters:
		x (float): Liczba, na której chcemy wykonać działanie.

	Returns:
		(float) Wynik działania
    """
    return x**2 + x + 3

def time():
    """ Funkcja zwracająca czas.

	Parameters:
		None

	Returns:
		(float) Czas.
    """
    return t()
