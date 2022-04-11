
def findNewDimensions(lrooms):
    xMax = -1000000
    yMax = -1000000
    xMin = 1000000
    yMin = 1000000
    for room in lrooms:
        xMin = min(xMin,room.cornerX)
        yMin = min(yMin,room.cornerY)
        xMax = max(xMax,room.cornerX+room.sizeX+1)
        yMax = max(yMax,room.cornerY+room.sizeY+1)
    return xMax, yMax, xMin, yMin


def generateGrid(xMax, yMax, xMin, yMin,lrooms,corridorRooms):
    grid = [(["#"]*(yMax-yMin-1))for i in range(xMax-xMin-1)]
    for room in corridorRooms:
        for i in range(room.sizeX):
            for j in range(room.sizeY):
                grid[i+room.cornerX-xMin][j+room.cornerY-yMin] = "."
    for room in lrooms:
        for i in range(1,room.sizeX-1):
            for j in range(1,room.sizeY-1):
                grid[i+room.cornerX-xMin][j+room.cornerY-yMin] = " "
    return grid

            

def prettyPrint(grid):
    for line in grid:
        for c in line:
            print(c,end="")
        print()




