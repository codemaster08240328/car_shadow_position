from math import pi, cos
earth_r = 6371000 # unit: m


def getTransformedLength(l, h1, h2):
    ratio = h2 / (h2 - h1)
    
    return l * ratio


def convertDistToLat(l):
    radian = l / earth_r
    lat = radian / pi * 180

    return lat


def convertDistToLon(l, lat):
    lat_radian = lat / 180 * pi
    r = earth_r * cos(lat_radian)

    radian = l / r
    lon = radian / pi * 180

    return lon
