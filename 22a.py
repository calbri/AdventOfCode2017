from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def getDirection(infected, currentDir):
    if infected:
        if currentDir == Direction.UP:
            return Direction.RIGHT
        elif currentDir == Direction.DOWN:
            return Direction.LEFT
        elif currentDir == Direction.LEFT:
            return Direction.UP
        elif currentDir == Direction.RIGHT:
            return Direction.DOWN
    else:
        if currentDir == Direction.UP:
            return Direction.LEFT
        elif currentDir == Direction.DOWN:
            return Direction.RIGHT
        elif currentDir == Direction.LEFT:
            return Direction.DOWN
        elif currentDir == Direction.RIGHT:
            return Direction.UP

def getPosition(location, currentDir):
    newLocation = [location[0], location[1]]
    if currentDir == Direction.UP:
        newLocation[0] -= 1
    elif currentDir == Direction.DOWN:
        newLocation[0] += 1
    elif currentDir == Direction.LEFT:
        newLocation[1] -= 1
    elif currentDir == Direction.RIGHT:
        newLocation[1] += 1

    return newLocation

f = open("22input.txt")

infectedNodes = []

i = 0
j = 0
for line in f.readlines():
    j = 0
    for c in line.rstrip():
        if c == "#":
            infectedNodes.append([i,j])
        j += 1
    i += 1

location = [i // 2, j // 2]

numIterations = 10000
numBurstsInfected = 0

direction = Direction.UP

for i in range(0, numIterations):
    if location in infectedNodes:
        direction = getDirection(True, direction)
        infectedNodes.remove(location)
    else:
        direction = getDirection(False, direction)
        infectedNodes.append(location)
        numBurstsInfected += 1

    location = getPosition(location, direction)

print(numBurstsInfected)
