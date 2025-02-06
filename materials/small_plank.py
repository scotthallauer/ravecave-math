import config

class SmallPlankDefinition:
    def __init__(self, width: int, thickness: int, max_length: int):
        self.width = width
        self.thickness = thickness
        self.max_length = max_length

    # Returns the desired plank length if possible, otherwise raises an error
    def request_length(self, length: float):
        if length > self.max_length:
            raise ValueError(
                "Requested plank length ({requested_length}mm) is longer than the plank definition allows (max of {max_length}mm)"
                    .format(
                        requested_length=round(length, config.PRECISION), 
                        max_length=round(self.max_length, config.PRECISION)
                    )
            )
        elif length < 0:
            raise ValueError(
                "Requested plank length ({requested_length}mm) is negative, but should be positive"
                    .format(
                        requested_length=round(length, config.PRECISION)
                    )
            )
        else:
            return length