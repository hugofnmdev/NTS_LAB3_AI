from rng import *
from delaunay import *

SEED  = 6729
rng = PseudoRNG(46613,17,SEED)

class Room:
  
    def __init__(self,sizeX,sizeY,cornerX,cornerY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.cornerX = cornerX
        self.cornerY = cornerY
        
class Corridor:
    def __init__(self,sizeX,sizeY,cornerX,cornerY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.cornerX = cornerX
        self.cornerY = cornerY



def generate_rooms(room_number,size_min,size_max,dimensionX,dimensionY):
    """
    @param room_number: positive integer
    @param size_min: positive integer, minimal size of a side
    @param size_max: positive integer, maximal size of a side
    @param dimensionX: positive integer, 
    @param dimensionY: positive integer
    @return a list of room_number rooms where the corner is in [0,dimensionX[ X [0,dimensionY[ 
    """
    roomlist = []
    i=0
    if (size_min < 3 or size_max < 3):
        raise Exception("size_min and size_max must be greater than 2")
    while i <= room_number:
        sizeX = rng.randInt(size_min,size_max)
        sizeY = rng.randInt(size_min,size_max)
        cornerX = rng.randInt(0,dimensionX-sizeX)
        cornerY = rng.randInt(0,dimensionY-sizeY)
        roomlist.append(Room(sizeX,sizeY,cornerX,cornerY))
        i += 1
    return roomlist


def collision_detection(roomA,roomB):
    """
    @param roomA: Room
    @param roomB: Room
    @return True if both rooms overlap, False else
    """
    res = False
    if (roomA.cornerX < roomB.cornerX + roomB.sizeX and roomA.cornerX + roomA.sizeX > roomB.cornerX and roomA.cornerY < roomB.cornerY + roomB.sizeY and roomA.cornerY + roomA.sizeY > roomB.cornerY):
        res = True
    return res
    
    
def best_move(roomA,roomB):
    """
    @param roomA: Room
    @param roomB: Room that overlaps with roomA
    Moves one of both rooms according to the rules in the subject 
    """
    if collision_detection(roomA,roomB):
        if roomA.cornerX < roomB.cornerX:
            roomA.cornerX += 1
        elif roomA.cornerY < roomB.cornerY:
            roomA.cornerY += 1

def separation_steering_behavior(list_rooms):
    """
    @param list_rooms: a list of rooms
    Moves the rooms until there are no more overlapping rooms.
    """
    for i in range(len(list_rooms)):
        for j in range(i+1,len(list_rooms)):
            best_move(list_rooms[i],list_rooms[j])
    

def choose_main_rooms(list_rooms,sizeXmin,sizeYmin):
    """
    @param list_rooms: a list of rooms
    @param sizeXmin: positive integer
    @param sizeYmin: positive integer
    @return a list of rooms that have dimensions > sizeXmin, sizeYmin
    """
    mainrooms = []
    for room in list_rooms:
        if room.sizeX > sizeXmin and room.sizeY > sizeYmin:
            mainrooms.append(room)
    return mainrooms


def distance_squared(center1,center2):
    """
    @param center1: couple of integers
    @param center2: couple of integers
    @return the square of the euclidean distance between center1 and center2
    """
    distance = 0
    for i in range(len(center1)):
        distance += (center1[i] - center2[i])**2
    return distance
    

def mst(list_centers,list_vertices):
    """
    @param list_centers: a list of couple of integers that represent coordinates
    @param list_vertices: a list of couples of integers i,j that represent centers, ie center i has coordinates list_centers[i]
    list_vertices, list_centers is the result of the Delaunay procedure
    @return the minimum (euclidean) spanning tree as a list of couples of integers i,j that represent centers, ie center i has coordinates list_centers[i]
    """
    return []
    

def make_corridors(list_centers, list_corridors):
    """
    @param list_corridors: a list of couple of integers that represent coordinates
    @param list_corridors: a list of couples of integers i,j that represent centers, ie center i has coordinates list_centers[i]
    @return a list of Corridors
    """
    corridorlist = []

    return corridorlist



def filter_rooms(list_rooms, list_corridor):
    """
    @param list_rooms: a list of rooms
    @param list_corridors: a list of corridors
    @return a list of all rooms that overlap at least one corridor
    """
    roomsfiltered = []
    for room in list_rooms:
        for corridor in list_corridor:
            if collision_detection(room,corridor):
                roomsfiltered.append(room)
    return roomsfiltered