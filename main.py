import math

from materials.large_plank import LargePlankDefinition
from materials.small_plank import SmallPlankDefinition

from parts.base_edge_plank import BaseEdgePlank
from parts.base_corner_wedge import BaseCornerWedge
from parts.roof_edge_plank import RoofEdgePlank
from parts.roof_corner_wedge import RoofCornerWedge
from parts.wall_edge_plank import WallEdgePlank
from parts.wall_horizontal_brace_plank import WallHorizontalBracePlank

from components.base_hexagon import BaseHexagon
from components.roof_hexagon import RoofHexagon
from components.wall_face import WallFace

def main():
    large_plank = LargePlankDefinition(width=152, thickness=50, max_length=6000)
    small_plank = SmallPlankDefinition(width=76, thickness=25, max_length=6000)

    base_plank = BaseEdgePlank(large_plank, length=3500)
    base_wedge = BaseCornerWedge(large_plank)
    base_hexagon = BaseHexagon(base_plank, base_wedge)

    roof_plank = RoofEdgePlank(large_plank, length=600)
    roof_wedge = RoofCornerWedge(large_plank)
    roof_hexagon = RoofHexagon(roof_plank, roof_wedge)

    wall_plank = WallEdgePlank(large_plank, base_hexagon, roof_hexagon, slope=math.radians(56))
    wall_face = WallFace(base_hexagon, roof_hexagon, wall_plank)

    horizontal_brace_plack = WallHorizontalBracePlank(small_plank, wall_face, base_hexagon, wall_face.face_length / 2)

    print(base_plank)
    print(base_wedge)
    print(base_hexagon)
    print(roof_plank)
    print(roof_wedge)
    print(roof_hexagon)
    print(wall_plank)
    print(wall_face)


if __name__=="__main__":
    main()