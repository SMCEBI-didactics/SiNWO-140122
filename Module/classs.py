


class Vector():
    """ Klasa zawierające współrzędne wektora.

        Attributes:
	    x (float): Współrzędna X
            y (float): Współrzędna Y
            z (float): Współrzędna Z

        Returns:
            None
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def add(self, x, y, z):
        """ Funkcja dodająca wartości wektora.

            Parameters:
                    x (float): liczba, którą chcemy dodać do współrzędnej X.
                    y (float): liczba, którą chcemy dodać do współrzędnej Y.
                    z (float): liczba, którą chcemy dodać do współrzędnej Z.

            Returns:
                    None
        """
        self.x += x
        self.y += y
        self.z += z



