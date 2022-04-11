from rng import *
from delaunay import *
from utils import *
from tp3 import *



def printTitle(title):
	print("\033[93m----==", title, "==----\033[0m")

def printBlink(text):
	print("\033[5m\033[34m", text, "\033[0m", sep="")

def printOK(text):
	print("\033[92mOK "+ text +"\033[0m")

def printKO(text):
	print("\033[91mTest failed: "+text+" ...\033[0m")



printTitle("Generate rooms")

genok = True
lrooms = generate_rooms(20,8,12,20,30)
if len(lrooms) != 20:
    printKO("generate_rooms : bad length of the list")
    genok = False
    
for room in lrooms:
    if room.sizeX < 8 or room.sizeX > 12 or room.sizeY < 8 or room.sizeY > 12 or room.cornerX < 0 or room.cornerY < 0 or room.cornerX >= 20 or room.cornerY >= 30: 
        printKO("generate_rooms : bad properties of a room")
        genok = False
        break

if genok:
    printOK(": generate_rooms")
    
print()


printTitle("Collision detection")

roomA = Room(10,10,0,0)
roomB = Room(15,15,15,15)
if not (collision_detection(roomA,roomB)):
    printOK(": test1")
else:
    printKO(": test1")

roomA = Room(10,10,5,5)
roomB = Room(10,10,0,0)
if (collision_detection(roomA,roomB)):
    printOK(": test2")
else:
    printKO(": test2")
    
print()



printTitle("Best move")

roomA = Room(5,4,0,0)
roomB = Room(5,1,1,2)
if best_move(roomA,roomB) != 1:
    printKO(": wrong room moved")
    
if roomB.sizeX != 5 or roomB.sizeY != 1 or roomB.cornerX != 1 or roomB.cornerY != 4:
    printKO(": wrong parameters in moved room")
else:
    printOK("")    
 
print()


printTitle("Minimum Spanning Tree")


if mst([[27, 34], [25, 22], [27, 9], [15, 31], [17, 11]], [(0, 1), (1, 3), (0, 3), (1, 2), (0, 2), (3, 4), (1, 4), (2, 4)]) != [(2, 4), (0, 1), (0, 3), (1, 2)]:
    printKO(": bad mst")
else:
    printOK(": good mst")

