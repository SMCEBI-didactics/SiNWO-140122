


class Vector():
    """

    Klasa Vector reprezentuje wektor trojwymiarowy

    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def add(self, x, y, z):
        """
        
        Metoda add zwieksza skladowe wektora o podane wartosci

        Args:
            x: wartosc typu liczbowego, pierwsza skladowa wektora
            y: wartosc typu liczbowego, druga skladowa wektora
            z: wartosc typu liczbowego, trzeci skladowa wektora

        Returs:
            None

        """
        self.x += x
        self.y += y
        self.z += z



