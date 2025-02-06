import math

from geometry.coordinate import ORIGIN
from geometry.direction import POS_X
from geometry.direction import NEG_X
from geometry.direction import POS_Y
from geometry.direction import NEG_Y
from geometry.coordinate import Coordinate
from geometry.direction import Direction
from geometry.line import InfiniteLine
from geometry.plane import Plane

from materials.small_plank import SmallPlankDefinition

from components.wall_face import WallFace
from components.base_hexagon import BaseHexagon

from parts.base_edge_plank import BaseEdgePlank

class WallHorizontalBracePlank:
    # length_from_base is the distance from the centre of this plank along the wall face to the base hexagon
    def __init__(self, small_plank: SmallPlankDefinition, wall_face: WallFace, base_hexagon: BaseHexagon, length_from_base: float):
        self.width = small_plank.width
        self.thickness = small_plank.thickness

        # See [Diagram B] for all the labelled points, edges and angles below.
        # Assume the following:
        # - Origin = Centre of the face at base level
        # - X-Axis = Perpendicular line from origin to structure centre (positive towards centre)
        # - Y-Axis = Parallel line along base edge plank (positive towards A)
        # - Z-Axis = Directly up from ground (positive upwards)
        base_centre_on_face = ORIGIN
        plank_centre_on_face = Coordinate(wall_face.horizontal_offset_at_length_from_base(length_from_base), 0, wall_face.vertical_offset_at_length_from_base(length_from_base))
        A = POS_Y.translate(plank_centre_on_face, wall_face.width_at_length_from_base(length_from_base) / 2)
        FACE_PLANE = Plane(base_centre_on_face, plank_centre_on_face, A)
        plank_bottom_on_face = Coordinate(wall_face.horizontal_offset_at_length_from_base(length_from_base - (self.thickness / 2)), 0, wall_face.vertical_offset_at_length_from_base(length_from_base - (self.thickness / 2)))
        D = POS_Y.translate(plank_bottom_on_face, wall_face.width_at_length_from_base(length_from_base - (self.thickness / 2)) / 2)
        print("YO")
        print(D.z+152)
        FACE_UP_DIRECTION = Direction(base_centre_on_face, plank_centre_on_face)
        FACE_DOWN_DIRECTION = FACE_UP_DIRECTION.reverse()
        C = FACE_UP_DIRECTION.translate(D, self.thickness)
        base_outer_corner_on_face = POS_Y.translate(base_centre_on_face, wall_face.width_at_length_from_base(0) / 2)
        base_centre_on_outer_edge = NEG_X.translate(base_centre_on_face, wall_face.base_edge_offset_length)
        base_plank = [x for x in base_hexagon.parts if isinstance(x, BaseEdgePlank)][0]
        base_plank_outer_corner = POS_Y.translate(base_centre_on_outer_edge, base_plank.length / 2)
        base_plank_inner_corner = POS_X.translate(base_plank_outer_corner, base_plank.thickness)
        EDGE_PLANK_SIDE_PLANE = Plane(base_outer_corner_on_face, D, base_plank_inner_corner)
        FACE_NORMAL_IN_DIRECTION = FACE_PLANE.normal(D).direction
        FACE_NORMAL_OUT_DIRECTION = FACE_NORMAL_IN_DIRECTION.reverse()
        J = FACE_NORMAL_IN_DIRECTION.translate(D, self.width)
        K = EDGE_PLANK_SIDE_PLANE.intersection(InfiniteLine(J, NEG_Y))
        B = EDGE_PLANK_SIDE_PLANE.intersection(InfiniteLine(C, NEG_Y))
        I = FACE_NORMAL_IN_DIRECTION.translate(C, self.width)
        temp_plane = Plane(J, K, D)
        temp_i = temp_plane.normal(J).direction.translate(J, self.thickness)
        H = EDGE_PLANK_SIDE_PLANE.intersection(InfiniteLine(temp_i, NEG_Y))
        BC = B.distance(C)
        HI = H.distance(temp_i)
        JK = J.distance(K)
        FG = BC
        LM = JK
        NO = HI
        self.geometry = {
            "BC": BC,
            "FG": FG,
            "HI": HI,
            "JK": JK,
            "LM": LM,
            "NO": NO
        }

        self.bounding_length = wall_face.width_at_length_from_base(length_from_base - (self.thickness / 2))