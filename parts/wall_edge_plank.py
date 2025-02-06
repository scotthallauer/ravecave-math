import math
import textwrap
import config

from materials.large_plank import LargePlankDefinition

from parts.base_corner_wedge import BaseCornerWedge

from components.base_hexagon import BaseHexagon
from components.roof_hexagon import RoofHexagon

# The planks that join the vertices of the base hexagon to the vertices of the roof hexagon
class WallEdgePlank:
    def __init__(self, large_plank: LargePlankDefinition, base_hexagon: BaseHexagon, roof_hexagon: RoofHexagon, slope: float):
        base_wedge = [x for x in base_hexagon.parts if isinstance(x, BaseCornerWedge)][0]

        # See [Diagram A] for all the labelled points and edges below.
        BQ = (base_hexagon.vertex_to_vertex_outer_length / 2) - (roof_hexagon.vertex_to_vertex_outer_length / 2)
        GQ = BQ * math.tan(slope)
        BG = BQ / math.cos(slope)
        BO = base_wedge.thickness
        BC = BO * math.cos(slope)
        CO = BO * math.sin(slope)
        MO = large_plank.width - CO
        LO = MO / math.sin(slope)
        LN = LO / math.cos(slope)
        LM = LO * math.cos(slope)
        MN = LN - LM
        NO = LN * math.sin(slope)
        AB = MN - BC
        CD = CO * math.tan(slope)
        GP = large_plank.width
        FG = GP * math.sin(slope)
        EG = GP / math.sin(slope)
        EF = EG - FG
        FP = GP * math.cos(slope)
        JP = large_plank.width - FP
        IJ = JP / math.tan(slope)
        IP = JP / math.sin(slope)
        HI = FG - IJ
        JK = JP * math.tan(slope)
        DE = BG - (BC + CD + EF + FG)
        KL = (AB + BC + CD + DE + EF + FG) - (HI + IJ + JK + LM + MN)
        self.geometry = {
            "AB": AB,
            "AN": large_plank.width,
            "BC": BC,
            "BO": BO,
            "CD": CD,
            "CO": CO,
            "DE": DE,
            "EF": EF,
            "FG": FG,
            "FP": FP,
            "GH": large_plank.width,
            "GP": GP,
            "HI": HI,
            "IJ": IJ,
            "IP": IP,
            "JK": JK,
            "JP": JP,
            "KL": KL,
            "LM": LM,
            "MN": MN,
            "MO": MO,
            "NO": NO
        }

        # Distance horizontally and vertically between the top outer edges of the base corner wedge and the roof corner wedge
        self.horizontal_length = BQ
        self.vertical_length = GQ

        # Length of the top and bottom sides of the plank
        self.top_length = BG
        self.bottom_length = IJ + JK + KL + LM + MN

        self.width = large_plank.width
        self.thickness = large_plank.thickness

        # Base end of the plank
        self.base_cut_horizontal_length = BO
        self.base_cut_vertical_length = NO

        # Roof end of the plank
        self.roof_cut_horizontal_length = IP
        self.roof_cut_vertical_length = GP

        # Length of the minimum full plank that this cut plank is contained in
        self.bounding_length = large_plank.request_length(AB + BG)
        
        # Acute incline angle (in radians) of the edge planks from the ground up
        self.slope = slope

    def __str__(self):
        return textwrap.dedent(
            """
            [WALL EDGE PLANK]
            Dimensions:
            - Top Length (BG) = {top_length}mm
            - Bottom Length (IN) = {bottom_length}mm
            - Bounding Length (AG) = {bounding_length}mm
            - Width (AN) = {width}mm
            - Thickness = {thickness}mm
            - Base Top Cut Length (BO) = {base_top_cut_length}mm
            - Base Bottom Cut Length (NO) = {base_bottom_cut_length}mm
            - Roof Top Cut Length (GP) = {roof_top_cut_length}mm
            - Roof Bottom Cut Length (IP) = {roof_bottom_cut_length}mm
            Angles:
            - Incline Angle = {slope}º
            - Base Top Cut Angle = {slope}º
            - Base Bottom Cut Angle = {base_bottom_cut_angle}º
            - Roof Top Cut Angle = {base_bottom_cut_angle}º
            - Roof Bottom Cut Angle = {slope}º
            Cutting Measurements:
            - AB = {ab}mm
            - BC = {bc}mm
            - CD = {cd}mm
            - EF = {ef}mm
            - FG = {fg}mm
            - HI = {hi}mm
            - IJ = {ij}mm
            - JK = {jk}mm
            - LM = {lm}mm
            - MN = {mn}mm
            """
            .format(
                top_length=round(self.top_length, config.PRECISION), 
                bottom_length=round(self.bottom_length, config.PRECISION), 
                bounding_length=round(self.bounding_length, config.PRECISION), 
                width=round(self.width, config.PRECISION), 
                thickness=round(self.thickness, config.PRECISION),
                base_top_cut_length=round(self.base_cut_horizontal_length, config.PRECISION),
                base_bottom_cut_length=round(self.base_cut_vertical_length, config.PRECISION),
                roof_top_cut_length=round(self.roof_cut_vertical_length, config.PRECISION),
                roof_bottom_cut_length=round(self.roof_cut_horizontal_length, config.PRECISION),
                slope=round(math.degrees(self.slope), config.PRECISION),
                base_bottom_cut_angle=round(90 - math.degrees(self.slope), config.PRECISION),
                ab=round(self.geometry["AB"], config.PRECISION),
                bc=round(self.geometry["BC"], config.PRECISION),
                cd=round(self.geometry["CD"], config.PRECISION),
                ef=round(self.geometry["EF"], config.PRECISION),
                fg=round(self.geometry["FG"], config.PRECISION),
                hi=round(self.geometry["HI"], config.PRECISION),
                ij=round(self.geometry["IJ"], config.PRECISION),
                jk=round(self.geometry["JK"], config.PRECISION),
                lm=round(self.geometry["LM"], config.PRECISION),
                mn=round(self.geometry["MN"], config.PRECISION)
            )
        )