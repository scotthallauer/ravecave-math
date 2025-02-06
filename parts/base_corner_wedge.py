import math
import textwrap
import config

from materials.large_plank import LargePlankDefinition

class BaseCornerWedge:
    def __init__(self, large_plank: LargePlankDefinition):
        # Inner angles when looking vertically downwards on the structure
        self.top_face_obtuse_angle = math.radians(120)
        # Outer angles when looking vertically downwards on the structure
        self.top_face_acute_angle = math.radians(60)

        # The three sides that connect with the base edge planks and wall edge planks
        self.small_side_face_width = large_plank.thickness
        # The outer face when looking vertically downwards on the structure, not connected to any planks
        self.large_side_face_width = large_plank.thickness + (2 * large_plank.thickness * math.cos(self.top_face_acute_angle))

        # The height of the wedge from the ground to the top
        self.side_face_length = large_plank.width

        # The height of the wedge if lying flat on its largest face
        self.thickness = large_plank.thickness * math.sin(self.top_face_acute_angle)

    def __str__(self):
        return textwrap.dedent(
            """
            [BASE CORNER WEDGE]
            Dimensions:
            - Length = {length}mm
            - Inner Face Widths = {inner_width}mm
            - Outer Face Width = {outer_width}mm
            - Thickness = {thickness}mm
            Angles:
            - Inner Angles (on top face) = {inner_angle}º
            - Outer Angles (on top face) = {outer_angle}º
            """
            .format(
                length=round(self.side_face_length, config.PRECISION),
                inner_width=round(self.small_side_face_width, config.PRECISION), 
                outer_width=round(self.large_side_face_width, config.PRECISION), 
                thickness=round(self.thickness, config.PRECISION),
                inner_angle=round(math.degrees(self.top_face_obtuse_angle), config.PRECISION),
                outer_angle=round(math.degrees(self.top_face_acute_angle), config.PRECISION)
            )
        )