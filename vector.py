import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, x):
        self._validate_dimension(x)
        return map(lambda a, b: a+b, self.coordinates, x.coordinates)

    def __sub__(self, x):
        self._validate_dimension(x)
        return map(lambda a, b: a-b, self.coordinates, x.coordinates)

    def __mul__(self, scalarInt):
        return map(lambda a: a * scalarInt, self.coordinates)

    def _validate_dimension(self, x):
        if x.dimension != self.dimension:
            raise ValueError('The vectors must have equal dimensinos')

    def magnitude(self):
        return math.sqrt(reduce(
            lambda sumSquared, coordinate: sumSquared + coordinate ** 2,
            self.coordinates, 0))

    def normalized(self):
        try:
            return self * (1.0 / self.magnitude())

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
        

