from __future__ import annotations

import math
import textwrap
import config

class Coordinate:
    def __init__(self, x: float, y: float, z: float, name: str = "_"):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return textwrap.dedent(
            """
            [COORDINATE: {name}]
            Position:
            - X = {x}
            - Y = {y}
            - Z = {z}
            Distance:
            - Origin: {distance}mm
            """
            .format(
                name=self.name,
                x=round(self.x, config.PRECISION), 
                y=round(self.y, config.PRECISION), 
                z=round(self.z, config.PRECISION),
                distance=round(self.distance(ORIGIN), config.PRECISION)
            )
        )

    def distance(self, other: Coordinate):
        return math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2))

ORIGIN = Coordinate(0, 0, 0, "origin")