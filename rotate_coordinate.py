from math import pi, cos, tan, sin, atan, sqrt


class CoordinateRotate:
    ang = 0
    def __init__(self, ang):
        self.ang = ang

    def transform(self, p):
        radian = pi/2 if p['y'] == 0 else atan(p['x'] / p['y'])
        
        transformed_radian = radian + self.ang / 180 * pi
        point = {
            'x': sqrt(p['x']*p['x'] + p['y']*p['y']) * sin(transformed_radian),
            'y': sqrt(p['x']*p['x'] + p['y']*p['y']) * cos(transformed_radian)
        }

        return point
