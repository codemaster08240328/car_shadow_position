from car_info import cars
from car import Car
from rotate_coordinate import CoordinateRotate
from utility import convertDistToLat, convertDistToLon

def main():
    car = Car(car_name=cars[1]['car_name'])
    car.set_camera(camera=cars[1]['camera'])
    car.set_car_pos(car_pos=cars[1]['car'])
    car.calculate_shadow_pos()

    shadow_pos_local = car.get_shadow_pos()
    transformedCoord = CoordinateRotate(ang=cars[1]['car']['direction'])

    sfl_local = {
        'x': shadow_pos_local['cf'],
        'y': shadow_pos_local['cl']
    }

    sfr_local = {
        'x': shadow_pos_local['cf'],
        'y': shadow_pos_local['cr']
    }

    sbl_local = {
        'x': shadow_pos_local['cb'],
        'y': shadow_pos_local['cl']
    }

    sbr_local = {
        'x': shadow_pos_local['cb'],
        'y': shadow_pos_local['cr']
    }

    sc_local = {
        'x': abs(shadow_pos_local['cf'] - shadow_pos_local['cb']) / 2,
        'y': abs(shadow_pos_local['cr'] - shadow_pos_local['cl']) / 2
    }

    sfl_tr = transformedCoord.transform(p=sfl_local)
    sfr_tr = transformedCoord.transform(p=sfr_local)
    sbl_tr = transformedCoord.transform(p=sbl_local)
    sbr_tr = transformedCoord.transform(p=sbr_local)
    sc_tr = transformedCoord.transform(p=sc_local)

    sfl = {}
    sfl['lat'] = car.get_camera()['lat'] + convertDistToLat(sfl_tr['y'])
    sfl['lon'] = car.get_camera()['lon'] + convertDistToLon(sfl_tr['x'], sfl['lat'])
    sfl['alt'] = car.get_camera()['alt'] - car.get_camera()['hfr']
    
    sfr = {}
    sfr['lat'] = car.get_camera()['lat'] - convertDistToLat(sfr_tr['y'])
    sfr['lon'] = car.get_camera()['lon'] + convertDistToLon(sfr_tr['x'], sfr['lat'])
    sfr['alt'] = car.get_camera()['alt'] - car.get_camera()['hfr']

    sbl = {}
    sbl['lat'] = car.get_camera()['lat'] + convertDistToLat(sbl_tr['y'])
    sbl['lon'] = car.get_camera()['lon'] - convertDistToLon(sbl_tr['x'], sbl['lat'])
    sbl['alt'] = car.get_camera()['alt'] - car.get_camera()['hfr']

    sbr = {}
    sbr['lat'] = car.get_camera()['lat'] - convertDistToLat(sbr_tr['y'])
    sbr['lon'] = car.get_camera()['lon'] - convertDistToLon(sbr_tr['x'], sbr['lat'])
    sbr['alt'] = car.get_camera()['alt'] - car.get_camera()['hfr']
    
    sc = {}
    sc['lat'] = car.get_camera()['lat'] + convertDistToLat(sc_tr['y']) if shadow_pos_local['cl'] > shadow_pos_local['cr'] else car.get_camera()['lat'] - convertDistToLat(sc_tr['y'])
    sc['lon'] = car.get_camera()['lon'] + convertDistToLon(sc_tr['x'], sc['lat']) if shadow_pos_local['cf'] > shadow_pos_local['cb'] else car.get_camera()['lon'] - convertDistToLon(sc_tr['x'], sc['lat'])
    sc['alt'] = car.get_camera()['alt'] - car.get_camera()['hfr']


    print(sfl)
    print(sfr)
    print(sbl)
    print(sbr)
    print(sc)

if __name__ == '__main__':
    main()
