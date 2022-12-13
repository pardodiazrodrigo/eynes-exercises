import math

class Circle():
    """
    >>> Circle(10).area()
    314.16
    >>> Circle(5).perimeter()
    31.42
    >>> print(Circle(20))
    Circle with radio 20, perimeter 125.66, area 1256.64.
    >>> Circle(5).radio = -1
    Radio can't be less than 0.
    >>> print(Circle(20) * 2)
    Circle with radio 40, perimeter 251.33, area 5026.55.
    >>> print(Circle(20) * -1)
    n can't by less than 0.
    None
    """

    PI = math.pi

    def __init__(self, radio):
        try:
            if radio <= 0:
                raise ValueError("Radio can't be less than 0.")
            else:
                self._radio = radio
        except ValueError as e:
            print(e)

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, r):
        if r <= 0:
            print("Radio can't be less than 0.")
        else:
            self._radio = r

    def area(self):
        return round(self.PI * self.radio**2, 2)

    def perimeter(self):
        return round(2 * self.PI * self.radio, 2)

    def __str__(self):
        return f"Circle with radio {self.radio}, perimeter {self.perimeter()}, area {self.area()}."

    def __mul__(self, n):
        if n <= 0:
            print("n can't by less than 0.")
        else:
            return Circle(self.radio * n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
