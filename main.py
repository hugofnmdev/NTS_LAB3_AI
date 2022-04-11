from rng import *
from delaunay import *
from utils import *
from tp3 import *
import mst_sol




def createMaze(n,sizeX,sizeY,maxX,maxY,sizeMainX,sizeMainY):

    list_corridors = []

    ### Create rooms, then remove the over-lapping
    list_rooms = generate_rooms(n,sizeX,sizeY,maxX,maxY)
    #separation_steering_behavior(list_rooms)
    #main_rooms = choose_main_rooms(list_rooms,sizeMainX,sizeMainY)
    
    ### Create a minimum spanning tree (delaunay is given)
    #list_edges, list_centers = delaunay(main_rooms)
    #minspantree = mst(list_centers,list_edges)
    
    ### From the Tree, create the corridors
    #list_corridors = make_corridors(list_centers,minspantree)
    #list_rooms = filter_rooms(list_rooms,list_corridors)
    
    ### I do this part, enjoy the show
    xMax, yMax, xMin, yMin = findNewDimensions(list_rooms)
    return generateGrid(dimX,dimY,main_rooms,list_corridors)
    
prettyPrint(createMaze(50,5,15,40,40,6,6))


