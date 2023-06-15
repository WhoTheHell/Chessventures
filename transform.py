class Transform():

    raster_size = (0,0)
    static_offset = (0,0)

    @classmethod
    def coord_to_pix(cls, col, row, center_offset):
        x = (col + 0.5) * cls.raster_size[0] + cls.static_offset[0] - center_offset[0]
        y = (row + 0.5) * cls.raster_size[1] + cls.static_offset[1] - center_offset[1]
        return (x, y)

    @classmethod
    def initialize(cls, _raster_size, _static_offset):
        cls.raster_size = _raster_size
        cls.static_offset = _static_offset