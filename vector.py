"""Represent an N-dmensional vecotr."""

import math
import functools


class Vector(object):
    """Represent an N-dimensional vector."""

    def __init__(self, coordinates):
        """Initialize coordinates of length N as an N-vector."""
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
        """Represent vector as string."""
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        """Determine if two vectors are equal."""
        return self.coordinates == v.coordinates

    def __add__(self, x):
        """Add two vectors."""
        self._validate_dimension(x)
        return map(lambda a, b: a + b, self.coordinates, x.coordinates)

    def __sub__(self, x):
        """Subtract two vectors."""
        self._validate_dimension(x)
        return map(lambda a, b: a - b, self.coordinates, x.coordinates)

    def __mul__(self, scalar_int):
        """Multiply a vector by a scalar."""
        return map(lambda a: a * scalar_int, self.coordinates)

    def _validate_dimension(self, x):
        """Check that another vector has the same dimensions as this."""
        if x.dimension != self.dimension:
            raise ValueError('The vectors must have equal dimensinos')

    def magnitude(self):
        """Calculate the length of a vector."""
        return math.sqrt(functools.reduce(
            lambda sumSquared, coordinate: sumSquared + coordinate ** 2,
            self.coordinates, 0))

    def normalized(self):
        """Give slope of normalized vector."""
        try:
            return self * (1.0 / self.magnitude())

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
