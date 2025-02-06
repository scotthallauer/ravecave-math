import textwrap
import config

from materials.large_plank import LargePlankDefinition

class RoofEdgePlank:
    def __init__(self, large_plank: LargePlankDefinition, length: int):
        self.length = large_plank.request_length(length)
        self.width = large_plank.width
        self.thickness = large_plank.thickness

    def __str__(self):
        return textwrap.dedent(
            """
            [ROOF EDGE PLANK]
            Dimensions:
            - Length = {length}mm
            - Width = {width}mm
            - Thickness = {thickness}mm
            """
            .format(
                length=round(self.length, config.PRECISION), 
                width=round(self.width, config.PRECISION), 
                thickness=round(self.thickness, config.PRECISION)
            )
        )