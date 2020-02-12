import math
from pprint import pprint
from geojson import FeatureCollection, Feature, Polygon, Point

R=6_371_000 #Earth Radius

def rotate(point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    px, py = point

    qx = math.cos(angle) * (px) - math.sin(angle) * (py )
    qy =  math.sin(angle) * (px) + math.cos(angle) * (py )
    return qx, qy

#Get area of polygone
def get_area(points):
    s=0
    n=len(points)
    for i in range(n):
        x1,y1=points[i]
        x2,y2=points[(i+1)%n]
        s+=(y1+y2)/2*(x2-x1)
    return abs(s)
def calc(lat,lon,alt,direction,camera_front,camera_rear,camera_right,camera_left,camera_heigh,front_heigh,rear_heigh,right_heigh,left_heigh):
    dy2=dy1=-camera_heigh/(camera_heigh-front_heigh) * camera_front

    dx1 = -camera_heigh/(camera_heigh - front_heigh)*camera_left
    dx2=   camera_heigh/(camera_heigh - front_heigh) *camera_right
    dx3 = -camera_heigh/(camera_heigh - rear_heigh) *camera_left
    dx4 = camera_heigh/(camera_heigh - rear_heigh)  *camera_right

    dy3 = dy4 = camera_heigh/(camera_heigh - rear_heigh) * camera_rear

    #Find center mass of figure
    #We divide it on 2 thriange find center mass of each and then find common center mass
    a1=get_area([(dx1,dy1),(dx2,dy2),(dx3,dy3),])
    a2 = get_area([(dx4, dy4), (dx2, dy2), (dx3, dy3), ])

    dx5=((dx1+dx2+dx3)/3*a1+(dx4+dx2+dx3)/3*a2)/(a1+a2)
    dy5=((dy1+dy2+dy3)/3*a1+(dy4+dy2+dy3)/3*a2)/(a1+a2)

    deltas=[
        (dx1,dy1),
        (dx2, dy2),
        (dx3, dy3),
        (dx4, dy4),

        (dx5, dy5),
    ]

    for i,coord in enumerate(deltas):
        dx1,dy1=coord
        deltas[i]=rotate((dx1,dy1),direction/180*math.pi)

    one_lat=R*math.pi/180
    one_lon=R*math.cos(lat/180*math.pi)*math.pi/180
    coordinates=[]

    surface_alt=alt-camera_heigh
    for i, coord in enumerate(deltas):
        dx1, dy1 = coord
        plon=lon+dx1/one_lon
        if plon>90:
            plon=180-plon
        if plon<-90:
            plon=-180-plon
        plat=lat- dy1 / one_lat
        if plat>180:
            plat=plat-360
        if plat < -180:
            plat = plat+360
        coordinates.append((plat,plon,surface_alt))

    return coordinates
""" pprint(calc(70,10,100,180,1,1,1,1,2,1,1,1,1)) """


#  Test
result = calc(49.990058,8.678522,140,264.09,2.5,2.0,0.9,0.9,1.96,0.9,1.5,1.5,1.5)
