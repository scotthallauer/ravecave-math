import config
import textwrap

from geometry.coordinate import Coordinate
from geometry.direction import Direction

class FiniteLine:
    def __init__(self, a: Coordinate, b: Coordinate):
        self.name = "{a_name}-{b_name}".format(a_name=a.name, b_name=b.name)
        self.a = a
        self.b = b
        self.length = a.distance(b)

    def __str__(self):
        return textwrap.dedent(
            """
            [FINITE LINE: {name}]
            Coordinate {a_name}:
            - X = {a_x}
            - Y = {a_y}
            - Z = {a_z}
            Coordinate {b_name}:
            - X = {b_x}
            - Y = {b_y}
            - Z = {b_z}
            Properties:
            - Length: {length}mm
            """
            .format(
                name=self.name,
                a_name=self.a.name,
                a_x=round(self.a.x, config.PRECISION), 
                a_y=round(self.a.y, config.PRECISION), 
                a_z=round(self.a.z, config.PRECISION),
                b_name=self.b.name,
                b_x=round(self.b.x, config.PRECISION), 
                b_y=round(self.b.y, config.PRECISION), 
                b_z=round(self.b.z, config.PRECISION),
                length=round(self.length, config.PRECISION)
            )
        )

    def point_from_a(self, length: float, name: str = "_"):
        if length > self.length:
            raise ValueError(
                "Requested length from coordinate {a_name} ({requested_length}mm) is longer than the length of the line between coordinates {a_name} and {b_name} ({line_length}mm)"
                    .format(
                        a_name=self.a.name,
                        b_name=self.b.name,
                        requested_length=round(length, config.PRECISION), 
                        line_length=round(self.length, config.PRECISION)
                    )
            )
        elif length < 0:
            raise ValueError(
                "Requested length from coordinate {a_name} ({requested_length}mm) is negative, but should be positive"
                    .format(
                        a_name=self.a.name,
                        requested_length=round(length, config.PRECISION)
                    )
            )
        length_ratio = length / self.length
        x = self.a.x + length_ratio * (self.b.x - self.a.x)
        y = self.a.y + length_ratio * (self.b.y - self.a.y)
        z = self.a.z + length_ratio * (self.b.z - self.a.z)
        return Coordinate(x, y, z, name)
    
    def point_from_b(self, length: float, name: str = "_"):
        if length > self.length:
            raise ValueError(
                "Requested length from coordinate {b_name} ({requested_length}mm) is longer than the length of the line between coordinates {b_name} and {a_name} ({line_length}mm)"
                    .format(
                        a_name=self.a.name,
                        b_name=self.b.name,
                        requested_length=round(length, config.PRECISION), 
                        line_length=round(self.length, config.PRECISION)
                    )
            )
        elif length < 0:
            raise ValueError(
                "Requested length from coordinate {b_name} ({requested_length}mm) is negative, but should be positive"
                    .format(
                        b_name=self.b.name,
                        requested_length=round(length, config.PRECISION)
                    )
            )
        length_ratio = length / self.length
        x = self.b.x + length_ratio * (self.a.x - self.b.x)
        y = self.b.y + length_ratio * (self.a.y - self.b.y)
        z = self.b.z + length_ratio * (self.a.z - self.b.z)
        return Coordinate(x, y, z, name)
    
class InfiniteLine:
    def __init__(self, origin: Coordinate, direction: Direction):
        self.origin = origin
        self.direction = direction