import math
import textwrap
import config

from materials.large_plank import LargePlankDefinition

class RoofCornerWedge:
    def __init__(self, large_plank: LargePlankDefinition):
        self.top_face_angle = math.radians(60)

        self.side_face_width = large_plank.thickness
        self.side_face_length = large_plank.width

        # The height of the wedge if lying flat on its side face
        self.thickness = (self.side_face_width / 2) * math.tan(self.top_face_angle)

    def __str__(self):
        return textwrap.dedent(
            """
            [ROOF CORNER WEDGE]
            Dimensions:
            - Length = {length}mm
            - Face Widths = {face_width}mm
            - Thickness = {thickness}mm
            Angles:
            - Inner Angles (on top face) = {inner_angle}º
            """
            .format(
                length=round(self.side_face_length, config.PRECISION),
                face_width=round(self.side_face_width, config.PRECISION),
                thickness=round(self.thickness, config.PRECISION),
                inner_angle=round(math.degrees(self.top_face_angle), config.PRECISION)
            )
        )