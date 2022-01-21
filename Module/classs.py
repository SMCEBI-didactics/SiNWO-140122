class Vector():
    """
    Klasa pelniaca role wektora z 3 skladowymi
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def add(self, x, y, z):
        """
        Funkcja ktora dodaje wektory
        """
        self.x += x
        self.y += y
        self.z += z



