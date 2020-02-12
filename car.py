from utility import getTransformedLength

class Car:
    def __init__(self, car_name):
        self.car_name = car_name
        self.lamp =  {
            'lat': 0,
            'lon': 0,
            'alt': 0,
            'hfr': 0
        }
        self.car_pos = {
            'hdtf': 0,
            'hdtb': 0,
            'hdtr': 0,
            'hdtl': 0,
            'fh': 0,
            'bh': 0,
            'rh': 0,
            'lh': 0,
            'dir': 0
        }
        self.shadow_pos = {
            'cf': 0,
            'cb': 0,
            'cr': 0,
            'cl': 0
        }

    def set_camera(self, camera):
        self.lamp['lat'] = camera['lat']
        self.lamp['lon'] = camera['lon']
        self.lamp['alt'] = camera['alt']
        self.lamp['hfr'] = camera['height']
    
    def get_camera(self):
        return self.lamp

    def set_car_pos(self, car_pos):
        self.car_pos['hdtf'] = car_pos['hor_dist_to_front']
        self.car_pos['hdtb'] = car_pos['hor_dist_to_rear']
        self.car_pos['hdtr'] = car_pos['hor_dist_to_right']
        self.car_pos['hdtl'] = car_pos['hor_dist_to_left']
        self.car_pos['fh'] = car_pos['front_height']
        self.car_pos['bh'] = car_pos['rear_height']
        self.car_pos['rh'] = car_pos['right_height']
        self.car_pos['lh'] = car_pos['left_height']
        self.car_pos['dir'] = car_pos['direction']

    def get_car_pos(self):
        return self.car_pos
    
    def calculate_shadow_pos(self):
        self.shadow_pos['cf'] = getTransformedLength(l=self.car_pos['hdtf'], h1=self.car_pos['fh'], h2=self.lamp['hfr'])
        self.shadow_pos['cb'] = getTransformedLength(l=self.car_pos['hdtb'], h1=self.car_pos['bh'], h2=self.lamp['hfr'])
        self.shadow_pos['cr'] = getTransformedLength(l=self.car_pos['hdtr'], h1=self.car_pos['rh'], h2=self.lamp['hfr'])
        self.shadow_pos['cl'] = getTransformedLength(l=self.car_pos['hdtl'], h1=self.car_pos['lh'], h2=self.lamp['hfr'])

    def get_shadow_pos(self):
        return self.shadow_pos
