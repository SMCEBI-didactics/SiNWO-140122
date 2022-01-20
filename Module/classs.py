


class Vector():
    """
    Klasa reprezentująca trójwymiarowy wektor.

    Notes:
        Początkowe wartości wymiarów wynoszą 0.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def add(self, x, y, z):
        """
        Metoda dodająca do składowych wektora podane wartości.

        Args:
            x (num): wymiar x,
            y (num): wymiar z,
            z (num): wymiar z,
        """
        self.x += x
        self.y += y
        self.z += z



