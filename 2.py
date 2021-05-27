class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def itog(self):
        return f"{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5) / 1000} т"

doroga = Road(3000, 10)
print(doroga.itog())