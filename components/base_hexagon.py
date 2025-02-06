import math
import textwrap
import config

from parts.base_edge_plank import BaseEdgePlank
from parts.base_corner_wedge import BaseCornerWedge

class BaseHexagon:
    def __init__(self, base_plank: BaseEdgePlank, base_wedge: BaseCornerWedge):
        self.parts = [base_plank] * 6 + [base_wedge] * 6

        self.width = base_plank.width

        self.vertex_to_vertex_inner_length = base_plank.length + (2 * ((base_wedge.small_side_face_width * math.cos(math.radians(30))) + (base_plank.length * math.sin(math.radians(30)))))
        self.vertex_to_vertex_outer_length = self.vertex_to_vertex_inner_length + (2 * base_wedge.thickness)
        self.face_to_face_inner_length = base_wedge.small_side_face_width + (2 * (base_plank.length * math.sin(math.radians(60)))) + (2 * (base_wedge.small_side_face_width * math.cos(math.radians(60))))
        self.face_to_face_outer_length = self.face_to_face_inner_length + (2 * base_plank.thickness)

        # The inside angle between adjacent base planks in the hexagon
        self.inner_angle = math.radians(120)

    def __str__(self):
        return textwrap.dedent(
            """
            [BASE HEXAGON]
            Parts:
            - Base Edge Planks: {base_plank_count}
            - Base Corner Wedges: {base_wedge_count}
            Dimensions:
            - Width = {width}mm
            - Inner Length (between opposite vertices) = {inner_vertex_length}mm
            - Inner Length (between opposite faces) = {inner_face_length}mm
            - Outer Length (between opposite vertices) = {outer_vertex_length}mm
            - Outer Length (between opposite faces) = {outer_face_length}mm
            Angles:
            - Inner Angles = {inner_angle}º
            """
            .format(
                base_plank_count=len([x for x in self.parts if isinstance(x, BaseEdgePlank)]),
                base_wedge_count=len([x for x in self.parts if isinstance(x, BaseCornerWedge)]),
                width=round(self.width, config.PRECISION),
                inner_vertex_length=round(self.vertex_to_vertex_inner_length, config.PRECISION),
                inner_face_length=round(self.face_to_face_inner_length, config.PRECISION),
                outer_vertex_length=round(self.vertex_to_vertex_outer_length, config.PRECISION),
                outer_face_length=round(self.face_to_face_outer_length, config.PRECISION),
                inner_angle=round(math.degrees(self.inner_angle), config.PRECISION)
            )
        )