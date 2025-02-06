import math
import textwrap
import config

from components.base_hexagon import BaseHexagon
from components.roof_hexagon import RoofHexagon

from parts.base_edge_plank import BaseEdgePlank
from parts.base_corner_wedge import BaseCornerWedge
from parts.roof_edge_plank import RoofEdgePlank
from parts.wall_edge_plank import WallEdgePlank

class WallFace:
    def __init__(self, base_hexagon: BaseHexagon, roof_hexagon: RoofHexagon, wall_plank: WallEdgePlank):
        base_plank = [x for x in base_hexagon.parts if isinstance(x, BaseEdgePlank)][0]
        base_wedge = [x for x in base_hexagon.parts if isinstance(x, BaseCornerWedge)][0]
        roof_plank = [x for x in roof_hexagon.parts if isinstance(x, RoofEdgePlank)][0]

        self.__ref_base_hexagon = base_hexagon

        self.parts = [wall_plank]

        self.base_face_width = base_plank.length + (2 * base_wedge.thickness * math.sin(base_wedge.top_face_obtuse_angle - math.radians(90)))
        self.roof_face_width = roof_plank.length
        self.side_length = wall_plank.top_length

        # Perpendicular distance from the outer edge of the base plank to outer-most corner of wall edge plank
        self.base_edge_offset_length = ((base_wedge.large_side_face_width - base_wedge.small_side_face_width) / 2) * math.cos(base_wedge.top_face_acute_angle)

        # Distance horizontally and vertically between the outer top edges of the base plank and the roof plank
        self.horizontal_length = ((base_hexagon.face_to_face_outer_length - (2 * self.base_edge_offset_length)) / 2) - (roof_hexagon.face_to_face_outer_length / 2)
        self.vertical_length = wall_plank.vertical_length

        # The incline angle of the face from the ground up
        self.slope = math.atan(self.vertical_length / self.horizontal_length)

        # Straight perpendicular distance between the outer top edges of the base plank and the roof plank
        self.face_length = self.vertical_length / math.sin(self.slope)

        # The corner angles on the base side of the face
        self.face_acute_angle = math.asin(self.face_length / self.side_length)

        # The corner angles on the roof side of the face
        self.face_obtuse_angle = math.radians(180 - math.degrees(self.face_acute_angle))

    def __str__(self):
        return textwrap.dedent(
            """
            [WALL FACE]
            Parts:
            - Wall Edge Planks: {wall_edge_plank_count}
            Dimensions:
            - Roof Edge Length = {roof_width}mm
            - Base Edge Length = {base_width}mm
            - Side Edge Length = {side_length}mm
            - Face Length = {face_length}mm
            Angles:
            - Incline Angle = {slope}º
            - Face Corner Angles (on roof side) = {roof_angle}º
            - Face Corner Angles (on base side) = {base_angle}º
            """
            .format(
                wall_edge_plank_count=len([x for x in self.parts if isinstance(x, WallEdgePlank)]),
                roof_width=round(self.roof_face_width, config.PRECISION),
                base_width=round(self.base_face_width, config.PRECISION),
                side_length=round(self.side_length, config.PRECISION),
                face_length=round(self.face_length, config.PRECISION),
                slope=round(math.degrees(self.slope), config.PRECISION),
                roof_angle=round(math.degrees(self.face_obtuse_angle), config.PRECISION),
                base_angle=round(math.degrees(self.face_acute_angle), config.PRECISION)
            )
        )
    
    # Width of the face between wall edge planks at the specified perpendicular distance along the face from the base
    def width_at_length_from_base(self, length: int):
        if length > self.face_length:
            raise ValueError(
                "Requested length from base ({requested_length}mm) is longer than the length of the face ({face_length}mm)"
                    .format(
                        requested_length=round(length, config.PRECISION),
                        face_length=round(self.face_length, config.PRECISION)
                    )
            )
        elif length < 0:
            raise ValueError(
                "Requested length from base ({requested_length}mm) is negative, but should be positive"
                    .format(
                        requested_length=round(length, config.PRECISION)
                    )
            )
        length_from_roof = self.face_length - length
        face_width = self.roof_face_width + (2 * length_from_roof / math.tan(self.face_acute_angle))
        return face_width
    
    # Vertical offset of the face from the top of the base plank at the specified distance along the face from the base
    def vertical_offset_at_length_from_base(self, length: int):
        if length > self.face_length:
            raise ValueError(
                "Requested length from base ({requested_length}mm) is longer than the length of the face ({face_length}mm)"
                    .format(
                        requested_length=round(length, config.PRECISION),
                        face_length=round(self.face_length, config.PRECISION)
                    )
            )
        elif length < 0:
            raise ValueError(
                "Requested length from base ({requested_length}mm) is negative, but should be positive"
                    .format(
                        requested_length=round(length, config.PRECISION)
                    )
            )
        length_from_roof = self.face_length - length
        vertical_length_from_roof = length_from_roof * math.sin(self.slope)
        vertical_length_from_base = self.vertical_length - vertical_length_from_roof
        return vertical_length_from_base
        
    def horizontal_offset_at_length_from_base(self, length: int):
        vertical_offset = self.vertical_offset_at_length_from_base(length)
        return vertical_offset / math.tan(self.slope)
