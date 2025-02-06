from geometry.coordinate import Coordinate
from geometry.coordinate import ORIGIN
from geometry.direction import Direction
from geometry.line import InfiniteLine

class Plane:
    """Represents a 3D plane defined by three points."""
    def __init__(self, a: Coordinate, b: Coordinate, c: Coordinate):
        """
        Initializes the plane from three points.
        """
        self.__ref_a = a
        self.__ref_b = b
        self.__ref_c = c

        # Compute two direction vectors on the plane
        v1 = Coordinate(b.x - a.x, b.y - a.y, b.z - a.z)
        v2 = Coordinate(c.x - a.x, c.y - a.y, c.z - a.z)

        # Compute normal using the cross product
        self.A = v1.y * v2.z - v1.z * v2.y
        self.B = v1.z * v2.x - v1.x * v2.z
        self.C = v1.x * v2.y - v1.y * v2.x
        self.D = -(self.A * a.x + self.B * a.y + self.C * a.z)

    def intersection(self, line: InfiniteLine):
        """
        Finds the intersection point of the plane with a given line.
        
        :param line: A Line object.
        :return: A Coordinate object if an intersection exists, or None if the line is parallel.
        """
        x0, y0, z0 = line.origin.x, line.origin.y, line.origin.z
        dx, dy, dz = line.direction.vector.x, line.direction.vector.y, line.direction.vector.z

        denominator = self.A * dx + self.B * dy + self.C * dz

        if abs(denominator) < 1e-6:  # Line is parallel to the plane
            return None

        # Solve for t
        t = - (self.A * x0 + self.B * y0 + self.C * z0 + self.D) / denominator

        # Compute intersection point
        x = x0 + dx * t
        y = y0 + dy * t
        z = z0 + dz * t

        return Coordinate(x, y, z)
    
    def normal(self, coordinate: Coordinate):
        return InfiniteLine(coordinate, Direction(ORIGIN, Coordinate(self.A, self.B, self.C)))