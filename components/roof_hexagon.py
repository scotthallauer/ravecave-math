import math
import textwrap
import config

from parts.roof_edge_plank import RoofEdgePlank
from parts.roof_corner_wedge import RoofCornerWedge

class RoofHexagon:
    def __init__(self, roof_plank: RoofEdgePlank, roof_wedge: RoofCornerWedge):
        self.parts = [roof_plank] * 6 + [roof_wedge] * 6

        self.width = roof_plank.width

        self.vertex_to_vertex_inner_length = roof_plank.length + (2 * 600 * math.sin(math.radians(30)))
        self.vertex_to_vertex_outer_length = self.vertex_to_vertex_inner_length + (2 * roof_wedge.thickness)
        self.face_to_face_inner_length = 2 * roof_plank.length * math.sin(math.radians(60))
        self.face_to_face_outer_length = self.face_to_face_inner_length + (2 * roof_plank.thickness)

        # The inside angle between adjacent base planks in the hexagon
        self.inner_angle = math.radians(120)

    def __str__(self):
        return textwrap.dedent(
            """
            [ROOF HEXAGON]
            Parts:
            - Roof Edge Planks: {roof_plank_count}
            - Roof Corner Wedges: {roof_wedge_count}
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
                roof_plank_count=len([x for x in self.parts if isinstance(x, RoofEdgePlank)]),
                roof_wedge_count=len([x for x in self.parts if isinstance(x, RoofCornerWedge)]),
                width=round(self.width, config.PRECISION),
                inner_vertex_length=round(self.vertex_to_vertex_inner_length, config.PRECISION),
                inner_face_length=round(self.face_to_face_inner_length, config.PRECISION),
                outer_vertex_length=round(self.vertex_to_vertex_outer_length, config.PRECISION),
                outer_face_length=round(self.face_to_face_outer_length, config.PRECISION),
                inner_angle=round(math.degrees(self.inner_angle), config.PRECISION)
            )
        )