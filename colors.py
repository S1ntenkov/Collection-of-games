class Colors:
    blue = (0, 0, 205)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    orange = (255, 165, 0)
    pink = (255, 0, 255)
    violet = (148, 0, 211)
    aqua = (0, 255, 255)
    aquamarine = (127, 255, 212)

    @classmethod
    def get_colors(cls):
        return [cls.blue, cls.red, cls.lime, cls.orange, cls.pink, cls.violet, cls.aqua, cls.aquamarine]
        