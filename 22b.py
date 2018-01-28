from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class NodeState(Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3

def getNewNodeState(state):
    if state == NodeState.CLEAN:
        return NodeState.WEAKENED
    elif state == NodeState.WEAKENED:
        return NodeState.INFECTED
    elif state == NodeState.INFECTED:
        return NodeState.FLAGGED
    elif state == NodeState.FLAGGED:
        return NodeState.CLEAN

def getDirection(state, currentDir):
    if state == NodeState.INFECTED:
        if currentDir == Direction.UP:
            return Direction.RIGHT
        elif currentDir == Direction.DOWN:
            return Direction.LEFT
        elif currentDir == Direction.LEFT:
            return Direction.UP
        elif currentDir == Direction.RIGHT:
            return Direction.DOWN
    elif state == NodeState.CLEAN:
        if currentDir == Direction.UP:
            return Direction.LEFT
        elif currentDir == Direction.DOWN:
            return Direction.RIGHT
        elif currentDir == Direction.LEFT:
            return Direction.DOWN
        elif currentDir == Direction.RIGHT:
            return Direction.UP
    elif state == NodeState.WEAKENED:
        return currentDir
    elif state == NodeState.FLAGGED:
        if currentDir == Direction.UP:
            return Direction.DOWN
        elif currentDir == Direction.DOWN:
            return Direction.UP
        elif currentDir == Direction.LEFT:
            return Direction.RIGHT
        elif currentDir == Direction.RIGHT:
            return Direction.LEFT

def getPosition(location, currentDir):
    newLocationX = location[0]
    newLocationY = location[1]
    if currentDir == Direction.UP:
        newLocationX -= 1
    elif currentDir == Direction.DOWN:
        newLocationX += 1
    elif currentDir == Direction.LEFT:
        newLocationY -= 1
    elif currentDir == Direction.RIGHT:
        newLocationY += 1

    return (newLocationX, newLocationY)

f = open("22input.txt")

detectedNodes = set()
labelledNodes = {}

i = 0
j = 0
for line in f.readlines():
    j = 0
    for c in line.rstrip():
        if c == "#":
            detectedNodes.add((i,j))
            labelledNodes[(i, j)] = NodeState.INFECTED
        j += 1
    i += 1

location = (i // 2, j // 2)

numIterations = 10000000
numBurstsInfected = 0

direction = Direction.UP

i = 0

while i < numIterations:
    if location in detectedNodes:
        nodeState = labelledNodes[location]
        direction = getDirection(labelledNodes[location], direction)
        labelledNodes[location] = getNewNodeState(labelledNodes[location])
        if labelledNodes[location] == NodeState.INFECTED:
            numBurstsInfected += 1
        if labelledNodes[location] == NodeState.CLEAN:
            detectedNodes.remove(location)
    else:
        labelledNodes[location] = NodeState.CLEAN
        direction = getDirection(labelledNodes[location], direction)
        detectedNodes.add(location)
        labelledNodes[location] = getNewNodeState(labelledNodes[location])

    location = getPosition(location, direction)

    i += 1

print(numBurstsInfected)
