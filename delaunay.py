import numpy
from scipy.spatial import Delaunay

def scalar(x1,y1,x2,y2,xP,yP):
    sign = (xP-x1)*(x2-x1) + (yP-y1)*(y2-y1)
    return (sign >= 0)

def inTriangle(x1,y1,x2,y2,x3,y3,xP,yP):
    sign1 = scalar(x1,y1,x2,y2,xP,yP)
    sign2 = scalar(x2,y2,x3,y3,xP,yP)
    sign3 = scalar(x3,y3,x1,y1,xP,yP)
    return sign1 == sign2 and sign1 == sign3


def center(room):
    return [room.cornerX + room.sizeX//2, room.cornerY + room.sizeY//2] 
    
def make_centers(lrooms):
    lcenters = []
    for room in lrooms:
        lcenters.append(center(room))
    return lcenters
    
def delaunay(lrooms):
    lcenters = make_centers(lrooms)
    centers = numpy.array(lcenters)
    triangles = Delaunay(centers)
    listEdges = []
    for triangle in triangles.simplices:
        tri = numpy.sort(triangle)
        v1 = tri[0],tri[1]
        v2 = tri[1],tri[2]
        v3 = tri[0],tri[2]
        if v1 not in listEdges:
            listEdges.append(v1)
        if v2 not in listEdges:
            listEdges.append(v2)
        if v3 not in listEdges:
            listEdges.append(v3)

    return listEdges, lcenters

#print(inTriangle(-2,-2,-2,2,-1,0,0,0))
