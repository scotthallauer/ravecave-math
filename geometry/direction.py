import math

from geometry.coordinate import ORIGIN
from geometry.coordinate import Coordinate

class Direction:
    def __init__(self, a: Coordinate, b: Coordinate):
        length = a.distance(b)
        x = (b.x - a.x) / length
        y = (b.y - a.y) / length
        z = (b.z - a.z) / length
        self.vector = Coordinate(x, y, z)

    def reverse(self):
        return Direction(self.vector, ORIGIN)
    
    def translate(self, coordinate: Coordinate, distance: float):
        return Coordinate(
            coordinate.x + distance * self.vector.x,
            coordinate.y + distance * self.vector.y,
            coordinate.z + distance * self.vector.z
        )

POS_X = Direction(ORIGIN, Coordinate(1, 0, 0))
NEG_X = Direction(ORIGIN, Coordinate(-1, 0, 0))
POS_Y = Direction(ORIGIN, Coordinate(0, 1, 0))
NEG_Y = Direction(ORIGIN, Coordinate(0, -1, 0))
POS_Z = Direction(ORIGIN, Coordinate(0, 0, 1))
NEG_Z = Direction(ORIGIN, Coordinate(0, 0, -1))